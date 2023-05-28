# Twitter-bot
This is a twitter bot repository that allows users to perform various actions on twitter using this bot through the twitter API.
The project uses tweepy library to connect to the Twitter API using python.
The bot has the following functions:
<ol>
1.  The tweet_bot function takes a message as input and optionally an image path. If an image path is provided, the code uploads the image and includes it in the tweet using the upload_media method. Finally, it creates a tweet using the create_tweet method and prints a success message with the tweet text
2.    The retweet_bot function takes two parameters: search_query and num_retweets. It uses the Cursor object to search for tweets based on the given search query and retrieves the specified number of tweets. It then iterates over the retrieved tweets and attempts to retweet each tweet using the retweet method of the API object.
3.  The like_tweets function takes two parameters: search_query (the query string to search for tweets) and num_likes (the number of tweets to like). It uses the search_recent_tweets method of the Client instance to search for recent tweets matching the query. It then iterates over the retrieved tweets and attempts to like each tweet using the like method 
4.  The get_liked_tweets function takes in the username and number of likes parameters. It then iterates over the userid to retrieve the number of liked tweets requested for.
</ol>