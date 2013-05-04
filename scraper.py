from bs4 import BeautifulSoup
import urllib

def getcontent(url):
    try:
        page = BeautifulSoup(urllib.urlopen(url).read())
        
        #find title
        name = page.find('h1', id='itemTitle')
        print(name.string)

        #find photograph
        photo = page.find('img', id='imgPhoto', itemprop='image')
        print(photo['src'])
        
        #find ingredients
        ingred = []
        for span in page.find_all('span', 'ingredient-name'):
            if span.has_key('class'): #and span['class'] == 'ingredient-name':
                print(span.string)
                ingred.append(span.string)
    except:
        #do nothing if cannot connect
        pass


def getpagesAR(url):
    page = BeautifulSoup(urllib.urlopen(url).read())
    links = set()
    nexturl = None
    for link in page.find_all('a'):
        if link.has_key('href'):
            if 'detail.aspx' in link['href'] and 'recipe/' in link['href']:
                links.add(link['href'])

            #gets lintto the next page
            if link.string is not None and "NEXT" in link.string:
                nexturl = link['href']
    #gets recipe information
    for link in links:
        getcontent(link)
    
    if nexturl is not None:
        getpagesAR(nexturl)

getpagesAR('http://allrecipes.com/recipes/main-dish/ViewAll.aspx?Photos=On')


