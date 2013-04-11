from bs4 import BeautifulSoup
import urllib

def snag(url):
    page = BeautifulSoup(urllib.urlopen(url).read())
    print(page.title.string)
    
    name = page.find('h1', id='itemTitle')
    print(name.string)

    photo = page.find('img', id='imgPhoto', itemprop='image')
    print(photo['src'])
    
    ingred = []
    
    for span in page.find_all('span', 'ingredient-name'):
        if span.has_key('class'): #and span['class'] == 'ingredient-name':
            print(span.string)
            ingred.append(span.string)
