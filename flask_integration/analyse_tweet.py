from textblob import TextBlob 

class TweetAnalyser:
	def analyse_tweet(self, query, count, analysing_model, tweeter_client):
		''' Help to analyse the sentimet of the query on tweter\n
		Parameters:\n
		query - The movie name\n
		count - How much tweet you want to analyse  '''
		#fetch the tweet
		fetched_tweets = tweeter_client.get_tweets(query, count)
		print("total no of fetched tweets", len(fetched_tweets))
		p_tweet = []
		n_tweet = []
		if not fetched_tweets:
			return 0
		for tweet in fetched_tweets:
			clean_tweet = tweeter_client.clean_tweet(tweet.text)
			print("Analysing : ",clean_tweet)
			# if tweet has retweets, ensure that it is appended only once 
			if clean_tweet not in p_tweet and clean_tweet not in n_tweet: 
				#analyzing sentiment
				print("before pred ",type(clean_tweet))
				sentiment = analysing_model.predict_sentiment(clean_tweet)
				if sentiment == 1:
					p_tweet.append(clean_tweet)
				elif sentiment == 0:
					n_tweet.append(clean_tweet)

		print("Total No of tweet positive", len(p_tweet))
		print("Total No of tweet negetive", len(n_tweet))
		print(p_tweet[:5])
		print("----------------")
		print(n_tweet[:5])
		if len(p_tweet):
			return 100*len(p_tweet)/(len(p_tweet)+len(n_tweet))
		return 0



if __name__ == "__main__":
	from tweet import *
	from get_model import *


	#instanciate the model
	model_path = '../model/sentiment_analyser_model.h5'
	tokenizer_path='../model/tokenizer.pickle'
	analysing_model = LoadTrainedModel(model_path, tokenizer_path)

	# new_input = 'Rasmus och jag spelade mycket fotboll ihop f rr och Efter incidenten n r han kommit hem k nde jag p eget intiat'
	# print(analysing_model.predict_sentiment(new_input))



	#Initialize tweeter clint
	tweeter_client = TwitterClient()
	analyser = TweetAnalyser()
	print(analyser.analyse_tweet("Love aaj kaal",2, analysing_model, tweeter_client))
	






