import requests
import json

API_ENDPOINT = 'https://discord.com/api/v8'
CLIENT_ID = '928291582896136233'
CLIENT_SECRET = 'iNSLfHtW2pr9Dai6LMfxy4eREbOZuA85'
REDIRECT_URI = 'https://nitlix.github.io/link-discord'

def exchange_code(code):
  data = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'grant_type': 'authorization_code',
    'code': code,
    'redirect_uri': REDIRECT_URI
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  r = requests.post('%s/oauth2/token' % API_ENDPOINT, data=data, headers=headers)
  r.raise_for_status()
  return r.json()


def what(tokentype,token,what):
    headers = {
        'authorization': f'{tokentype} {token}'
    }
    r = requests.get(f'https://discord.com/api/users/@me{what}', headers=headers)
    return r.json()


def refresh_token(e,refresh_token):
  data = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'grant_type': 'refresh_token',
    'refresh_token': refresh_token
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  r = requests.post('%s/oauth2/token' % API_ENDPOINT, data=data, headers=headers)
  r.raise_for_status()
  return r.json()


  

quick = exchange_code("EOPwk7nXufrza753W65EpDTIJVFzwy")





with open(f'main.json', 'w+') as o:
    o.seek(0)
    json.dump(what(quick['token_type'],quick['access_token'],''), o, indent=4)
    o.truncate()

with open(f'connections.json', 'w+') as o:
    o.seek(0)
    json.dump(what(quick['token_type'],quick['access_token'],'/connections'), o, indent=4)
    o.truncate()

with open(f'guilds.json', 'w+') as o:
    o.seek(0)
    json.dump(what(quick['token_type'],quick['access_token'],'/guilds'), o, indent=4)
    o.truncate()



