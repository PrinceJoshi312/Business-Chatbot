# Importing necessary libraries
import json  # Library for working with JSON data
import random  # Library for generating random numbers and selections
import pickle  # Library for serializing and deserializing Python objects
import numpy as np  # Library for numerical operations

import nltk  # Natural Language Toolkit for text processing
from nltk.stem import WordNetLemmatizer  # Lemmatization module to reduce words to their base form
from keras import models  # Module for building neural network models

# Initializing the WordNet lemmatizer
lemmatizer = WordNetLemmatizer()

# Loading intents from the intents.json file
intents = json.loads(open('intents.json').read())

# Loading words and classes from pickle files
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))

# Loading the trained model from a saved file
model = models.load_model('chatbot.h5')

# Function to clean up a sentence by tokenizing and lemmatizing words
def clean_up_sentence(sentence):
    # Tokenize the sentence into words
    sentenceWords = nltk.word_tokenize(sentence)
    # Lemmatize each word to its base form
    sentenceWords = [lemmatizer.lemmatize(word) for word in sentenceWords]
    return sentenceWords

# Function to create a bag of words representation for a sentence
def bag_of_words(sentence):
    # Clean up the sentence
    sentenceWords = clean_up_sentence(sentence)
    # Initialize an empty bag of words
    bag = [0] * len(words)
    # Iterate over each word in the sentence
    for w in sentenceWords:
        # Check if the word is in the vocabulary
        for i, word in enumerate(words):
            # If the word is found, set the corresponding index in the bag to 1
            if word == w:
                bag[i] = 1
    return np.array(bag)

# Function to predict the class of a sentence using the trained model
def predict_class(sentence):
    # Create a bag of words representation for the sentence
    bag = bag_of_words(sentence)
    # Predict the probabilities of each class using the model
    res = model.predict(np.array([bag]))[0]
    # Define a threshold for considering the prediction
    errorThreshold = 0.25
    # Extract classes with probabilities above the threshold
    result = [[i, r] for i, r in enumerate(res) if r > errorThreshold]
    # Sort the classes by probability in descending order
    result.sort(key=lambda x: x[1], reverse=True)
    # Format the results as a list of dictionaries
    return_list = []
    for r in result:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

# Function to get a response based on predicted intents
def get_response(intentsList, intentsJson):
    # Extract the predicted intent from the list of intents
    tag = intentsList[0]['intent']
    # Retrieve the list of intents from the JSON data
    list_of_intents = intentsJson['intents']
    # Iterate over each intent in the list
    for i in list_of_intents:
        # Check if the intent matches the predicted tag
        if i['tags'] == tag:
            # Select a random response from the list of responses
            result = random.choice(i['responces'])
            break
    return result

# Main loop for the chatbot
print("GO bot is running")

while True:
    # Get user input
    message = input("")
    # Predict the intent of the input message
    ints = predict_class(message)
    # Get a response based on the predicted intent
    res = get_response(ints, intents)
    # Print the response
    print(res)
