pip install --quiet gradio

import gradio as gr
import tensorflow as tf
import numpy as np 
import pandas as pd
import requests
from urllib.request import urlretrieve


from numpy import loadtxt 
from tensorflow.keras.models import load_model 

model = load_model('/Users/sadaf/Desktop/Python/cnn_img/cell_images/malaria_model_acc95.h5')

from tensorflow.keras.preprocessing import image

from numpy import argmax


def my_predict(image):
  image = image.reshape(1, 130, 130, 3)
  prediction = model.predict(image)
  if prediction == 0:
      return "The cell is infected."
  else:
      return "The cell is NOT infected."
  
urlretrieve("https://i.pinimg.com/originals/3b/96/c2/3b96c22bf9672e656800218e10dd2162.png","infected_cell.png")
urlretrieve('https://i.pinimg.com/originals/2b/8f/d6/2b8fd6e0c1b224121957bcb46ccc4f4a.png','uninfected_cell.png')
urlretrieve('https://i.pinimg.com/originals/9f/ed/60/9fed60da9e972bf31f1be75cbe0b42a8.png','malaria_thumbnail.png')


sample_images = [
    ["infected_cell.png"],
    ['uninfected_cell.png']
]

thumb = [['malaria_thumbnail.png']]


gr.Interface(
    fn=my_predict, 
    inputs=gr.Image(shape=(130,130)),
    outputs = gr.Textbox(label='Result'),
    allow_flagging= "never",
    title = 'Welcome to MICP: Malaria Infected-Cell Predictor ',
    description= """This tool predicts malaria-infected cells. Deep learning approach has been used to design MICP with the accuracy of 95%.
    \nUpload your cell image and click 'Submit' button or click one of the examples to load them.
    """,
    article ='''<html>
   <head>
   </head>

   <body>
      <div style = "position:relative; text-align: center;">
         Created by Seyedehsadaf Asfa & Reza Arshinchi Bonab
      </div>
   </body>
</html>''',
    thumbnail= thumb,
    examples=sample_images).launch(inbrowser=True,share=True)