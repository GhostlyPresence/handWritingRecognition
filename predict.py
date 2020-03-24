from tensorflow import keras
from tensorflow.keras import backend as K
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

import base64
import io
import cv2
import numpy as np


def get_model():
    global classifier
    classifier = load_model('classifier/MNIST_Digit_recognizer.h5')

def preprocess_image(data):
    nparr = np.fromstring(data, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
    #image = np.array(image)
    #image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image,(28,28),cv2.INTER_AREA)
    #cv2.imwrite("image.jpg",image)
    image = image.reshape(1,28,28,1)
    image = image/255.0
    
    return image

def make_prediction(image):
    p = classifier.predict(image)
    p = p.tolist()
    return p

print("* Loading keras model......")
get_model()



