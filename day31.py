#instargram for selenium
#selenium -> 사람이 화면에서 작동하듯 사용할 수 있음. requests에서 안되는 것들 해결 가능

from selenium import webdriver
import chromedriver_autoinstaller 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.implicitly_wait(8) #3초 wait option

url = "https://www.instagram.com/"

driver.get(url=url)
time.sleep(200)


#login 하기위해 xpath 필요함
id = "test@naver.com"
password ="test"
input_id = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
input_id.send_keys(id)

driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password).send_key(password)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').send_keys(password).send_keys(Keys.ENTER)


#search
hashtag = "강아지"
url = f"https://www.instagram.com/explore/tags/{hashtag}"
driver.get(url=url)

#scroll
for _ in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #javascript 실행
    time.sleep(7)

















