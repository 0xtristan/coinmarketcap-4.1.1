from coinmarketcap import Market
import json
import collections

coinmarketcap = Market()
stats = coinmarketcap.ticker()
#print(json.dumps(stats, indent=4))
movers = {}
for coin in stats:
    #print(coin)
    if(int(coin["rank"]) > 200):
        break

    #print(json.dumps(coin, indent=4))
    mcVolRatio = float(coin["24h_volume_usd"])/float(coin["market_cap_usd"])
    if(mcVolRatio > 0.05):
        print(coin["symbol"]+": " + str(mcVolRatio)+"\t"+str(coin["percent_change_24h"])+"%")
        movers[mcVolRatio] = [coin["symbol"],str(coin["percent_change_24h"])]

sortedBymcVol = collections.OrderedDict(reversed(sorted(movers.items())))
print()
print("Sorted by ratio:")

for k,v in sortedBymcVol.items():
    print(v[0]+": "+str(k)+"\t"+v[1]+"%")
