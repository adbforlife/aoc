import sys
day = int(sys.argv[1])
session_val = '53616c7465645f5fc18e89d455e11f41b1cce093f54d8b19a8dbccacf607f52db59de12feebe575ac3f256d54e6e90e3a495545ead98d9eee613b4867b1ea4ae'
cookies = dict(session=session_val)
url = f'https://adventofcode.com/2022/day/{day}/input'
import requests
r = requests.get(url, cookies=cookies)
print(r.text)
