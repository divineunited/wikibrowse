### This application mimics a random browsing through wikipedia pages that a user might do. The function starts by accepting a wikipedia URL and an integer for the amount of jumps that the program will randomly jump. It will jump from one wikipedia page to another depending on the number of jumps given.

import re
import urllib.request
import random
import webbrowser


def wikibrowse(url, jumps):
    '''Accepts a wikipedia URL and an integer for the amount of jumps that the program will randomly jump. It will jump from one wikipedia page to another depending on the number of jumps given.'''
    webbrowser.open_new_tab(url)

    while jumps > 0:

        web_page = urllib.request.urlopen(url)
        contents = web_page.read() .decode(errors="replace")
        web_page.close()

        body = re.findall('(?<=<body).+?(?=</body>)', contents, re.DOTALL)
        links = re.findall('(?<=href=").+?(?=")', body[0], re.DOTALL)

        wikilinks = ['https://en.wikipedia.org' + link for link in links if ('.org' not in link) and ('wiki' in link)]

        print('\nJumping from ' + url)

        jumps -= 1
        url = random.choice(wikilinks)

        print('To ' + url)
        webbrowser.open_new_tab(url)


def checkUrl(url):
    '''This checks to see if a website exists or not. Returns True or False'''
    try:
        request = urllib.request.Request(url)
        request.get_method = lambda: 'HEAD'
        urllib.request.urlopen(request)
        return True
    except:
        return False


#main:

while True:
    url = str(input('\nPlease enter a wikipedia website: (or type STOP) '))
    if url.upper() == 'STOP':
        break
    jumps = eval(input('Please enter the number of random hops from that page: '))

    #checking to make sure it is a valid wikipedia url and the jumps entered is an integer:
    if (('wikipedia.org' in url) and checkUrl(url) and isinstance(jumps, int)):
        wikibrowse(url, jumps)
    else:
        print('Invalid entry.') 