from json import loads

with open('config/config.json', 'r') as f:
    config_json_data = loads(f.read())

def generateTweet():
    tweet_content = input('Digite o Tweet: ')
    
    print('Escolha a conta:')
    for user in config_json_data:
        print(f'{user} - {config_json_data[str(user)]["name"]}')
    user = input()


    tweet_json = f'{{"{int(sorted(config_json_data.keys())[-1])+1}": {{"content": "{tweet_content}", "user": "{user}"}} }}'
    return tweet_json

def saveTweet(tweet_json):
    pass

my_tweet = generateTweet()
print(my_tweet)