import time
from selenium import webdriver
from selenium.webdriver.common.by import By

global base
base='https://www.itjuzi.com/person'

class Classify(object):
    def __init__(self,driver:webdriver.Chrome) -> None:
        global d
        d=driver
        d.get(base)
        self.driver=d
        # self.industries,self.locations,self.turns=self.get_classification()
        # self.provinces=self.get_details(self.locations[0])
        # self.continents=self.get_details(self.locations[1])
        pass
    def get_classification(self)->list: #获取三个基本分类标签：行业、地区、轮次
        d.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div/div/div/div[2]/div[1]/div[1]/div[1]/div[3]').click()
        time.sleep(2)
        lst1=d.find_elements(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div/div/div/div[2]/div[1]/div[1]/div[4]/div/div[2]/span')[1:]   #the first time the program pause at No.8-"education"; second time at No.11-"sports"
        lst2=d.find_elements(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div/div/div/div[2]/div[1]/div[1]/div[5]/div[1]/div[2]/span')[1:3]
        lst3=d.find_elements(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div/div/div/div[2]/div[1]/div[1]/div[7]/div/div[2]/span')[2:6]
        return lst1,lst2,lst3
    def get_details(self,l:webdriver.Chrome._web_element_cls)->list:    #传入的是web节点
        l.click()
        time.sleep(2)
        lst=d.find_elements(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div/div/div/div[2]/div[1]/div[1]/div[5]/div[2]/div[2]/span')
        return lst
    def logout(self)->None:
        d.get(base)
        time.sleep(2)
        try:
            d.find_element(By.XPATH,'/html/body/div[7]/div/div/div/i').click()
        except:
            pass
        time.sleep(1)
        d.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/div/div[1]/nav/div/div[2]/div/span').click()
        d.quit()
        pass