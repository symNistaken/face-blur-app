import sys
import os
import cv2
from face_blur import blur_faces


def main(camera_index=0):
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8', errors='replace')
    base_path = sys._MEIPASS if getattr(sys, 'frozen', False) else os.path.dirname(__file__)
    cascade_path = os.path.join(base_path, 'haar_cascade', 'haarcascade_frontalface_default.xml')
    face_cascade = cv2.CascadeClassifier(cascade_path)
    if face_cascade.empty():
        print('Cascade dosyası yüklenemedi:', cascade_path)
        return 1
    cap = cv2.VideoCapture(camera_index)
    try:
        if not cap.isOpened():
            print('Kamera açılamadı. Bağlantıyı ve izinleri kontrol edin.')
            return 1
        print("Uygulama başladı. Çıkmak için 'q' tuşuna basın.")
        while True:
            ret, frame = cap.read()
            if not ret or frame is None:
                print('Kameradan görüntü alınamadı.')
                return 1
            cv2.imshow('Face Blur Application', blur_faces(frame, face_cascade))
            if cv2.waitKey(1) & 0xFF == ord('q'):
                return 0
    finally:
        # Release the camera even on read failure or an OpenCV/window exception.
        cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Yerel webcam yüz bulanıklaştırma')
    parser.add_argument('--camera', type=int, default=0, help='Kamera indeksi (varsayılan: 0)')
    try:
        sys.exit(main(parser.parse_args().camera))
    except cv2.error:
        print('OpenCV görüntü veya pencere işlemini tamamlayamadı.')
        sys.exit(1)
