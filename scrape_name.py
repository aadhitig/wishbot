# NOT implemented as part of bot.py
# Possible usage: ask user if they would like to add the suggested gift (by displaying the name and soliciting a 'yes' or 'no') before adding it to the wishlist

# #-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

def getName(url):
'''Takes a product URL as an input and isolates and prints the product's name/title'''
	content = requests.get(url).content
	soup = BeautifulSoup(content, features='lxml')
	product_names = str(soup.findAll('title')[0])
	list_pn = product_names.split()
	list_pn.remove('|')
	list_pn.remove('Etsy</title>')
	list_pn[0] = list_pn[0][7:]
	print(' '.join(list_pn))
