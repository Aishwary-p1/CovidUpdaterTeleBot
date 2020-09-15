import requests
from bs4 import BeautifulSoup as bs

url = "https://www.mohfw.gov.in/"

page = requests.get(url)

soup = bs(page.text,"html.parser")

st = str(soup.find_all('strong', class_="mob-hide"))

active, recovered, deaths = [], [], []

ans, temp = [], ''

for i in range(len(st)-1):
    if st[i].isdigit():
        temp+=st[i]
        if not(st[i+1].isdigit()):
            ans.append(temp)
            temp=''
            
def get_active():
	return [ans[0], ans[1]]

def get_recovered():
	return [ans[2], ans[3]]

def get_deaths():
	return [ans[4], ans[5]]

