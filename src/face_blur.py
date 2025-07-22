import cv2

def blur_faces(frame, face_cascade):
    scale = 0.5  
    small_frame = cv2.resize(frame, (0, 0), fx=scale, fy=scale)
    gray = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        x_big, y_big, w_big, h_big = int(x/scale), int(y/scale), int(w/scale), int(h/scale)
        face_region = frame[y_big:y_big+h_big, x_big:x_big+w_big]
        blurred_face = cv2.GaussianBlur(face_region, (99, 99), 30)
        frame[y_big:y_big+h_big, x_big:x_big+w_big] = blurred_face

    return frame

def load_cascade(cascade_path):
    return cv2.CascadeClassifier(cascade_path)