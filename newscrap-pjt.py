from bs4 import BeautifulSoup as bs
import requests
import csv
import os

# *****Create empty list to save Headings & Links. *****#
Headings = []
Links = []

# *****Create User-Agent***** #
user_agent = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}

# *****Url of site which to be scrapped***** #
url = "https://www.thehindu.com/news/"

# *****Make get request to url using requests library***** #
r=requests.get(url , headers = user_agent)

# *****Use BeautifulSoup to convert scrapped dato into text***** #
soup=bs(r.text , 'html5lib')

# *****Scrap data which is needed***** #
News = soup.find_all('a', class_ = 's4x-100-ls-heading')

for news in News:
    Headings.append(news.get_text())
    Links.append(news.attrs['href'])
# print(Headings)
# print(Links)
# print(len(Links))

# *****Save scrapped data in to .csv file***** #
with open('NewsData.csv','a',newline='') as csv_file:
    empty_file = os.stat('NewsData.csv',).st_size==0
    Table=['Title','Link']
    w=csv.DictWriter(csv_file, fieldnames = Table)
    if empty_file:
        w.writeheader()
    for j in range(len(Headings)):
        w.writerow({'Title':Headings[j],'Link':Links[j]})
