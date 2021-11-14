from mee6_py_api.api import API
import asyncio
import time
import requests
from pprint import pprint
import configparser
config = configparser.RawConfigParser()
config.read('config.txt')

settings = dict(config.items('CONFIG'))\

guild_id = settings['guild_id']
user_id = settings['user_id']
url = settings['url']

class TestClass: # I have a class here because that's what the example code had for the API and I'm too lazy to change it.
    def __init__(self):
        self.mee6API = API(guild_id)

    async def test_get_leaderboard_page(self): #Gets all the data from the first page of the leaderboard.
        leaderboard_page = await self.mee6API.levels.get_leaderboard_page(0)
        return leaderboard_page
    
    def test_has_passed_userXP(self):
        f = open("rank.txt", "r") # Check what rank you currently are. Saved in rank.txt
        my_rank = int(f.read())
        f.close()
        leaderboard = asyncio.run(testClass.test_get_leaderboard_page())
        for i in range(0,100): # Check the first 100 people to see if they match with var user_id
            time.sleep(1)
            print(leaderboard["players"][i]["id"])
            if leaderboard["players"][i]["id"] == str(user_id): # Check if user_id matches. API stores info in nested dicts & lists
                if my_rank < i: 

                    # Webhook stuff
                    data = { 
                        "content" : f"<@{user_id}>, you have been passed! You are now in rank {i + 1}."
                    }

                    result = requests.post(url, json=data)
                    
                    # Check for errors
                    if 200 <= result.status_code < 300:
                        print(f"Webhook sent {result.status_code}")
                    else:
                        print(f"Not sent with {result.status_code}, response:\n{result.json()}")
                
                # Save the new rank in rank.txt
                w = open("rank.txt", "w")
                w.write(str(i))
                w.close()
                break

testClass = TestClass()
while True: # Keep program running
    testClass.test_has_passed_userXP()
    time.sleep(60) # You can only earn xp every minute with Mee6, no use in checking more often