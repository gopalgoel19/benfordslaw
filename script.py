import requests
import os
from requests.structures import CaseInsensitiveDict
import json

def connect_to_endpoint(url):
    headers = CaseInsensitiveDict()
    headers["authority"] = "twitter.com"
    headers["accept"] = "*/*"
    headers["accept-language"] = "en-US,en;q=0.9"
    headers["authorization"] = "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
    headers["content-type"] = "application/json"
    headers["cookie"] = 'guest_id_marketing=v1%3A164669839006955000; guest_id_ads=v1%3A164669839006955000; kdt=bJhJox5mrrrW9YL31dig3hjZzwtYxMNtt3gWz9Kh; dnt=1; lang=en; at_check=true; des_opt_in=Y; ads_prefs="HBISAAA="; auth_multi="2267107398:ea358fb90f14c99304a149ddac00852753045188"; auth_token=c274a2446f16c8d61dad57c023deb867d3f4fcf5; personalization_id="v1_9jLSqtshjUAHvNtxOiXxXQ=="; guest_id=v1%3A164998183114759413; twid=u%3D1476707953906536449; ct0=e45ee8be21a4cf7ef219330c409e226f73805a8e4c9cf769dbc66dab4c5993b575b07b833f32695130b92d888b16d47f729c204f91597e008fa4f9cdcf018a2ff00d3708aaaf4f6ec8d575a1d9c7f459; _twitter_sess=BAh7CCIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADofbGFzdF9wYXNzd29yZF9jb25maXJtYXRpb24i%250AFTE2NDk5ODE4NDI2ODMwMDA6HnBhc3N3b3JkX2NvbmZpcm1hdGlvbl91aWQi%250AGDE0NzY3MDc5NTM5MDY1MzY0NDk%253D--e53384759fe1544e9f88448e8673fd59bfdf2af5; mbox=PC#5a3221c3daf94883a14095c1b9f300e7.34_0#1713230769|session#13bc083cb00d4690b5be5e0570150820#1649987829'
    headers["referer"] = "https://twitter.com/akshaybd/followers"
    headers["sec-fetch-dest"] = "empty"
    headers["sec-fetch-mode"] = "cors"
    headers["sec-fetch-site"] = "same-origin"
    headers["sec-gpc"] = "1"
    headers["user-agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.79 Safari/537.36"
    headers["x-csrf-token"] = "e45ee8be21a4cf7ef219330c409e226f73805a8e4c9cf769dbc66dab4c5993b575b07b833f32695130b92d888b16d47f729c204f91597e008fa4f9cdcf018a2ff00d3708aaaf4f6ec8d575a1d9c7f459"
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
    file1 = open("myfile.txt", 'w')
    file1.write(response.text)
    file1.close()
    return response.json()

def get_following_url(userid, cursor = None):    
    if cursor:
        return 'https://twitter.com/i/api/graphql/aH-mD-8F2mwJpQLegEDaWw/Following?variables={"userId":"' + userid + '","count":200,"cursor":"' + cursor + '","includePromotedContent":false,"withSuperFollowsUserFields":true,"withDownvotePerspective":false,"withReactionsMetadata":false,"withReactionsPerspective":false,"withSuperFollowsTweetFields":true,"__fs_dont_mention_me_view_api_enabled":true,"__fs_interactive_text_enabled":true,"__fs_responsive_web_uc_gql_enabled":false}'
    else:
        return 'https://twitter.com/i/api/graphql/aH-mD-8F2mwJpQLegEDaWw/Following?variables={"userId":"' + userid + '","count":200,"includePromotedContent":false,"withSuperFollowsUserFields":true,"withDownvotePerspective":false,"withReactionsMetadata":false,"withReactionsPerspective":false,"withSuperFollowsTweetFields":true,"__fs_dont_mention_me_view_api_enabled":true,"__fs_interactive_text_enabled":true,"__fs_responsive_web_uc_gql_enabled":false}'


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
        id = user["rest_id"]
        follower_count = user["legacy"]["followers_count"]
        name = user["legacy"]["name"]
        ids.append((follower_count,name,id))
    
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


def main():
    userid = "2267107398" #gopal
    ids = get_following_ids(userid)
    print(ids, len(ids))


if __name__ == "__main__":
    main()
