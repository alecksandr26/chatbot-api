import random
import json
import pickle
import numpy as np


import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

lemmatizer = WordNetLemmatizer()
intents = json.loads(open("intents.json").read())

words = []
classes = []
documents = []
ignore_letters = ["¿", "?", "¡", "!", ".", ",", "-", "_", ""]

for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        word_list = nltk.word_tokenize(pattern)        
        words.extend(word_list)
        documents.append((word_list, intent["tag"]))
        if intent["tag"] not in classes:
            classes.append(intent["tag"])

words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
words = sorted(set(words))
classses = sorted(set(classes))

pickle.dump(words, open('words.pk1', "wb"))
pickle.dump(classes, open("classes.pk1", "wb"))

training = []
output_empty = [0] * len(classes)

for document in documents:
    bag = []
    word_patterns = document[0]

    # Make it lower case
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    
    for word in words:
        if word in word_patterns:
            bag.append(1)
        else:
            bag.append(0)
    
    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])


random.shuffle(training)

# Getting the training data
train_x = np.array([item[0] for item in training])
train_y = np.array([item[1] for item in training])

print(train_x)
print(train_y)

# Build the model
model = Sequential()
model.add(Dense(128, input_shape = (len(train_x[0]), ), activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation = 'softmax'))
sgd = SGD(learning_rate = 0.01, decay = 1e-6, momentum = 0.9, nesterov = True)
model.compile(loss = 'categorical_crossentropy', optimizer = sgd, metrics = ["accuracy"])

# Train the model
model.fit(train_x, train_y, epochs = 200, batch_size = 5, verbose = 1)

model.save('chatbot_model_test.keras')
print("Done")

