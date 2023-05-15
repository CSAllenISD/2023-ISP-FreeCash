import os
import re
import shutil
import string
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import losses
import pandas as pd
from pandas import *

data = read_csv("app\database\headlinesAndSentiments.csv")

# converting csv column data to list
headlines = data['Sentence'].to_list()
sentiments = data['Sentiment'].to_list()
sentimentIntegers = []
for sentiment in sentiments:
  assert sentiment == "positive" or sentiment == "negative" or sentiment == "neutral"
  if sentiment == "positive":
    sentimentIntegers.append(1)
  elif sentiment == "negative":
    sentimentIntegers.append(-1)
  else:
    sentimentIntegers.append(0)

i = 0

batch_size = 32
seed = 42


raw_train_ds = tf.keras.utils.text_dataset_from_directory(
    'train',
    batch_size=batch_size,
    validation_split=0.2,
    subset='training',
    seed=seed)

raw_val_ds = tf.keras.utils.text_dataset_from_directory(
    'train',
    batch_size=batch_size,
    validation_split=0.2,
    subset='validation',
    seed=seed)

def custom_standardization(input_data):
  lowercase = tf.strings.lower(input_data)
  stripped_html = tf.strings.regex_replace(lowercase, '<br />', ' ')
  return tf.strings.regex_replace(stripped_html,
                                  '[%s]' % re.escape(string.punctuation),
                                  '')


max_features = 10000
sequence_length = 250


vectorize_layer = layers.TextVectorization(
    standardize=custom_standardization,
    max_tokens=max_features,
    output_mode='int',
    output_sequence_length=sequence_length)


# Make a text-only dataset (without labels), then call adapt
train_text = raw_train_ds.map(lambda x, y: x)
vectorize_layer.adapt(train_text)


def vectorize_text(text, label):
  text = tf.expand_dims(text, -1)
  return vectorize_layer(text), label


# retrieve a batch (of 32 reviews and labels) from the dataset
text_batch, label_batch = next(iter(raw_train_ds))
first_review, first_label = text_batch[0], label_batch[0]

train_ds = raw_train_ds.map(vectorize_text)
print(train_ds)
val_ds = raw_val_ds.map(vectorize_text)
#test_ds = raw_test_ds.map(vectorize_text)


AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
#test_ds = test_ds.cache().prefetch(buffer_size=AUTOTUNE)


embedding_dim = 16


model = tf.keras.Sequential([
  layers.Embedding(max_features + 1, embedding_dim),
  layers.Dropout(0.5),
  layers.GlobalAveragePooling1D(),
  layers.Dropout(0.5),
  layers.Dense(1)])

model.compile(loss=losses.BinaryCrossentropy(from_logits=True),
              optimizer='adam',
              metrics=tf.metrics.BinaryAccuracy(threshold=0.0))

model.load_weights("app/models/ckpt350")

#print("Loss: ", loss)
#print("Accuracy: ", accuracy)


export_model = tf.keras.Sequential([
  vectorize_layer,
  model,
  layers.Activation('sigmoid')
])


export_model.compile(
    loss=losses.BinaryCrossentropy(from_logits=False), optimizer="adam", metrics=['accuracy']
)

# Test it with `raw_test_ds`, which yields raw strings
#loss, accuracy = export_model.evaluate(raw_test_ds)
#print(accuracy)
    
examples = headlines

predictions = export_model.predict(examples)

f = open("train/predictions.txt", "a")
for i in range(len(predictions)):
  f.write(str(predictions[i][0]) + ", " + str(sentimentIntegers[i]) + "\n")
f.close()