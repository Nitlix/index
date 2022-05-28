import pip
import requests
def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])


try:
    import mouse
except Exception:
    install("mouse")
    import mouse

import time
import datetime

print("hi")

while True:
    actions = list(requests.get('https://api.nitlix.pro/api/v1/remote-manager/check-actions?id=' + 'x').json()['resp'])
    for x in actions:
        try:
            if x['name'] == "mouse":
                try:
                    print('moved' + str(int(x['data']['x'])) +" " + str(int(x['data']['y'])))
                    mouse.move(int(x['data']['x']),int(x['data']['y']))
                except Exception:
                    pass
        except Exception:
            pass
    time.sleep(1)