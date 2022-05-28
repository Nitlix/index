main = {"hi":{"apple": 124,"orange":2155}}

for x,y in main.items():
    print(y)
    y['apple'] = 128

print(main)