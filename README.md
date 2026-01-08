# Image Recognition System

A Python-based Image Recognition System that trains a machine learning model on custom image datasets and provides a web interface to upload images and get predictions.

---

## 📌 Project Overview

This project allows users to:
- Train an image classification model using a dataset
- Upload images through a web application
- Predict the class of the uploaded image
- Use a simple and modular Python project structure

---

## 📁 Project Structure


Image-recognition-system/
│
├── dataset/                # Training and testing images
│   ├── train/
│   └── test/
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
````

---

## ⚙️ Technologies Used

* Python
* Flask
* TensorFlow / Keras
* NumPy
* OpenCV
* HTML / CSS

---

## 📦 Installation

Clone the repository:


git clone https://github.com/vedant4X/Image-recognition-system.git
cd Image-recognition-system
```

Create a virtual environment (optional but recommended):


python -m venv venv
```

Activate virtual environment:


# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

Install required packages:


pip install -r requirements.txt
```

---

## 🧠 Train the Model

Before running the app, train the model using your dataset:


python train_model.py
```

After successful training, the model file will be saved in the `model/` directory.

---

## 🚀 Run the Application

Start the Flask web app:


python app.py
```

Open your browser and go to:


http://127.0.0.1:5000
```

Upload an image to get predictions.

---

## 🧪 Dataset Guidelines

* Place images inside `dataset/train/` and `dataset/test/`
* Each class should be in a separate folder
* Example:


dataset/train/dog/
dataset/train/cat/
dataset/test/dog/
dataset/test/cat/
```

---

## ✅ Features

* Custom image dataset support
* Simple web UI
* Easy training and prediction
* Beginner-friendly project structure

---

## ❗ Common Issues

* **Model not found**: Make sure `train_model.py` is run before `app.py`
* **Wrong predictions**: Ensure dataset is properly labeled
* **Module not found error**: Install dependencies correctly

---

## 🔮 Future Improvements

* Add real-time camera detection
* Improve model accuracy
* Deploy on cloud (AWS / Render / Heroku)
* Add user authentication

---

## 📜 License

This project is for educational purposes.

---

## 👤 Author

**Vedant**
GitHub: [https://github.com/vedant4X](https://github.com/vedant4X)

```

---

