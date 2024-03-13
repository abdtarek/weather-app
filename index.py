#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

# city
city = " cairo"
 
# create url
url = "https://www.google.com/search?q="+"weather"+city

#print(url)
 
# requests instance
html = requests.get(url).content
 
# getting raw data
soup = BeautifulSoup(html, 'html.parser')

# get the temperature
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

# this contains time and sky description
str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
 
# format the data
data = str.split('\n')
time = data[0]
sky = data[1]

# list having all div tags having particular class name
listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
 
# particular list with required data
strd = listdiv[5].text
 
# formatting the string
pos = strd.find('Wind')
other_data = strd[pos:]

# printing all the data
print ("Content-Type: text/html")
print()
print ("<html><head>")
print ("</head><body>")
print ("WeatherApp v2 In Progress ..." + "</br> </br>")
print("Temperature is: "  + temp + "</br></br>")
print("Time: " +  time + "</br></br>")
print("Sky Description: " + sky + "</br></br>")
print(other_data)
print ("</body></html>")
