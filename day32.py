#function 형태로 리팩토링


# #instargram for selenium
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

def login(id, password):
    #login 하기위해 xpath 필요함
    id = "test@naver.com"
    password ="test"

    input_id = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
    input_id.send_keys(id)

    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password).send_key(password)
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').send_keys(password).send_keys(Keys.ENTER)

login(id, password)




def search(hashtag, scroll_times):
#search
    url = f"https://www.instagram.com/explore/tags/{hashtag}"
    driver.get(url=url)

#scroll
    for _ in range(scroll_times):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #javascript 실행
        time.sleep(7)

hashtag = "강아지"
search(hashtag, 5)



def like_comment(nth, comment, repeat=3):
    #nth 포스트 클릭
    row = (nth - 1) // 3 + 1
    col = (nth - 1) % 3 + 1

    xpath = f'/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[1]/div/div/div[2]/div[3]/a/div[{row}]/div[{col}]'
    driver.find_element(By.XPATH, xpath).click()

    for _ in range(repeat):
        #like
        like_xpath = f'/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[1]/div/div/div[2]/div[3]/a/div]'
        driver.find_element(By.XPATH, like_xpath).click()

        #댓글 달기

        comment_xpath = f'/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[1]/div/div/div[2]/div[3]/a/div]'
        driver.find_element(By.XPATH, comment_xpath).click()
        driver.find_element(By.XPATH, comment_xpath).send_keys(comment)

        #게시버튼 누르기

        comment_button_xpath = f'/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[1]/div/div/div[2]/div[3]/a/div/button]'
        driver.find_element(By.XPATH, comment_button_xpath).click()

        #다음 게시물 
        next_button_xpath = f'/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[1]/div/div/div[2]/div[3]/a/div/button]'
        driver.find_element(By.XPATH, next_button_xpath).click()

like_comment(4, '강아지가 귀여워요', 2)

time.sleep(20)









