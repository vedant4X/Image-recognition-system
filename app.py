from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
import cv2
import os

app = Flask(__name__)

# ---------- BASE PATH ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------- UPLOAD FOLDER ----------
UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ---------- LOAD MODEL ----------
MODEL_PATH = os.path.join(BASE_DIR, "model", "image_model.h5")
model = tf.keras.models.load_model(MODEL_PATH)

# ---------- LOAD CLASS LABELS (FIXED) ----------
# MUST match training folders: dataset/train/cat , dataset/train/dog
TRAIN_DIR = os.path.join(BASE_DIR, "dataset", "train")
class_labels = sorted(os.listdir(TRAIN_DIR))

print("CLASS LABELS:", class_labels)  # should print ['cat', 'dog']

# ---------- ROUTES ----------
@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        file = request.files.get("image")

        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            img = cv2.imread(filepath)
            img = cv2.resize(img, (128, 128))   # MUST match training size
            img = img / 255.0
            img = np.reshape(img, (1, 128, 128, 3))

            pred = model.predict(img)
            prediction = class_labels[np.argmax(pred)]

    return render_template("index.html", prediction=prediction)

# ---------- RUN ----------
if __name__ == "__main__":
    app.run(debug=True)
