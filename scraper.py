from bs4 import BeautifulSoup
import urllib

def getcontent(url):
    try:
        page = BeautifulSoup(urllib.urlopen(url).read())
    #print(page.title.string)
    
        name = page.find('h1', id='itemTitle')
        print(name.string)

        photo = page.find('img', id='imgPhoto', itemprop='image')
        print(photo['src'])
        
        ingred = []
    
        for span in page.find_all('span', 'ingredient-name'):
            if span.has_key('class'): #and span['class'] == 'ingredient-name':
                print(span.string)
                ingred.append(span.string)
    except:
        pass


def getpagesAR(url):
    page = BeautifulSoup(urllib.urlopen(url).read())
    links = set()
    for link in page.find_all('a'):
        if link.has_key('href'):
            if 'detail.aspx' in link['href'] and 'recipe/' in link['href']:
                links.add(link['href'])
            #if 'NEXT' in link.string:
                #print('has next!')
                #getpagesAR(link['href'])
    print(links)
    for link in links:
        getcontent(link)

getpagesAR('http://allrecipes.com/recipes/ViewAll.aspx')
