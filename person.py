from bs4 import BeautifulSoup

class Person(object):
    def __init__(self,elem:str) -> None:
        global info,base
        base='https://www.itjuzi.com'
        info=elem
        soup = BeautifulSoup(info, 'html.parser')
        # self.name=self.url=self.image_url=self.designation=self.intro=''
        self.name = soup.find('a', {'class': 'name'}).text.strip()
        self.url=base+soup.find('a',{'class':'name'}).get('href')
        self.designation = soup.find('a', {'class': 'des'}).text.strip()
        # self.image_url = soup.find('img', {'class': 'usericon'}).get('src')
        self.intro = soup.find('p', {'class': 'intro'}).text.strip()
        pass
