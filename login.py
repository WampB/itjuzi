import time,json
from selenium import webdriver
from selenium.webdriver.common.by import By

global option,url,info,cookies

option=webdriver.ChromeOptions()
option.add_argument("--disable-images")
option.add_argument("--disable-javascript")
option.add_argument("--disable-blink-features=AutomationControlled")
# option.add_argument('--proxy-server=http://114.116.2.116:8001')

info="info.json"
cookies="cookies.json"
url="https://www.itjuzi.com/"

class Login(object):
    def __init__(self) -> None:
        self.option=option
        self.info=info
        self.cookies=cookies
        self.url=url
        pass
    def pwd_login(self)->webdriver.Chrome: #log in by id and password
        driver=webdriver.Chrome(options=option)
        driver.implicitly_wait(3)
        with open(info,"r",encoding="utf-8") as f:
            id_pwd=json.loads(f.read())
        logURL=url+'login?%2F'
        driver.get(logURL)
        time.sleep(2)
        try:
            driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div/input').send_keys(id_pwd['id'])
            driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/form/div[2]/div/div/input').send_keys(id_pwd['pwd'])
            driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div/button').click()
            time.sleep(2)
            driver.find_element(By.XPATH,'/html/body/div[7]/div/div/div/i').click()
            print("Successful login!")
        except:
            print('Failure while login!')
            pass
        return driver
    def cookieLogin(self)->webdriver.Chrome:
        driver = webdriver.Chrome(options=option)
        driver.get(url)
        with open(cookies, 'r', encoding='utf-8') as f:
            listCookies = json.loads(f.read())
        f.close()
        for cookie in listCookies:
            driver.add_cookie(cookie)
        driver.get(url)
        print("Successful self-login!")
        return driver
    def loadCookies(self,driver:webdriver.Chrome)->None:
        cookies=json.dumps(driver.get_cookies())
        with open("cookies.json","w") as f:
            f.write(cookies)
        f.close()
        print("Successfully loaded Cookies!")