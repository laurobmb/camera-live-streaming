from flask import Flask, render_template, Response
import cv2
import os

app = Flask(__name__)
LINK1 = os.getenv('LINK1')
LINK2 = os.getenv('LINK2')
LINK3 = os.getenv('LINK3')
camera1 = cv2.VideoCapture(LINK1)
camera2 = cv2.VideoCapture(LINK2)
camera3 = cv2.VideoCapture(LINK3)

def gen_frames(CAMERA):
    while True:
        success, frame = CAMERA.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed1')
def video_feed1():
    return Response(gen_frames(camera1),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed2')
def video_feed2():
    return Response(gen_frames(camera2),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed3')
def video_feed3():
    return Response(gen_frames(camera3),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/cam1')
def index1():
    return render_template('cam1.html')

@app.route('/cam2')
def index2():
    return render_template('cam2.html')

@app.route('/cam3')
def index3():
    return render_template('cam3.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
