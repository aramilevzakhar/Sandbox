from bs4 import BeautifulSoup as bs4
import requests 



#print(sorted(names, reverse=True))



class name:
    def __init__(self):
        pass
       
    def getNames(self):
        text = ""
        with open('/home/zakhar/Downloads/123.html', 'r', encoding='UTF8') as fi:
            text += fi.read()
        with open('/home/zakhar/Downloads/567.html', 'r', encoding='UTF8') as fi:
            text += fi.read()
        soup = bs4(text, 'html.parser')
#print(soup.prettify())
        names = [ item.get_text() for item in soup.findAll(class_='nameslist') ]
        names = sorted(names, reverse=False)
        names = set(names)
        return names
                

    





