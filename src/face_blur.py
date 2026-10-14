import cv2


def blur_faces(frame, face_cascade):
    if frame is None or frame.ndim != 3 or frame.shape[2] != 3 or not frame.size:
        raise ValueError('A non-empty BGR frame is required')
    height, width = frame.shape[:2]
    small_width, small_height = max(1, width // 2), max(1, height // 2)
    small_frame = cv2.resize(frame, (small_width, small_height))
    gray = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for x, y, w, h in faces:
        left, top = max(0, int(x * width / small_width)), max(0, int(y * height / small_height))
        right, bottom = min(width, int((x + w) * width / small_width)), min(height, int((y + h) * height / small_height))
        if right <= left or bottom <= top:
            continue
        region = frame[top:bottom, left:right]
        frame[top:bottom, left:right] = cv2.GaussianBlur(region, (99, 99), 30)
    return frame


def load_cascade(cascade_path):
    return cv2.CascadeClassifier(cascade_path)
