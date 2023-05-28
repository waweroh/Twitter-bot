import tweepy
import keys



# Intitalize the twitter client
client = tweepy.Client(
    consumer_key=keys.api_key,
    consumer_secret=keys.api_key_secret,
    bearer_token = keys.bear_token,
    access_token=keys.access_token,
    access_token_secret=keys.access_token_secret
)
auth = tweepy.OAuth1UserHandler(
    access_token=keys.access_token,
    access_token_secret=keys.access_token_secret,
    consumer_key=keys.api_key,
    consumer_secret=keys.api_key_secret
)
api = tweepy.API(auth)

# Send a tweet
client.create_tweet(text="Have you a great day. Happy coding.")
def like_tweets(search_query, num_likes):
    tweets = client.search_all_tweets(query=search_query, tweet_fields="id", max_results=num_likes)
    for tweet in tweets:
        try:
            client.like(tweet.id)
            print("Liked a tweet:", tweet.text)
        except tweepy.TweepError as e:
            print("Error liking tweet:", e)

# usage: like tweets containing the hashtag "#haters"



def retweet_bot(search_query, num_retweets):
    tweets = client.search_recent_tweets(query=search_query, tweet_fields="id", max_results=num_retweets)
    for tweet in tweets.data:
        try:
            # Retweet the tweet
            client.retweet(tweet.id)
            print("Retweeted a tweet:", tweet.text)
        except tweepy.TweepError as e:
            print("Error retweeting tweet:", e)

# usage: retweet tweets containing hashtag "#Elonmusk"


def tweet_bot(message, image_path=None):
    if image_path:
        media = client.upload_media(image_path)
        response = client.create_tweet(text=message, media_ids=[media.media_key])
    else:
        response = client.create_tweet(text=message)
    tweet = response.data
    print("Tweeted successfully:", tweet.text)

# usage: tweet a message 

def get_liked_tweets(username, num_tweets):
    liked_tweets = client.get_user_liked_tweets(username=username, max_results=num_tweets)
    for tweet in liked_tweets.data:
        try:
            print("Tweet ID:", tweet.id)
            print("Text:", tweet.text)
            print("Likes:", tweet.public_metrics.like_count)
            print("Retweets:", tweet.public_metrics.retweet_count)
            print("---")
        except tweepy.errors.Forbidden as e:
            print("Forbidden error:", e)

if __name__ == "__main__":
    tweet_bot("assemble coders.")
    retweet_bot("#Elonmusk", 5)
    get_liked_tweets("wdkjkhj", 15)
    like_tweets("#haters", 20) 


