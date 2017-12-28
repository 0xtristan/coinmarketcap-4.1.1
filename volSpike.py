from coinmarketcap import Market
import json
import collections
import time

coinmarketcap = Market()
#stats = coinmarketcap.ticker()
#print(json.dumps(stats, indent=4))
volVals = {}
iteration = 0
numCoins = 5
while(1):
    stats = coinmarketcap.ticker()
    for coin in stats:
        #print(coin)
        if(int(coin["rank"]) > numCoins):
            break

        #print(json.dumps(coin, indent=4))
        vol = float(coin["24h_volume_usd"])
        if(iteration>numCoins):
            diff = vol/volVals[str(coin["symbol"])]


            if(diff > 1.2):
                movers[mcVolRatio] = [coin["symbol"],str(coin["percent_change_24h"])]
                print("VOL SPIKE: "+coin["symbol"]+" "+diff)

        print(coin["symbol"]+" "+str(vol))
        volVals[str(coin["symbol"])] = vol
        iteration = iteration + 1
    if(iteration>numCoins):
        time.sleep(10)
    print()
    print()
