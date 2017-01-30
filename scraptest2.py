import urllib
import re

urls = ["http://google.com","http://nytimes.com","http://cnn.com"]

i=0

regex = '<title>(.+?)</title>'
pattern = re.compile(regex)


while i<len(urls):

	htmlfile = urllib.urlopen(urls[i])
	htmltext = htmlfile.read()
	title = re.findall(pattern,htmltext)
# 	open("testfile","wb").write(htmltext)
	
	
	print title
	i+=1
	