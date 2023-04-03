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
 
# converting column data to list
headlines = data['Sentence'].to_list()

def toInteger(str):
  if str == 'positive':
    return 1
  elif str == 'neutral':
    return 0
  elif str == 'negative':
    return -1
sentimentTexts = data['Sentiment'].to_list()
sentiments = list(map(toInteger, sentimentTexts))

# Make NumPy printouts easier to read.
np.set_printoptions(precision=3, suppress=True)

# Load the BERT encoder and preprocessing models
preprocess = hub.load('https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3')
bert = hub.load('https://tfhub.dev/google/experts/bert/wiki_books/sst2/2')

# Convert the sentences to bert inputs
bert_inputs = preprocess(headlines)

# Feed the inputs to the model to get the pooled and sequence outputs
bert_outputs = bert(bert_inputs, training=False)
pooled_output = bert_outputs['pooled_output']
sequence_output = bert_outputs['sequence_output']

print(type(pooled_output))