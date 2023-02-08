from bs4 import BeautifulSoup
import requests

input_code = input("Please input you want to search the code : ")

def crawl(code):

    url=f"https://finance.naver.com/item/main.naver?code={code}"
    res = requests.get(url)


    bsobj = BeautifulSoup(res.text, "html.parser")

    div_today = bsobj.find("div",{"class":"today"})
    em = div_today.find("em")

    price = em.find("span",{"class":"blind"}).text


    print(price)


    h_company = bsobj.find("div", {"class":"h_company"})
    name = h_company.a.text

    code = bsobj.find("div", {"class":"description"})
    # print(description.span.text)
    code = code.span.text


    table_no_info = bsobj.find("table",  {"class":"no_info"})
    # print(table_no_info.tr.find_all("td"))
    tds = table_no_info.tr.find_all("td")
    volume = tds[2].find("span", {"class":"blind"}).text
    print(volume)
    # print(ratio)
    # print(tds[2])

    dic = {"price" : price, "name": name, "code":code, "volume":volume }

    return dic


dic = crawl(f"{input_code}")
print(dic)