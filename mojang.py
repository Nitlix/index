import requests
import time
import datetime
import json


headers ={"Authorization":['item_sold_minecraft']}

Authorization: Bearer [JWT/auth token here]

request = requests.get('https://api.minecraftservices.com/rollout/v1/msamigration')

print(request.text)