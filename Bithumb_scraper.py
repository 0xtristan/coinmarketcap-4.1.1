# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import matplotlib.pyplot as plt
import numpy as np
import time
import datetime

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

plt.ion() ## Note this correction
fig=plt.figure()
#plt.axis([0,20,0,60000000])

i=0
x=list()
y=list()
colours = {'Bitcoin Cash':['b','o'],
            'Bitcoin':['g','o'],
            'Ethereum':['r','o'],
            'Dash':['c','o'],
            'Ethereum Classic':['m','o'],
            'Ripple':['y','o'],
            'Qtum':['k','o'],
            'Litecoin':['b','^'],
            'Monero':['g','^'],
            'Zcash':['r','^']}

#plt.show()
#time.sleep(10)

while True:

    #url = input('Enter url: ')
    url = 'https://coinmarketcap.com/exchanges/bithumb/#USD'
    try:
        html = urllib.request.urlopen(url, context=ctx).read()
    except:
        continue
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup.findAll('tr')
    vol=list()
    names=list()
    v=()

    for tag in tags[1:11]: # need to ignore 'volume' table header
        nameTag = tag.contents[3].string
        volumeTag = tag.span.string
        #print(type(volumeTag))
        #print(nameTag)
        volume = volumeTag.strip()[1:]
        volume = int(volume.replace(',', ''))
        v = (nameTag,volume) #make this a tuple instead
        vol.append(v)
        names.append(nameTag)
        #print(volume)

    #print(vol)
    #print()
    #x.append(i)
    #y.append(vol)
    j=0
    for data in vol:
        #plt.scatter(i,data[1],c=colours[data[0]],s=4) # need to assign specific colours to cryptos
        plt.scatter(i,data[1],c=colours[data[0]][0],marker=colours[data[0]][1],s=4)
        j+=1
    plt.autoscale(enable=True, axis='both', tight=False)
    plt.legend(names,loc='upper left',fontsize=5)
    i+=2;
    plt.show()
    plt.pause(120) #Note this correction
    #time.sleep(5)
