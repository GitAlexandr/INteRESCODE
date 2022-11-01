import requests
import json

url = "https://music.yandex.ru/handlers/main.jsx?what=chart&lang=ru&external-domain=music.yandex.ru&overembed=false&ncrnd=0.6530313336708948"

res = requests.get(url)
for i in range(100):
    music_position = res.json()["chartPositions"][i]["chartPosition"]["position"]
    music_name = res.json()["chartPositions"][i]["track"]["title"]
    music_artist = res.json()["chartPositions"][i]["track"]["artists"]
    arr = []
    for g in music_artist:
        gg = g["name"]
        arr.append(gg)
    hh = " ".join(arr)
    with open("links.txt", "a") as f:
            f.write(str(music_position))
            f.write(" ")
            f.write(music_name)
            f.write(" ")
            f.write(hh)
            f.write("\n")
