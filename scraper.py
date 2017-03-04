from ConfigParser import ConfigParser

config = ConfigParser()
config.read('data/configs.ini')
cf = config.get('Scrape', 'Cat_Fle')
vf = config.get('Scrape', 'Vid_Fle')
sm = config.getboolean('Scrape', 'Sort_Min')

import urllib2
import os
from decimal import Decimal
catas = []
playlists = []
tmpList = []

def main():
    data = urllib2.urlopen("http://www.swagbucks.com/watch")
    d = data.readlines()
    start = False

    for i in d:

        if (i.find("<ul id=\"mainNavCategoriesList\" class=\"navList\">")!=-1):
            start = True
        if start:
            CatPharser(i)
        if (i.find("</ul>")<>-1):
            start = False
    with open(cf,"w") as f:
        for l in catas:
            f.write(l + '\n')

    f.close()
    print "Done Catagories"

    for c in catas:
        data = urllib2.urlopen(c)
        d = data.readlines()
        for l in d:
            if l.find("cards:[") <> -1:
                pharser(l)

    playlists.sort(key=lambda x: x[1])
    with open(vf,"w") as f:
        for l in playlists:
            f.write(l[0] + '\n')

    f.close()
    print "Done videos"

def CatPharser(datastring):
    if (datastring.find("<a href=")!=-1):
        links = datastring.find("href=")+6
        linke = datastring.find("class=")-2
        link = "http://www.swagbucks.com" + datastring[links:linke]
        link = link.replace("\/","/")
        catas.append(link)

def pharser(dataStr):
    tmpList=[]
    data = dataStr[dataStr.find("cards:")+7::]
    data = data.split("cardId")
    for d in data:
        links = d.find("link:")+7
        linke = d.find("image:")-3
        link = "http://www.swagbucks.com" + d[links:linke]
        link = link.replace("\/","/")
        #thats link worked out, time to work out sb/min ratio, smaller is better
        #size:
        if sm:
            times = d.find("durationMin:")+13
            timee = d.find("pos:")-1
            if d[times:timee] != "":
                time = Decimal(d[times:timee])
            else:
                time = -1
        else:
            times = d.find("size:")+6
            timee = d.find("durationTime:")-2
            if d[times:timee] != "":
                time = Decimal(d[times:timee])
            else:
                time = -1

        #thats time sorted, blanks will be ignored, so time set to -1 is ok as place holder
        sbs = d.find("earnLoc:")+ 9
        sbe = sbs+1
        if d[sbs:sbe] != "":
            sb = Decimal(d[sbs:sbe])
        else:
            sb = 1
        #swagbucks value sorted. now lets calulate the ratio, and put them in a place holder array
        sbRatio = Decimal(sb/time)
        if link != "http://www.swagbucks.com":
            tmpList.append((link,sbRatio))

    for x in tmpList:
        playlists.append(x)

#main()

if __name__ == '__main__':
    main()