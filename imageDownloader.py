# imageDownloader.py
# Finds and downloads all images from any given URL.
# FB - 201009072

import re
import sys
import urllib2

from os.path import basename
from urlparse import urlsplit


url = sys.argv[1]
urlContent = urllib2.urlopen(url).read()
# HTML image tag: <img src="url" alt="some_text"/>
imgUrls = re.findall('img .*?src="(.*?)"', urlContent)

# download all images
for imgUrl in imgUrls:
    try:
        imgData = urllib2.urlopen(imgUrl).read()
        fileName = basename(urlsplit(imgUrl)[2])
        print fileName
        output = open(fileName,'wb')
        output.write(imgData)
        output.close()
    except:
        pass
