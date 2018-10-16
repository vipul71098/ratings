
import requests
import re
from bs4 import BeautifulSoup as soup

fb = []
google = []

hotel_name = input("ENTER HOTEL NAME :")

response_facebook = requests.get("https://www.google.co.in/search?q="+hotel_name+"+HOTEL+FACEBOOK")
response_google = requests.get("https://www.google.co.in/search?q="+hotel_name+"+HOTEL+google ratings")

page_soup_facebook=soup(response_facebook.text,"html.parser")
page_soup_google=soup(response_google.text,"html.parser")

for f in page_soup_facebook.find_all( string=re.compile("Rating")):
	fb.append(f)
for g in page_soup_google.find_all( string=re.compile("Rating")):
	google.append(g)

print("FACEBOOK Rating:")
print(fb[0])

print("Google Rating:")
G =google[0]
print(G[0:25])
