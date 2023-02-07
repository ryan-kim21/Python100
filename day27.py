#robots.txt를 확인해 허용범위 확인하기
#웹 크롤링

from bs4 import BeautifulSoup
import requests


url = "https://finance.naver.com/item/main.naver?code=005930"
res = requests.get(url)
# print(res.text)

bsobj = BeautifulSoup(res.text, "html.parser")

div_today = bsobj.find("div",{"class":"today"})
em = div_today.find("em")

price = em.find("span",{"class":"blind"}).text

# print(div_today)
print(price)
# print(em)
# print(bsobj)








