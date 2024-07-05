import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.join(CURRENT_DIR, "../models/braintumor.h5")
LABELS = os.path.join(CURRENT_DIR, "../models/classes.txt")

def get_models():
    global model
    from keras.models import load_model
    model = load_model(MODEL)
    print("MODEL LOADED")

def get_image_results(image_path, target_size):
    from keras.preprocessing.image import img_to_array
    from PIL import Image
    import numpy as np
    image = Image.open(image_path)
    if image.mode != "RGB":
        image = image.convert("RGB")

    image = image.resize(target_size)
    img_array = img_to_array(image)
    img_array = img_array.reshape(1, 150, 150, 3)
    get_models()
    result = model.predict(img_array)
    return result