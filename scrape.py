import requests 
from bs4 import BeautifulSoup

base_url = "https://www.yelp.ca/search?find_desc=Restaurants&find_loc="
loc = 'Newport+Beach,+CA'
page = 0
current_page = 0

while current_page < 201:
	url  = base_url + loc + "&start=" + str(current_page)
	yelp_r = requests.get(url)
	yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')
	businesses = yelp_soup.findAll('div', {'class': 'biz-listing-large'})
	file_path = 'yelp-{loc}.txt'.format(loc=loc)
	with open(file_path,"a") as textfile:
		businesses = yelp_soup.findAll('div', {'class': 'biz-listing-large'})
		for biz in businesses:
		#(biz.text)
		title = biz.findAll('a', {'class': 'bizz-name'})[0].text
		print(title)
		address = biz.findAll('adress')[0].text
		print(address)
		print('\n')
		phone = biz.findAll('span', {'class': 'biz-phone'})[0].text
		print(phone)
		page_line="{title}\n{address}\n{phone}\n\n".format(
			title=title,
			address=address,
			phone=phone)
		textfile.write(page_line)
	current_page +=10
























print(yelp_soup.findAll('li', {'class': 'regular-search'}))

for name in yelp_soup.findAll('li', {'class': 'regular-search'}):
	print(name.txt)















print(yelp_r.status_code)

yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')


print(yelp_soup.prettify())
print(yelp_soup.findAll('li',{}))

for link in yelp_soup.findAll('a'):
	print(link)