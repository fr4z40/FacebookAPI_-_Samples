#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Eduardo Frazão ( http://github.com/fr4z40 )

from urllib.request import urlopen
from bs4 import BeautifulSoup as bsp
from time import sleep
from getpass import getpass

# ------------------------------------------------------------------------------- #
                                                                                  #
from facebook import GraphAPI                                                     #
                                                                                  #
def wall_post(pub_text, title, pub_link, cap, desc, pic_url):                     #
    dict_in = {"name": title,"link": pub_link,                                    #
               "caption": cap,"description": desc,                                #
               "picture": pic_url}                                                #
    facebook_api.put_wall_post(pub_text, attachment=dict_in, profile_id='me')     #
                                                                                  #
# ------------------------------------------------------------------------------- #


def source(url):
    return(bsp((urlopen(url)).read()))

facebook_api = GraphAPI(getpass("Token:"))
url = 'http://www.cnet.com/news/'
html_sample = source(url)
rst = ((((html_sample.find_all('div',{'class':'fdListingContainer'}))[0]).find_all('div'))[0])
rst = rst.find_all('div',{'class':'row'})

for r in rst:
    try:
        text = 'Facebook API + Beautifulsoup\n\nWeb Scraping and Publishing test\n'
        link = (url + (((r.find_all('a',{'class':'imageLinkWrapper'}))[0]).get('href')))
        img = (((r.find_all('img'))[1]).get('src'))
        title = ((((r.find_all('h3'))[0]).text).strip())
        desc = (((r.find_all('p')[0]).text).strip())
        caption = (((r.find_all('span',{'class':'assetAuthor'})[0]).text).strip())

       # ------------------------------------------------ #
        wall_post(text, title, link, caption, desc, img)  #
       # ------------------------------------------------ #

        print('Published: %s' % title)
        sleep(60)

    except:
        pass
