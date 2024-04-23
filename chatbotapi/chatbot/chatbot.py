import random
import json
import pickle
import numpy as np


import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model


lemmatizer = WordNetLemmatizer()
intents = json.loads(open("intents.json").read())

words = pickle.load(open("words.pk1", "rb"))
classes = pickle.load(open("classes.pk1", "rb"))


model = load_model("chatbot_model_test.keras")


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)

    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
            else:
                bag[i] = 0
    return np.array(bag)



def predict_class(sentence):
    X = bag_of_words(sentence)
    Y = model.predict(np.array([X]))[0]
    epsilon = 0.25
    results = [[i, r] for i, r in enumerate(Y) if r > epsilon]

    results.sort(key = lambda x: x[1], reverse = True)

    return_list = []
    for r in results:
        return_list.append({"intent" : classes[r[0]], "probability" : str(r[1])})
    return return_list



def get_response(intents_list, intents_json):
    tag = intents_list[0]["intent"]
    list_of_intents = intents_json["intents"]
    for i in list_of_intents:
        if i["tag"] == tag:
            result = random.choice(i["responses"])
            return result

print("\n\n\n")
while True:
    message = input("YOU: ")
    ints = predict_class(message)
    res = get_response(ints, intents)
    print("\nAI Chatbot: " + res, "\t", ints)
