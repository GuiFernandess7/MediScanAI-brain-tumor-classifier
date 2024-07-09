import os
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.join(CURRENT_DIR, "../models/braintumor.h5")
LABELS = os.path.join(CURRENT_DIR, "../models/classes.txt")

model = None

def get_models():
    global model
    if model is None:
        model = load_model(MODEL)
        print("MODEL LOADED")

def load_labels():
    with open(LABELS, 'r') as file:
        labels = [line.strip() for line in file.readlines()]
    return labels

def preprocess_image(image_path, target_size):
    image = Image.open(image_path)
    if image.mode != "RGB":
        image = image.convert("RGB")

    image = image.resize(target_size)
    img_array = img_to_array(image)
    img_array = img_array.reshape(1, *target_size, 3)
    img_array /= 255.0
    return img_array

def get_image_results(image_path, target_size=(150, 150)):
    get_models()
    img_array = preprocess_image(image_path, target_size)
    result = model.predict(img_array)
    return result

def format_predictions(predictions, labels):
    formatted_results = {label: float(f"{prob:.4f}") for label, prob in zip(labels, predictions[0])}
    return formatted_results
