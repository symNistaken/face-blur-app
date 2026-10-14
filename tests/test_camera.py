import sys
from pathlib import Path
import unittest
from unittest.mock import Mock, patch
import numpy as np
import cv2
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import main
from face_blur import blur_faces


class CameraTests(unittest.TestCase):
    def setUp(self):
        self.capture = Mock()
        self.capture.isOpened.return_value = True
        self.capture.read.return_value = (True, np.zeros((120,160,3), dtype=np.uint8))
        self.cascade = Mock()
        self.cascade.empty.return_value = False
        self.cascade.detectMultiScale.return_value = []

    def run_main(self, display_error=None):
        with patch.object(main.cv2, 'VideoCapture', return_value=self.capture), patch.object(main.cv2, 'CascadeClassifier', return_value=self.cascade), patch.object(main.cv2, 'imshow', side_effect=display_error), patch.object(main.cv2, 'waitKey', return_value=ord('q')), patch.object(main.cv2, 'destroyAllWindows') as cleanup:
            result = main.main()
            cleanup.assert_called_once()
        return result

    def test_q_stops_and_releases_camera(self):
        self.assertEqual(self.run_main(), 0)
        self.capture.release.assert_called_once()

    def test_camera_open_failure_releases_resources(self):
        self.capture.isOpened.return_value = False
        self.assertEqual(self.run_main(), 1)
        self.capture.release.assert_called_once()

    def test_read_failure_releases_resources(self):
        self.capture.read.return_value = (False, None)
        self.assertEqual(self.run_main(), 1)
        self.capture.release.assert_called_once()

    def test_display_exception_still_releases_camera(self):
        with self.assertRaises(cv2.error):
            self.run_main(cv2.error('display failed'))
        self.capture.release.assert_called_once()

    def test_missing_cascade_does_not_open_camera(self):
        self.cascade.empty.return_value = True
        with patch.object(main.cv2, 'CascadeClassifier', return_value=self.cascade), patch.object(main.cv2, 'VideoCapture') as opening:
            self.assertEqual(main.main(), 1)
            opening.assert_not_called()


class BlurTests(unittest.TestCase):
    def test_blur_changes_only_detected_region(self):
        image = np.random.default_rng(42).integers(0,256,(120,160,3),dtype=np.uint8)
        cascade = Mock()
        cascade.detectMultiScale.return_value = [(10,10,20,20)]
        result = blur_faces(image.copy(), cascade)
        self.assertFalse(np.array_equal(result[20:60,20:60], image[20:60,20:60]))
        self.assertTrue(np.array_equal(result[:20], image[:20]))

    def test_tiny_frame_and_outside_boxes(self):
        cascade = Mock()
        cascade.detectMultiScale.return_value = [(-10,-10,1,1),(20,20,1,1)]
        self.assertEqual(blur_faces(np.zeros((1,1,3),dtype=np.uint8),cascade).shape, (1,1,3))

    def test_missing_frame_rejected(self):
        with self.assertRaises(ValueError):
            blur_faces(None, Mock())

    def test_bundled_cascade_loads(self):
        cascade = cv2.CascadeClassifier(str(Path(__file__).resolve().parents[1]/'src/haar_cascade/haarcascade_frontalface_default.xml'))
        self.assertFalse(cascade.empty())
