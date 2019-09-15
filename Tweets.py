import GetOldTweets3 as got

def get_tweets(key_words, date, max_tweets=10, previous_days=1, next_days=1):
    
    tweets = []
    lower_bound_date = str(date - datetime.timedelta(days=N_days_before))
    upper_bound_date = str(date + datetime.timedelta(days=N_days_next))
    
    for key_word in key_words:
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch(key_word)\
                                           .setSince(lower_bound_date)\
                                           .setUntil(upper_bound_date)\
                                           .setMaxTweets(max_tweets)
        tweet = got.manager.TweetManager.getTweets(tweetCriteria)
        tweets = tweet + tweets
    return tweets