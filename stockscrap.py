import urllib
import re

# symbolslist = ["aapl","spy","goog","nflx"]


# i=o
# 
# while i<len(symbolslist):

	# url = "https://www.olx.in/bangalore/mobile-phones/?search%5Bphotos%5D=false"
htmlfile = urllib.urlopen("http://www.olx.in/bangalore/mobile-phones/?search%5bphotos%5d=false")
htmltext = htmlfile.read()
regex = '<img class="fleft" src=(.+?) alt=(.+?)>'
pattern = re.compile(regex)
title = re.findall(pattern,htmltext)
print title
	# i+=1

