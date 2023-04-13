import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import tensorflow_hub as hub
import tensorflow_text as text  # Imports TF ops for preprocessing.
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# importing module
from pandas import *
 
# reading CSV file
data = read_csv("headlinesAndSentiments.csv")

print(-3)

# converting column data to list
headlines = data['Sentence'].to_list()

print(-2)

def toInteger(str):
  if str == 'positive':
    return 1
  elif str == 'neutral':
    return 0
  elif str == 'negative':
    return -1
sentimentTexts = data['Sentiment'].to_list()
sentiments = list(map(toInteger, sentimentTexts))

print(-1)

# Make NumPy printouts easier to read.
np.set_printoptions(precision=3, suppress=True)

print(0)

# Load the BERT encoder and preprocessing models
preprocess = hub.load('https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3')

print(1)

# Convert the sentences to bert inputs
bert_inputs = preprocess(headlines)

print(2)

# Feed the inputs to the model to get the pooled and sequence outputs
print(bert_inputs)