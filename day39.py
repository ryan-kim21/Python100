import requests
import pandas as pd
import openpyxl

from libs.evparser import EvGoKrSubsidyParser

url = "https://www.ev.or.kr/portal/localInfo"

data = requests.get(url)

print(data.text)

# f = open("local_info.html", "w+", encoding="utf-8")
# f.write(data.text)
# f.close()


ev_parser = EvGoKrSubsidyParser(data.text)
ev_parser.save_to_excel("crawl_subsidy_all.xlsx")

