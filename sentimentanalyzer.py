import os
import re
import shutil
import string
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import losses
import pandas as pd
from pandas import *


data = read_csv("headlinesAndSentiments.csv")


# converting column data to list
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

#positiveHeadlines = []
#negativeHeadlines = []

#for i in range(len(sentimentIntegers)):
#  if sentimentIntegers[i] == 1:
#    positiveHeadlines.append(headlines[i])
#  elif sentimentIntegers[i] == -1:
#    negativeHeadlines.append(headlines[i])

#for i in range(len(positiveHeadlines)):
#  f = open("aclImdb/train/pos/" + str(i) + ".txt", "x", encoding='utf-8')
#  f.write(positiveHeadlines[i])

#for i in range(len(negativeHeadlines)):
#  f = open("aclImdb/train/neg/" + str(i) + ".txt", "x", encoding='utf-8')
#  f.write(negativeHeadlines[i])

#url = "https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"


#dataset = tf.keras.utils.get_file("aclImdb_v1", url,
#                                    untar=True, cache_dir='.',
#                                    cache_subdir='')


#dataset_dir = os.path.join(os.path.dirname(dataset), 'aclImdb')


#os.listdir(dataset_dir)


#train_dir = os.path.join(dataset_dir, 'train')
#os.listdir(train_dir)


#sample_file = os.path.join(train_dir, 'pos/1181_9.txt')
#with open(sample_file) as f:
  #print(f.read())


#remove_dir = os.path.join(train_dir, 'unsup')
#shutil.rmtree(remove_dir)


batch_size = 32
seed = 42


raw_train_ds = tf.keras.utils.text_dataset_from_directory(
    'sentimentsAndHeadlines/train',
    batch_size=batch_size,
    validation_split=0.2,
    subset='training',
    seed=seed)


#for text_batch, label_batch in raw_train_ds.take(1):
  #for i in range(3):
    #print("Review", text_batch.numpy()[i])
    #print("Label", label_batch.numpy()[i])
   
raw_val_ds = tf.keras.utils.text_dataset_from_directory(
    'sentimentsAndHeadlines/train',
    batch_size=batch_size,
    validation_split=0.2,
    subset='validation',
    seed=seed)


#raw_test_ds = tf.keras.utils.text_dataset_from_directory(
#    'aclImdb/test',
#    batch_size=batch_size)


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
#print("Review", first_review)
#print("Label", raw_train_ds.class_names[first_label])
#print("Vectorized review", vectorize_text(first_review, first_label))


#print("1287 ---> ",vectorize_layer.get_vocabulary()[1287])
#print(" 313 ---> ",vectorize_layer.get_vocabulary()[313])
#print('Vocabulary size: {}'.format(len(vectorize_layer.get_vocabulary())))


train_ds = raw_train_ds.map(vectorize_text)
print(train_ds)
val_ds = raw_val_ds.map(vectorize_text)
#test_ds = raw_test_ds.map(vectorize_text)


AUTOTUNE = tf.data.AUTOTUNE


#print()
#print("type(train_ds)")
#print(type(train_ds))
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

#for file in ["ckpt", "ckpt25", "ckpt50", "ckpt100", "ckpt250", "ckpt500", "ckpt1000"]:
#  print(file)
#model.load_weights("ckpt")
#  loss, accuracy = model.evaluate(test_ds)
#  print("Loss: " + str(loss))
#  print("Accuracy: " + str(accuracy))

#epochs = 350
#history = model.fit(
#    train_ds,
#    validation_data=val_ds,
#    epochs=epochs)

model.load_weights("ckpt350")

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
#print(type(predictions))
#print(type(predictions[0]))

f = open("predictions.txt", "a")
for i in range(len(predictions)):
  f.write(str(predictions[i][0]) + ", " + str(sentimentIntegers[i]) + "\n")
f.close()

#  predictionsMatrix = [[]]
#  predictionsMatrixCorrect = []
#  headlineAccuracy = []

#  for i in range(20):
#    threshold = i / 40
#    predictionsInt = []
#    for prediction in predictions:
#      if prediction < .5 - threshold:
#        predictionsInt.append(-1)
#      elif prediction > .5 + threshold:
#        predictionsInt.append(1)
#      else:
#        predictionsInt.append(0)
#    predictionsMatrix.append(predictionsInt)
#    numSame = sum(x == y for x, y in zip(predictionsInt, sentimentIntegers))
#    headlineAccuracy.append(numSame / len(predictionsInt))

#  maxValue = max(headlineAccuracy)
#  maxIndex = headlineAccuracy.index(maxValue)

#  print("maxValue: " + str(maxValue))
#  print("maxIndex: " + str(maxIndex))