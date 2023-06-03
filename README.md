# Twitter-bot
This is a twitter bot repository that allows users to perform various actions on twitter using this bot through the twitter API.
The project uses tweepy library to connect to the Twitter API using python.
The bot has the following functions:


## Twitting function
The given code defines a function called tweet_bot that allows you to post a tweet with a message and an image. Here's a breakdown of the code:

- The tweet_bot function takes two parameters: message, which is the content of the tweet, and image_path, which is the file path of an optional image to be attached to the tweet.

- The code checks if image_path is provided and attaches it to the tweet.


- The code then uses the client.create_tweet() method to create a tweet with the provided message text. If an image is attached, the media_ids parameter is set to the media key of the uploaded image.

- The create_tweet() method returns a Tweet object, which is stored in the response variable.

- Finally, the code prints a success message indicating that the tweet was posted successfully, along with the text of the tweeted message.


## Deleting Tweets function

The given code defines a function called delete_tweet that takes a tweet_id as input and attempts to delete the tweet with that ID using the client.delete_tweet() method. The code does the following.

- The delete_tweet function is defined with a single parameter tweet_id, which represents the ID of the tweet to be deleted.

- Inside the function, there is a try block that contains the code to delete the tweet using client.delete_tweet(tweet_id).

- If the deletion is successful and no exception is raised, the code prints a success message indicating that the tweet was deleted successfully, along with the tweet_id.

- If an exception occurs during the deletion process, it is caught in the except block, and the code prints an error message indicating that there was an error deleting the tweet, along with the specific exception message e.

- Outside the function, the delete_tweet function is called with a specific tweet_id (1664895447348187137) to demonstrate the usage. This will attempt to delete the tweet with the given ID.

By running this code, you can delete a specific tweet by providing its ID as an argument to the delete_tweet function. If the tweet is successfully deleted, a success message will be printed. Otherwise, an error message will be printed along with the specific exception message.

## Other functions. Due to twitter deprecating API v1.1 this functions do not contact the Twitter API
- The retweet_bot function takes two parameters: search_query and num_retweets. It uses the Cursor object to search for tweets based on the given search query and retrieves the specified number of tweets. It then iterates over the retrieved tweets and attempts to retweet each tweet using the retweet method of the API object.


- The like_tweets function takes two parameters: search_query (the query string to search for tweets) and num_likes (the number of tweets to like). It uses the search_recent_tweets method of the Client instance to search for recent tweets matching the query. It then iterates over the retrieved tweets and attempts to like each tweet using the like method 


- The get_liked_tweets function takes in the username and number of likes parameters. It then iterates over the userid to retrieve the number of liked tweets requested for.







