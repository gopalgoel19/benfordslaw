import requests

cookies = {
    'guest_id_marketing': 'v1%3A164669839006955000',
    'guest_id_ads': 'v1%3A164669839006955000',
    'kdt': 'bJhJox5mrrrW9YL31dig3hjZzwtYxMNtt3gWz9Kh',
    'dnt': '1',
    'lang': 'en',
    'at_check': 'true',
    'des_opt_in': 'Y',
    'mbox': 'PC#5a3221c3daf94883a14095c1b9f300e7.34_0#1713230769|session#13bc083cb00d4690b5be5e0570150820#1649987829',
    'auth_multi': '"1476707953906536449:c274a2446f16c8d61dad57c023deb867d3f4fcf5"',
    'auth_token': 'ea358fb90f14c99304a149ddac00852753045188',
    'personalization_id': '"v1_Vj89x0kEsh2Bp8UUYxmqOw=="',
    'guest_id': 'v1%3A165000342614063352',
    'twid': 'u%3D2267107398',
    'ct0': '68884df20fa488178f60ef241102ad985ea1147f1467a057bd9d1444acc1f5fd9f93811dbb5198225f511faa286b16ca4abea5df30026c29a2fcff537fe95182b3af3b63cc9720733982967d8492f7ae',
    '_twitter_sess': 'BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCA0EZzOAAToMY3NyZl9p%250AZCIlZDYyMDU4N2EwY2I3NzVhM2I2MzllMzdjMjJmMzE1YTQ6B2lkIiVjMTk1%250AN2JkMGNiMWQ0Njg4NWE3M2UyZTg3Y2Y1MWVlMQ%253D%253D--c9a2cb6231a21048d79d472ea547efb3e13085eb',
    'external_referer': 'padhuUp37ziB1mb6tX%2Bb05GcyPv53d7c|0|8e8t2xd8A2w%3D',
}

headers = {
    'authority': 'twitter.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'cache-control': 'no-cache',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'guest_id_marketing=v1%3A164669839006955000; guest_id_ads=v1%3A164669839006955000; kdt=bJhJox5mrrrW9YL31dig3hjZzwtYxMNtt3gWz9Kh; dnt=1; lang=en; at_check=true; des_opt_in=Y; mbox=PC#5a3221c3daf94883a14095c1b9f300e7.34_0#1713230769|session#13bc083cb00d4690b5be5e0570150820#1649987829; auth_multi="1476707953906536449:c274a2446f16c8d61dad57c023deb867d3f4fcf5"; auth_token=ea358fb90f14c99304a149ddac00852753045188; personalization_id="v1_Vj89x0kEsh2Bp8UUYxmqOw=="; guest_id=v1%3A165000342614063352; twid=u%3D2267107398; ct0=68884df20fa488178f60ef241102ad985ea1147f1467a057bd9d1444acc1f5fd9f93811dbb5198225f511faa286b16ca4abea5df30026c29a2fcff537fe95182b3af3b63cc9720733982967d8492f7ae; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCA0EZzOAAToMY3NyZl9p%250AZCIlZDYyMDU4N2EwY2I3NzVhM2I2MzllMzdjMjJmMzE1YTQ6B2lkIiVjMTk1%250AN2JkMGNiMWQ0Njg4NWE3M2UyZTg3Y2Y1MWVlMQ%253D%253D--c9a2cb6231a21048d79d472ea547efb3e13085eb; external_referer=padhuUp37ziB1mb6tX%2Bb05GcyPv53d7c|0|8e8t2xd8A2w%3D',
    'origin': 'https://twitter.com',
    'pragma': 'no-cache',
    'referer': 'https://twitter.com/gopalgoel19',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'x-csrf-token': '68884df20fa488178f60ef241102ad985ea1147f1467a057bd9d1444acc1f5fd9f93811dbb5198225f511faa286b16ca4abea5df30026c29a2fcff537fe95182b3af3b63cc9720733982967d8492f7ae',
    'x-twitter-active-user': 'yes',
    'x-twitter-auth-type': 'OAuth2Session',
    'x-twitter-client-language': 'en',
}

json_data = {
    'variables': '{"tweet_id":"1402269946353262602","dark_request":false}',
    'queryId': 'VaenaVgh5q5ih7kvyVjgtg',
}

response = requests.post('https://twitter.com/i/api/graphql/VaenaVgh5q5ih7kvyVjgtg/DeleteTweet', headers=headers, cookies=cookies, json=json_data)
print(response.json())