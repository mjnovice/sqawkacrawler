import requests
from BeautifulSoup import BeautifulSoup
from time import sleep

l=['iker-casillas','lionel-messi','xabi-alonso','mats-hummels']#List of Players!

def crawl(url):
    while True:
	try:
	    r=requests.get(url)
	    return r.content
	    break
	except Exception as e:
	    print e
	    sleep(2)
	    print "Retrying!!"

base_url = 'http://www.squawka.com/players/'

def urlify(player,base_url):
    return base_url+player+'/stats'

for i in xrange(len(l)):
    player=l[i]
    print "Fetching information for %s"%player
    print "waiting..."
    sleep(4)
    html = crawl(urlify(player,base_url))
    parsed_html = BeautifulSoup(html)
    print ""
    print ""
    print "Stats for player: %s"%player
    for i in xrange(1,13):
	value = parsed_html.body.find(id='stat-'+str(i)).find('span',attrs={'class':'stat'}).text
	heading = parsed_html.body.find(id='stat-'+str(i)).find('span',attrs={'class':'heading'}).text
	print heading+' '+value
    print ""
    print ""