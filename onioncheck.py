# -*- coding: utf-8 -*-
# This script will check if the .onion is up.
# If the .onion is up it will be written to websites.txt with url + title.
# For example: 
# $ cat websites.txt 
# http://swehackmzys2gpmb.onion/swehack - Ett svenskt diskussionsforum om IT-säkerhet - Index

import requests

# Tor settings
# Tor standard port is 9050
proxies = {
        'http': 'socks5://localhost:9050',
        'https': 'socks5://localhost:9050'
        }
# Send valid tor user agent, just in case.
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0'
        }
      
# Connect to .onion
print "[+] Starting"
def crawl():
    print "[+] Opening urls.txt"
    with open('urls.txt') as fn:
        for line in fn:
            url = line.strip('\n')
            print "[+] Connecting to %s \n" % url
            try:
                rStatus = requests.get(url, headers=headers, proxies=proxies).status_code
                print rStatus
                if rStatus == 200:
                    rTitle = requests.get(url, headers=headers, proxies=proxies)
                    title = rTitle.text
                    if '<TITLE>' in rTitle.text:
                        title = title.split('<TITLE>')[1]
                        title = title.split('</TITLE>')[0]
                        title = title.strip()
                        title = title.encode('UTF-8')
                    elif '<title>' in rTitle.text:
                        title = title.split('<title>')[1]
                        title = title.split('</title>')[0]
                        title = title.strip()
                        title = title.encode('UTF-8')
                    else:
                        print "[+] Did not find title element"
                    print title
                    if title in open('websites.txt').read():
                        print "[+] Already in the document."
                    else:
                        print "[+] Saving"
                        with open('websites.txt', 'a') as f:
                            f.write(url + title + '\n')
                        print '[+] Saved URL'
            except:
                print "[-] Could not find %s" % url

crawl()
