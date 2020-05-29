import cv2

class VideoCamera(object):
  def __init__(self):
    self.video = cv2.VideoCapture(0)

  def __del__(self):
    self.video.release()

  def get_frame(self):
    success, frame = self.video.read()
    frame = cv2.flip(frame, 1)
    ret, frame = cv2.imencode('.jpg', frame)
    return frame.tobytes()