import requests
import datetime
import json
start_time = datetime.datetime.now()



e = requests.get('https://ftx.com/api/markets/BTC/USD/orderbook')

print(e.json())


end_time = datetime.datetime.now()
time_diff = (end_time - start_time)
execution_time = time_diff.total_seconds() * 1000

print("It took " + str(round(execution_time)) + "ms")