import requests
from bs4 import BeautifulSoup
import pandas as pd

data=[]
for i in range(4):
  num=i+1
  header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
  url=f'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20231122&hh=14&rtm=Y&pg={num}'
  request=requests.get(url,headers=header)
  soup = BeautifulSoup(request.text)
  table=soup.find('table',{'class':'list-wrap'})
  artists=table.findAll('a',{'class':'artist'})
  titles=table.findAll('a',{'class':'title'})
  for i, (t, a) in enumerate(zip(titles, artists)):
    title = t.text.replace('19금\n', '').strip()
    artist = a.text.strip().split('\n')[0]
    dic={'순위':(num-1)*50+i+1, '아티스트':artist, '제목':title}
    data.append(dic)

df=pd.DataFrame(data)
df.to_excel('geniechart.xlsx') 