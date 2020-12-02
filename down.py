from os import path
import requests
DAY = 1
if not path.exists("input.txt"):
    print("Downloading input file...")
    with open("../cookie") as f:
        cookie = f.read()
    r = requests.get( # type: ignore
        "https://adventofcode.com/2020/day/{}/input".format(DAY),
        headers={ "Cookie": "session={}".format(cookie) }
    )
    with open("input.txt", "w") as f:
        f.write(r.text)

