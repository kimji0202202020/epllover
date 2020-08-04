from bs4 import BeautifulSoup
import requests
from selenium import webdriver

path = "/Users/yjlee/Downloads/chromedriver "
driver = webdriver.Chrome(path, chrome_options=options)
driver.implicitly_wait(3)

naver_wfootball = "https://sports.news.naver.com/wfootball/record/index.nhn?category=epl"
driver.get(naver_wfootball)

page = driver.page_source
premi_team_rank_list = BeautifulSoup(page, "html.parser")
team_rank_list = premi_team_rank_list.select('#wfootballTeamRecordBody>table>tbody>tr')

for team in team_rank_list:
    num = team.select('.num > div.inner > strong')[0].text
    name = team.select('.name')[0].text
    print(num + "위 : " + name)
