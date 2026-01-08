# Image Recognition System

A Python-based Image Recognition System that trains a machine learning model on custom image datasets and provides a web interface to upload images and get predictions.

---

## 📌 Project Overview

This project allows users to:
- Train an image classification model using a custom dataset
- Upload images through a web application
- Predict the class of uploaded images
- Understand end-to-end image recognition workflow

---

## 📁 Project Structure

```bash
Image-recognition-system/
│
├── dataset/                # Training and testing images
│   ├── train/
│   │   ├── class1/
│   │   └── class2/
│   └── test/
│       ├── class1/
│       └── class2/
│
├── model/                  # Saved trained model
│
├── static/
│   └── uploads/            # Uploaded images
│
├── templates/              # HTML templates
│   └── index.html
│
├── app.py                  # Flask web application
├── train_model.py          # Model training script
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
