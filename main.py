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
    #print("country name:" ,country_name, "country capital:",country_capital, "country population:",country_population, "country area:",country_area)
    lists.append(list)
try:
    with open('country_data.csv', 'w',encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['country_name','country_capital','country_population','country_area'])
        writer.writeheader()
        for list in lists:
            writer.writerow(list)
        csvfile.close()
except IOError:
    print("I/O error")




