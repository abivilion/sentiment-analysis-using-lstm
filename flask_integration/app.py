from flask import Flask, render_template, flash, request
from analyse_tweet import TweetAnalyser
from tweet import TwitterClient
from get_model import LoadTrainedModel
from keras.backend import clear_session




# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

#Define home route
@app.route("/")
def index():
    return render_template("index.html")

#Define diagnosis route
@app.route("/analyse", methods=['POST'])
def diagnosis():
    #instanciate the model
    analysing_model_path = '../models/sentiment_model.sav'
    tokenizer_path='../model/tokenizer.pickle'
    analysing_model = LoadTrainedModel(analysing_model_path, tokenizer_path)
    #Initialize tweeter clint
    tweeter_client = TwitterClient()
    #instantiate tweet analyser
    analyser = TweetAnalyser()

    name = request.form['name']
    print("name", name)
    prediction = analyser.analyse_tweet(name, 50, analysing_model, tweeter_client)
    # prediction = analysing_model.predict_sentiment("So good")
    clear_session()
    #Predict on the given parameters
    print(prediction)
    return render_template("index.html", result=name, prediction=prediction)
        
if __name__ == "__main__":
    app.run()