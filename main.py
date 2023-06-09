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





def like_tweets(search_query, num_likes):
    tweets = client.search_all_tweets(query=search_query, tweet_fields="id", max_results=num_likes)
    for tweet in tweets:
        try:
            client.like(tweet.id)
            print("Liked a tweet:", tweet.text)
        except tweepy.TweepError as e:
            print("Error liking tweet:", e)

# usage: like tweets containing the hashtag "#haters"

#like tweet

def like_tweet(tweet_id):
    try:
        client.like(tweet_id)
        print("Liked a tweet:", tweet_id)

    except Exception as e:
        print("Error liking tweet:", e)
like_tweet(1664226636680552449)


def retweet_bot(search_query, num_retweets):
    tweets = client.search_recent_tweets(query=search_query, tweet_fields="id", max_results=num_retweets)
    for tweet in tweets.data:
        try:
            # Retweet the tweet
            client.retweet(tweet.id)
            print("Retweeted a tweet:", tweet['text'])
        except tweepy.TweepError as e:
            print("Error retweeting tweet:", e)
retweet_bot("#Elonmusk", 5)

# usage: retweet tweets containing hashtag "#Elonmusk"


def tweet_bot(message, image_path=None):
    if image_path:
        media = client.upload_media(image_path)
        response = client.create_tweet(text=message, media_ids=[media.media_key])
    else:
        response = client.create_tweet(text=message)
    tweet = response.data
    print("Tweeted successfully:", tweet['text'])

# tweet_bot("Happy Sato")   

# usage: tweet a message 

#Edit a tweet
def block_user(target_user_id ):
    # block = client.block(blocked = target_user_id)
    # for user in block.data:
    try:
        client.block(target_user_id)
        print ("Successfully blocked:", target_user_id)

    except tweepy.TweepyError as error:
        print("Error blocking user:", error)
block_user(1293130256505884672)



def delete_tweet(tweet_id):
    try:
        client.delete_tweet(tweet_id)
        print("Tweet deleted successfully:", tweet_id)
    except tweepy.TweepyError as e:
        print("Error deleting tweet:", e)

# delete a specific tweet
delete_tweet(1664895447348187137)

def get_liked_tweets(username, num_tweets):
    liked_tweets = client.get_liked_tweets(username=username, max_results=num_tweets)
    for tweet in liked_tweets.data:
        try:
            print("Tweet ID:", tweet.id)
            print("Text:", tweet.text)
            print("Likes:", tweet.public_metrics.like_count)
            print("Retweets:", tweet.public_metrics.retweet_count)
            print("---")
        except tweepy.errors.Forbidden as e:
            print("Forbidden error:", e)
get_liked_tweets("wdkjkhj", 15)


#retweets bot function
class MyStream(tweepy.StreamingClient):
    # a method
    def upon_tweet(self, tweet):
        print("Tweet:", tweet.text)
        try:
            client.retweet(tweet.id)
        except Exception as error:
            print(error)

#instance of stream object.
stream = MyStream(bearer_token = keys.bear_token)

#rules to find especific tweets
rule = tweepy.StreamRule("(#python OR #coding) (-is:retweet -is :reply)")
stream.add_rules(rule)
stream.filter()

#Edit tweet




if __name__ == "__main__":
    #tweet_bot("assemble coders.")
    retweet_bot("#Elonmusk", 5)
    get_liked_tweets("wdkjkhj", 15)
    like_tweets("#haters", 20) 


