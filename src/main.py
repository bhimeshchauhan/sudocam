from __future__ import absolute_import
from flask import Flask, render_template, Response

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def hello_world(name=None):
  return render_template('main.html', name="bhimesh")


def gen(camera):
    while True:
        # get camera frame
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/camera')
def camera(frame=None):
  from .scripts import camera
  return Response(gen(camera.VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')
