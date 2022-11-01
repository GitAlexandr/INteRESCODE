# Getting the date of birth of friends from vk using VkApi
import dotenv
import os
import numpy as np
import requests

dotenv.load_dotenv()

Token = os.environ.get("CHPOKEN")
Method = "friends.get"
Id = os.environ.get("MYID")
arr = []
url = ("https://api.vk.com/method/{METHOD}?user_id={ID}&fields=bdate&access_token={TOKEN}&v=5.131".format(
    METHOD=Method, TOKEN=Token, ID=Id))
res = requests.get(url=url)
friend = res.json()["response"]["items"]


def zapolni(arr, friend):
    for i in friend:
        try:
            friend_birth = (i["bdate"])
            if len(friend_birth) > 8:
                year = int(friend_birth[-4::])
                arr.append(year)
        except:
            pass
    return arr


arr = zapolni(arr, friend)

sort_year = np.mean(arr)
print(2022 - int(sort_year))
