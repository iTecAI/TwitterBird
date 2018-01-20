import ems
import urllib.request as url
import webbrowser as web
import os

#load up config file
cfg = open('config.txt', 'r')
cfg_lines = cfg.readlines()
cfg.close()
cfg = ''.join(cfg_lines).splitlines()



psr = ems.parser(str(url.urlopen('https://twitter.com/' + cfg[0]).read())) #twitter targeter
key_strings = cfg[1:len(cfg)] #keywords defined
elements = psr.getElementsByClass("TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
contents = []
for element in elements:
    contents.append(psr.getContent(element))

dumb_tweets = ''
for e in contents:
    for i in key_strings:
        if i in e.lower():
            dumb_tweets = dumb_tweets + '<p><b>' + i + ':</b> ' + e + '</p>'
            break

base_string = dumb_tweets
html = open('markup_temp.html', 'w')
html.write(base_string)

html.close()

web.open('file://' + os.path.realpath('markup_temp.html'))


