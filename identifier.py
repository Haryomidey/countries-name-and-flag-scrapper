from bs4 import BeautifulSoup
import requests
import json

soup = BeautifulSoup(requests.get('https://www.worldometers.info/geography/flags-of-the-world/').text, 'html.parser')

content_inner = soup.find('div', {"class": "content-inner"})

rows = content_inner.find('div', {'class': "row"}).find_all('div', {'class': "col-md-4"})

countries_name_and_flag = []

for row in rows:
    dic = {}
    image_src = f"https://www.worldometers.info/{row.img['src']}"
    name = row.find('div', {'style': "font-weight:bold; padding-top:10px"}).text
    
    
    dic['country_name'] = name
    dic['flag_src'] = image_src

    countries_name_and_flag.append(dic)

with open('countries_name_and_flag.json', 'w') as json_file:
    json.dump(countries_name_and_flag, json_file, indent=4)

print("Data has been successfully dumped into 'countries_name_and_flag.json' file.")

