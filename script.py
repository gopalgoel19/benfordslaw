import requests
import os
from requests.structures import CaseInsensitiveDict
import json
import matplotlib.pyplot as plt

def connect_to_endpoint(url):
    headers = CaseInsensitiveDict()
    headers["authority"] = "twitter.com"
    headers["accept"] = "*/*"
    headers["accept-language"] = "en-US,en;q=0.9"
    headers["authorization"] = "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
    headers["cache-control"] = "no-cache"
    headers["content-type"] = "application/json"
    headers["cookie"] = 'guest_id_marketing=v1%3A164669839006955000; guest_id_ads=v1%3A164669839006955000; kdt=bJhJox5mrrrW9YL31dig3hjZzwtYxMNtt3gWz9Kh; dnt=1; lang=en; at_check=true; des_opt_in=Y; _sl=1; personalization_id="v1_+Ne/LiItHdp0/OBMp52W1A=="; guest_id=v1%3A165057133129728834; auth_token=3ca0a47281df2185e772263255960f7fb7bc068c; ct0=f22f1f6bb7d28686f7efdb86fb2291a811952d0dd277c2aee99f03f4d22a784fd6794c0915cf096eab2318805016d0e92afc00008260973afdf53539ec6f968715c4f5f14f4d187066139bbe3feff638; twid=u%3D1517233098756292608; mbox=PC#5a3221c3daf94883a14095c1b9f300e7.34_0#1713816525|session#45917ba21b024a1d8dcfe9624aca01a8#1650573585; external_referer=padhuUp37ziAYt49cfJv%2FPYan957PLwSgO%2FWRGmTwuk%3D|0|8e8t2xd8A2w%3D; att=1-NoMRunwPZngP9JGhx4XPbKnGqjGmCC8jbu16LvGU; _twitter_sess=BAh7CyIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADofbGFzdF9wYXNzd29yZF9jb25maXJtYXRpb24i%250AFTE2NTA1NzE1NzM3NDcwMDA6HnBhc3N3b3JkX2NvbmZpcm1hdGlvbl91aWQi%250AGDE1MTcyMzMwOTg3NTYyOTI2MDg6B2lkIiVmYzk3NTBkMTE3N2QwYzkwOWZh%250AYjVlOGU3MjNjZjA4ZjoPY3JlYXRlZF9hdGwrCEEm106AAToMY3NyZl9pZCIl%250AYWU5NDgxZjVhZmRjYzc4ZGM3MmNlYWIyMTRmYTMyMGU%253D--8ab3656446a514918c19348d241f02c4661b70f6'
    headers["pragma"] = "no-cache"
    headers["referer"] = "https://twitter.com/jadacryptoguy/following"
    headers["sec-fetch-dest"] = "empty"
    headers["sec-fetch-mode"] = "cors"
    headers["sec-fetch-site"] = "same-origin"
    headers["sec-gpc"] = "1"
    headers["user-agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    headers["x-csrf-token"] = "f22f1f6bb7d28686f7efdb86fb2291a811952d0dd277c2aee99f03f4d22a784fd6794c0915cf096eab2318805016d0e92afc00008260973afdf53539ec6f968715c4f5f14f4d187066139bbe3feff638"
    headers["x-twitter-active-user"] = "yes"
    headers["x-twitter-auth-type"] = "OAuth2Session"
    headers["x-twitter-client-language"] = "en"

    response = requests.get(url, headers=headers)
    print(response.status_code, url[:200])
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

def get_following_url(userid, cursor = None):    
    if cursor:
        return 'https://twitter.com/i/api/graphql/aH-mD-8F2mwJpQLegEDaWw/Following?variables={"userId":"' + userid + '","count":200,"cursor":"' + cursor + '","includePromotedContent":false,"withSuperFollowsUserFields":true,"withDownvotePerspective":false,"withReactionsMetadata":false,"withReactionsPerspective":false,"withSuperFollowsTweetFields":true,"__fs_dont_mention_me_view_api_enabled":true,"__fs_interactive_text_enabled":true,"__fs_responsive_web_uc_gql_enabled":false}'
    else:
        return 'https://twitter.com/i/api/graphql/aH-mD-8F2mwJpQLegEDaWw/Following?variables={"userId":"' + userid + '","count":200,"includePromotedContent":false,"withSuperFollowsUserFields":true,"withDownvotePerspective":false,"withReactionsMetadata":false,"withReactionsPerspective":false,"withSuperFollowsTweetFields":true,"__fs_dont_mention_me_view_api_enabled":true,"__fs_interactive_text_enabled":true,"__fs_responsive_web_uc_gql_enabled":false}'

def get_tweets_url(cursor = None):
    if cursor:
        return 'https://twitter.com/i/api/graphql/xV-_tjFDYxtd6kmroDuG7w/UserTweets?variables={"userId":"2267107398","count":40,"cursor":"' + cursor + '","includePromotedContent":true,"withQuickPromoteEligibilityTweetFields":true,"withSuperFollowsUserFields":true,"withDownvotePerspective":false,"withReactionsMetadata":false,"withReactionsPerspective":false,"withSuperFollowsTweetFields":true,"withVoice":true,"withV2Timeline":true,"__fs_responsive_web_like_by_author_enabled":false,"__fs_dont_mention_me_view_api_enabled":true,"__fs_interactive_text_enabled":true,"__fs_responsive_web_uc_gql_enabled":false,"__fs_responsive_web_edit_tweet_api_enabled":false}'
    else:
        return 'https://twitter.com/i/api/graphql/xV-_tjFDYxtd6kmroDuG7w/UserTweets?variables={"userId":"2267107398","count":40,"includePromotedContent":true,"withQuickPromoteEligibilityTweetFields":true,"withSuperFollowsUserFields":true,"withDownvotePerspective":false,"withReactionsMetadata":false,"withReactionsPerspective":false,"withSuperFollowsTweetFields":true,"withVoice":true,"withV2Timeline":true,"__fs_responsive_web_like_by_author_enabled":false,"__fs_dont_mention_me_view_api_enabled":true,"__fs_interactive_text_enabled":true,"__fs_responsive_web_uc_gql_enabled":false,"__fs_responsive_web_edit_tweet_api_enabled":false}'


def processResponse(json_response):
    instructions = json_response["data"]["user"]["result"]["timeline"]["timeline"]["instructions"]
    data = None
    stop = False
    cursor = None
    ids = []

    for i in instructions:
        if i["type"] == "TimelineAddEntries":
            data = i["entries"]
        if i["type"] == "TimelineTerminateTimeline" and i["direction"] == "Bottom":
            stop = True
    
    for item in data:
        content = item["content"]
        if "itemContent" not in content:
            if item["entryId"].startswith("cursor-bottom"):
                cursor = content["value"]
            continue
        user = content["itemContent"]["user_results"]["result"]
        if "rest_id" not in user:
            print(user)
            continue
        id = user["rest_id"]
        follower_count = user["legacy"]["followers_count"]
        name = user["legacy"]["name"]
        ids.append((str(follower_count),name,id))
    
    return (ids, cursor, stop)
    

def get_following_ids(userid):
    url = get_following_url(userid)
    json_response = connect_to_endpoint(url)
    ids_total = []
    ids, cursor, stop = processResponse(json_response) 
    ids_total += ids

    while not stop:
        url = get_following_url(userid, cursor)
        json_response = connect_to_endpoint(url)
        ids, cursor, stop = processResponse(json_response) 
        ids_total += ids
        print(len(ids), len(ids_total))

    print("Total: ", len(ids_total))
    
    return sorted(ids_total)  

def process_tweets_response(json_response):
    instructions = json_response["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"]
    data = None
    stop = False
    cursor = None
    ids = []
    f = open("ids.txt", 'a')

    for i in instructions:
        if i["type"] == "TimelineAddEntries":
            data = i["entries"]
        if i["type"] == "TimelineTerminateTimeline" and i["direction"] == "Bottom":
            stop = True
    
    for item in data:
        content = item["content"]
        if "itemContent" not in content:
            if item["entryId"].startswith("cursor-bottom"):
                cursor = content["value"]
            continue
        user = content["itemContent"]["tweet_results"]["result"]
        if "rest_id" not in user:
            print(user)
            continue
        id = user["rest_id"]
        f.write(id)
        f.write("\n")
        ids.append(id)

    f.close()
    return (ids, cursor, stop)

def get_tweets(cursor=None):
    tweet_ids = []
    stop = False
    while not stop:
        url = get_tweets_url(cursor)
        json_response = connect_to_endpoint(url)
        ids, cursor, stop = process_tweets_response(json_response)
        tweet_ids += ids
        print(len(ids), len(tweet_ids))

    print("Total: ", len(tweet_ids))

    return tweet_ids

def plot_bar_chart():
    userid = "2178012643" #balaji
    ids = get_following_ids(userid)
    print(ids, len(ids))
    counts = [0] * 9
    for fc, name, id in ids:
        ind = ord(fc[0]) - ord('1')
        counts[ind] += 1

    print(counts)

    x = [i for i in range(1,10)]
    y = counts

    plt.bar(x, y)
    plt.show()

def main():
    plot_bar_chart()

if __name__ == "__main__":
    main()
