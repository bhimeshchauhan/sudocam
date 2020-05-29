import cv2

class VideoCamera(object):
  def __init__(self):
    self.video = cv2.VideoCapture(0)
    self.frame = None

  def __del__(self):
    self.video.release()

  def draw_rectangle(self):
    height, width, channels = self.frame.shape
    upper_left = (int(width / 4), int(height / 4))
    bottom_right = (int(width * 3 / 4), int(height * 3 / 4))

    # draw in the image
    cv2.rectangle(self.frame, upper_left, bottom_right, (0, 255, 0), 2)


  def get_frame(self):
    success, self.frame = self.video.read()
    self.frame = cv2.flip(self.frame, 1)
    self.draw_rectangle()
    ret, self.frame = cv2.imencode('.jpg', self.frame)
    return self.frame.tobytes()