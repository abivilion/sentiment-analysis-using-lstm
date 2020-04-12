import re 
import tweepy

class TwitterClient(): 
	def __init__(self): 
		''' 
		Class constructor or initialization method. 
		'''
		# keys and tokens from the Twitter Dev Console 
		consumer_key = 'Ba1b8bMxYntM3g8B7boQpx9f6'
		consumer_secret = 'I8JNVAfmFaEb6iRJrCXUExe6M86BhB4mzq16qi8OMDohP4kehg'
		access_token = '774113130611736577-GDkP6QwEky1cqC05f8ZEJHp5yN9KSg5'
		access_token_secret = '9OToacpLH0xIkEuBknXyrrjaXXwdY5OIdWyqngqN7xVe2'

		# attempt authentication 
		try: 
			# create OAuthHandler object 
			self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
			# set access token and secret 
			self.auth.set_access_token(access_token, access_token_secret) 
			# create tweepy API object to fetch tweets 
			self.api = tweepy.API(self.auth) 
		except: 
			print("Error: Authentication Failed") 

	def clean_tweet(self, tweet): 
		''' 
		Utility function to clean tweet text by removing links, special characters using simple regex statements. 
		'''
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()) 
    
	def get_tweets(self, query, count = 10): 
		''' 
		Get given number of tweets for the given query
		'''
		try: 
			# call twitter api to fetch tweets 
			return self.api.search(q = query, count = count)

		except tweepy.TweepError as e: 
			# print error (if any) 
			print("Error : " + str(e)) 

if __name__ == "__main__":
	tweeter_client = TwitterClient()
	tweets = tweeter_client.get_tweets("odisha", 10)
	clean_tweets = [tweeter_client.clean_tweet(tweet.text) for tweet in tweets]
	print(clean_tweets)