import sys
import os
import cv2
from face_blur import blur_faces

def main():
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(__file__)

    cascade_path = os.path.join(base_path, 'haar_cascade', 'haarcascade_frontalface_default.xml')
    face_cascade = cv2.CascadeClassifier(cascade_path)

    if face_cascade.empty():
        print(f"Error: Cascade dosyası bulunamadı veya yüklenemedi: {cascade_path}")
        input("Çıkmak için Enter'a basın...")
        return

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        input("Çıkmak için Enter'a basın...")
        return

    print("Uygulama başladı. Çıkmak için 'q' tuşuna basın.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        blurred_frame = blur_faces(frame, face_cascade)
        cv2.imshow('Face Blur Application', blurred_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()