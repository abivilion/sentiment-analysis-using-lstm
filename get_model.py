#!/usr/bin/env python
# coding: utf-8
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import pickle
import numpy as np

class LoadModel:
    def __init__(self, model_path, tokenizer_path):
        # load model
        self.model = load_model(model_path)
        # loading Tokenizer
        with open(tokenizer_path, 'rb') as tokenizer:
            self.tokenizer = pickle.load(tokenizer)

    def predict_sentiment(self,new_input):
        '''
        Return 0 for Negetive and 1 for Positive '''
        try:
            #vectorizing the input by the pre-fitted tokenizer instance
            new_input = self.tokenizer.texts_to_sequences(new_input)
            #padding the tweet to have exactly the same shape as `training` input
            new_input = pad_sequences(new_input, maxlen=28, dtype='int32', value=0)
            #Predicting sentiment
            sentiment = self.model.predict(new_input,batch_size=1,verbose = 2)[0]
            return (np.argmax(sentiment))
        except Exception as e:
            print(e)

if __name__ == "__main__":
    def show_output(prediction):
        if(prediction == 0):
            print("negative")
        elif (prediction == 1):
            print("positive")

    model = LoadModel(model_path='sentiment_analyser_model.h5', tokenizer_path='tokenizer.pickle')
    #positive testing
    new_input = ['so good.']
    show_output(model.predict_sentiment(new_input))
    #Negetive testing
    new_input = ['so bad.']
    show_output(model.predict_sentiment(new_input))