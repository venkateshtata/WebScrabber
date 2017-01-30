import urllib

htmlfile = urllib.urlopen("http://www.google.com")
htmltext = htmlfile.read()

print htmltext