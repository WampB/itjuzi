import time
from login import Login
from selenium import webdriver
from person import Person
from classify_person import Classify
from selenium.webdriver.common.by import By

global base,industries,locations,turns,file,countFile
base='https://www.itjuzi.com/person'
d_class=Classify(Login().pwd_login())
industries,locations,turns=d_class.get_classification()
# provinces=d_class.get_details(locations[0])
# continents=d_class.get_details(locations[1])
driver=d_class.driver
file=open("persons.txt",'a+',encoding='utf-8')
countFile=open("count.txt","a+",encoding="utf-8")

def clear(driver:webdriver.Chrome)->None:
    btn=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div/div[2]')
    btn.click()
    pass

def write_info(industry:str,turn:str,in_or_out:str)->None:   #crawler on a page
    persons=driver.find_elements(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div/div/div/div[2]/div[1]/div[2]/div')
    for i in persons:
        one=Person(i.get_attribute("innerHTML"))
        file.write(one.name+'\t'+one.designation+'\t'+one.intro+'\t'+industry+'\t'+turn+'\t'+in_or_out+'\t'+one.url+'\n')
    pass

def craw_eachclass(industry:str,turn:str,in_or_out:str)->None:
    try:
        pagenum=len(driver.find_elements(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div/div/div/div[2]/div[1]/div[3]/div/ul/li'))
        countFile.write(industry+'\t'+turn+'\t'+in_or_out+str(pagenum)+'pages\n')
    except:
        return
    if pagenum==1:
        write_info(industry,turn,in_or_out)
    elif pagenum>=4:
        while True:
            try:
                write_info(industry,turn,in_or_out)
                driver.find_element(By.CSS_SELECTOR,"button.btn-next[type='button']").click()
                time.sleep(1)
            except:
                driver.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[1]/div').click()
                driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div/div/div/div[2]/div[1]/div[3]/div/ul/li[1]').click()
                break
    else:
        for i in range(pagenum):
            write_info(industry,turn,in_or_out)
            driver.find_element(By.CSS_SELECTOR,"button.btn-next[type='button']").click()
            time.sleep(1)
    pass

for i in locations:
    for k in industries:
        for m in turns:
            time.sleep(1)
            i.click()
            k.click()
            m.click()
            time.sleep(1)
            craw_eachclass(k.text,m.text,i.text)
            clear(driver)
        time.sleep(2)
    time.sleep(2)
file.close()
countFile.close()
input('input to end')
d_class.logout()
