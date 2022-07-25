# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 18:50:57 2022

@author: siddhardhan
"""
import string

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()


class model_input(BaseModel):
    model: string
    price: int
    launch: int
    camera: int
    selfie: int
    audio: float
    display: float
    battery: int


# loading the saved model
diabetes_model = pickle.load(open('MobileModel.ipynb', 'rb'))


@app.post('/diabetes_prediction')
def diabetes_predd(input_parameters: model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)

    model = input_dictionary['model']
    price = input_dictionary['price']
    launch = input_dictionary['launch']
    camera = input_dictionary['camera']
    selfie = input_dictionary['selfie']
    audio = input_dictionary['audio']
    display = input_dictionary['display']
    battery = input_dictionary['battery']

    input_list = [model, price, launch, camera, selfie, audio, display, battery]

    prediction = diabetes_model.predict([input_list])

    if (prediction[0] == 0):
        return 'The mobile is  not found'
    else:
        return model


