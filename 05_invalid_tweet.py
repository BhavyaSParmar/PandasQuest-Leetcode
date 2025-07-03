import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    invalids = tweets[tweets['content'].str.len() > 15] 
    return invalids[['tweet_id']]