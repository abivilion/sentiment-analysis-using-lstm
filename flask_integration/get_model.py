#!/usr/bin/env python
# coding: utf-8
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import pickle
import numpy as np

class LoadTrainedModel:
    def __init__(self, model_path, tokenizer_path):
        # load model
        self.analysing_model = pickle.load(open(model_path, 'rb'))
        # loading Tokenizer
        with open(tokenizer_path, 'rb') as dummy_tokenizer:
            self.tokenizer = pickle.load(dummy_tokenizer)

    def predict_sentiment(self,new_input):
        '''
        Return 0 for Negetive and 1 for Positive '''
        try:
            new_input = [new_input]
            #vectorizing the input by the pre-fitted tokenizer instance
            new_input = self.tokenizer.texts_to_sequences(new_input)
            #padding the tweet to have exactly the same shape as `training` input
            new_input = pad_sequences(new_input, maxlen=28, dtype='int32', value=0)
            print(self.analysing_model)
            #Predicting sentiment
            sentiment = self.analysing_model.predict(new_input)[0]
            return (np.argmax(sentiment))
        except Exception as e:
            print("Error in model", e)

if __name__ == "__main__":
    def show_output(prediction):
        if(prediction == 0):
            print("negative")
        elif (prediction == 1):
            print("positive")

    analysing_model = LoadTrainedModel(model_path='../model/sentiment_analyser_model.h5', tokenizer_path='../model/tokenizer.pickle')
    #positive testing
    new_input = 'so good.'
    show_output(analysing_model.predict_sentiment(new_input))
    #Negetive testing
    new_input = 'Rasmus och jag spelade mycket fotboll ihop f rr och Efter incidenten n r han kommit hem k nde jag p eget intiat'
    show_output(analysing_model.predict_sentiment(new_input))