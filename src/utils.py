def resize_frame(frame, width):
    height = int(frame.shape[0] * (width / frame.shape[1]))
    return cv2.resize(frame, (width, height))

def convert_to_gray(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)