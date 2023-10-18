from selenium import webdriver
from selenium.webdriver.common.by import By
import bs4

class Crawler(webdriver.Chrome):
    def __init__(self,d:webdriver.Chrome) -> None:
        global driver,base
        driver=d
        base="https://www.itjuzi.com"
        pass
    def process_person(self,url:str):
        lst=[]
        driver.get(url)
        inrto_p=education=work='nothing'
        try:
            inrto_p=driver.find_element(By.XPATH,'//*[@id="__layout"]/div/main/div[2]/div[2]/div[1]/div/div[1]/div/div').text
        except:
            pass
        region=driver.find_element(By.XPATH,'//*[@id="__layout"]/div/main/div[2]/div[1]/div/div/div[3]/div/span[1]').text
        try:
            education=driver.find_element(By.XPATH,'//*[@id="__layout"]/div/main/div[2]/div[2]/div[1]/div/div[4]/div/div').text
        except:
            pass
        try:
            work=driver.find_element(By.XPATH,'//*[@id="__layout"]/div/main/div[2]/div[2]/div[1]/div/div[3]/div/div').text
        except:
            pass
        lst.append(inrto_p)
        lst.append(region)
        lst.append(work)
        lst.append(education)
        firms=driver.find_elements(By.XPATH,'//*[@id="__layout"]/div/main/div[2]/div[2]/div[1]/div/div[2]/div/div/ul/li')
        lst_firms=[]
        for elem in firms:
            soup=bs4.BeautifulSoup(elem.get_attribute('innerHTML'),'html.parser')
            company_name = soup.find('span', class_='title').text
            industry = soup.find('i', class_='primary-text').text
            company_url=base+soup.find('a',class_='person-company-item').get("href")
            founding_date = soup.find_all('span')[1].text
            description = soup.find('p').text.strip()
            image_url=soup.find('img').get("src")
            lst_firms.append([company_name,industry,company_url,founding_date,description,image_url])
        num=len(lst_firms)
        lst.append(lst_firms)
        return num,lst  #intro_p, region, work, education, name, industry, url, date, description, image
    def process_company(self,url:str):
        driver.get(url)
        register_name=phone=mail=details=labels=finance_time=turn_now=turn_now_amount=investors=website=address='empty'

        #website
        try:
            contact1=driver.find_element(By.XPATH,'//*[@id="__layout"]/div/main/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[1]')
            soup1=bs4.BeautifulSoup(contact1.get_attribute('innerHTML'),'html.parser')
            website=soup1.find('a').text
        except:
            pass
        
        #phone-mail-address
        contact2=driver.find_element(By.XPATH,'//*[@id="__layout"]/div/main/div[2]/div[3]/div[2]/div[1]/div[4]')
        soup2=bs4.BeautifulSoup(contact2.get_attribute('innerHTML'),'html.parser')
        infos=soup2.find_all('div',class_='company-contact-item')
        try:
            phone=infos[0].text
            mail=infos[1].text
            address=infos[2].text
        except:
            pass

        #labels:list
        label_elem=driver.find_element(By.XPATH,'//*[@id="__layout"]/div/main/div[2]/div[2]/div/div[2]/div[1]/div')
        label_lst=bs4.BeautifulSoup(label_elem.get_attribute('innerHTML'),'html.parser')
        labels=[]
        for label in label_lst:
            labels.append(label.text)

        #detailed introduction
        detail_elem=driver.find_element(By.XPATH,'//*[@id="desc"]')
        details=bs4.BeautifulSoup(detail_elem.get_attribute('innerHTML'),'html.parser').find('p').text

        #register name
        try:
            register_name=driver.find_element(By.CSS_SELECTOR,'#pane-1 > table > tbody > tr:nth-child(1) > td > span').text
        except:
            try:
                register_name=driver.find_element(By.XPATH,'//*[@id="desc"]/div/div/div[2]/div/span[1]').text
            except:
                pass

        #financing events
        try:
            table_elem=driver.find_element(By.XPATH,'//*[@id="pane-1"]/div[1]/div/div/div[3]/table')
            soup3=bs4.BeautifulSoup(table_elem.get_attribute('innerHTML'),'html.parser')
            finances=soup3.find_all('td')
            finance_time=finances[0].text
            turn_now=finances[1].text
            turn_now_amount=finances[2].text
            try:
                invs=soup3.find_all('li')
                investors=[]
                for i in invs:
                    investors.append(i.text)
            except:
                investors=[finances[3].text]
        except:
            pass
        
        return register_name,phone,mail,details,labels,finance_time,turn_now,turn_now_amount,investors,website,address

