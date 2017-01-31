import urllib
import re

# symbolslist = ["aapl","spy","goog","nflx"]


# i=o
# 
# while i<len(symbolslist):

	# url = "https://www.olx.in/bangalore/mobile-phones/?search%5Bphotos%5D=false"
htmlfile = urllib.urlopen("http://www.olx.in/bangalore/mobile-phones/?search%5bphotos%5d=false")
htmltext = htmlfile.read()
regex = '<span>(.+?)</span>'
pattern = re.compile(regex)
title = re.findall(pattern,htmltext)
f = open('testfile.txt', 'w')
f.write(htmltext)
f.close
print title
	# i+=1

