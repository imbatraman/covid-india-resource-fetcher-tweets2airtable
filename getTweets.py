import requests
import os

BEARER_TOKEN = '<YOUR TWITTER API BEARAER TOKEN>'

original_tweet_list = []

def auth():
    return os.environ.get("BEARER_TOKEN")


def create_url(query):
    # query = "from:twitterdev -is:retweet"
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    tweet_fields = "tweet.fields=text,author_id,public_metrics,created_at,referenced_tweets"
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(
        query, tweet_fields
    )
    return url


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(BEARER_TOKEN)}
    return headers


def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def getRelatedTweets():
    city = 'delhi'
    status = 'verified'
    category = 'oxygen'
    availability = 'available'
    lookup_query = f"{city} {status} {category} {availability}"
    url = create_url(lookup_query)
    headers = create_headers(BEARER_TOKEN)
    json_response = connect_to_endpoint(url, headers)
    tweets_data = json_response['data']
    # print(json.dumps(json_response, indent=4, sort_keys=True))
    return tweets_data

def lookupOriginalTweet(id, headers):
    url = f"https://api.twitter.com/2/tweets/{id}?expansions=referenced_tweets.id"
    headers = create_headers(BEARER_TOKEN)
    response = requests.request("GET", url, headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def getOriginalTweetTextList():
    global original_tweet_list
    twe = getRelatedTweets()
    for _ in twe:
        try:
            retweet_count = _['public_metrics']['retweet_count']
            if retweet_count > 5:
                referenced_tweet = _['referenced_tweets'][0]
                tweet_type = referenced_tweet['type']
                if tweet_type.lower() == 'retweeted':
                    original_tweet_id = referenced_tweet['id']
                    original_tweet_id_text = lookupOriginalTweet(original_tweet_id, BEARER_TOKEN)
                    original_tweet_text = original_tweet_id_text['data']['text']
                    original_tweet_dict = {
                        'text': original_tweet_text,
                        'retweets': retweet_count
                    }
                    original_tweet_list.append(original_tweet_dict)
        except KeyError as keyError:
            print(keyError)
    return original_tweet_list

