from flask import Flask, request, render_template
import cv2
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/detect", methods=["POST"])
def detect():
    file = request.files['image']
    img = np.frombuffer(file.read(), np.uint8)
    image = cv2.imdecode(img, cv2.IMREAD_COLOR)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,4)

    return f"Faces detected: {len(faces)}"

app.run(host="0.0.0.0", port=5000)