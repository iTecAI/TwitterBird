import pyquery as pq
class parser(): #much like how one would do it in HTMLParser, but easier.
    def __init__(self, html): #init parser class
        self.html = html

    #list all elements with class
    def getElementsByClass(self, eclass):
        si = pq.allIndex(self.html, 'class="' + eclass + '"') #find indexes of all classes of type eclass
        elements = [] #init list elements
        for c in si: #begin handling element indexes
            start = self.html.rfind('<', 0, c) #find beginning of tag
            etype = ''
            i = start + 1
            while self.html[i] != ' ': #find tag type
                etype = etype + self.html[i]
                i += 1
            end = self.html.find('</' + etype + '>', c) + 2 + len(etype) #find end of element
            elements.append(self.html[start:end + 1]) #add element to list
        return elements

    #get element with ID
    def getElementById(self, eid):
        pass

    #list elements of a type
    def getElementsByType(self, etype):
        pass

    #get content of an <p>, <h1>, <title>, etc.
    def getContent(self, estring):
        etype = '' #get tag type
        i = 1
        while self.html[i] != ' ': #find tag type
            etype = etype + estring[i]
            i += 1
        cbegin = estring.find('>') #find content start
        cend = estring.find('</' + etype + '>') #find content end
        content = estring[cbegin + 1:cend - 3] #get content
        return content

    #get attrs of an element
    def getAttrs(self, estring):
        pass

#test
"""psr = parser(url.urlopen('https://twitter.com/realDonaldTrump').read())
#psr = parser('<p class="js-tweet-text-container">hi</p>')
elements = psr.getElementsByClass("TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
print elements
for element in elements:
    print psr.getContent(element)"""
