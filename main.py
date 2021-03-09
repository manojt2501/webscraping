import requests
from bs4 import BeautifulSoup
import csv
URL="https://scrapethissite.com/pages/simple/"
res= requests.get(URL)
soup =BeautifulSoup(res.content,'html5lib')
country_all=soup.find_all('div', attrs = {"class":"col-md-4 country"})
lists=[]
for country in country_all:
    list={}
    list['country_name']= country.h3.text.replace('\n','').strip()
    list['country_capital']=country.find('span',attrs={"class":"country-capital"}).text
    list['country_population']=country.find('span',attrs={"class":"country-population"}).text
    list['country_area']=country.find('span',attrs={"class":"country-area"}).text
    lists.append(list)
try:
    with open('country_data.csv', 'w',encoding='utf-8') as csvfile: #used UTF-8 encoding as my scraped data was containing unicode characters
        writer = csv.DictWriter(csvfile, fieldnames=['country_name','country_capital','country_population','country_area'])
        writer.writeheader()
        for list in lists:
            writer.writerow(list)
        csvfile.close()
except IOError:
    print("I/O error")
try:
    for mylist in lists:
        columns = ', '.join("" + str(x) + "" for x in mylist.keys())
        values = ', '.join("'" + str(x) + "'" for x in mylist.values())
        sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('mytable', columns, values)
        print(sql)
        f= open("scrap.sql","a", encoding="UTF-8")
        f.write(sql + '\n')
    f.close()
except IOError:
    print("I/O error")

