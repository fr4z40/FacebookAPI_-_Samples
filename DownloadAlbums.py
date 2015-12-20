#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Eduardo Frazão
#   * http://github.com/fr4z40
#   * https://bitbucket.org/fr4z40

import json
from urllib.request import urlopen
from subprocess import call
from getpass import getpass
from os import mkdir, chdir
from os.path import exists

# --------------------------- #
from facebook import GraphAPI #
# --------------------------- #


def down(url):
    cli = 'Mozilla/5.0 Gecko/20100101 Firefox/39.0'
    call(('wget -t 5 --user-agent="%s" -c "%s"' % (cli,url)), shell=True)


# -------------------------------------------------------------------------------------------------- #

def down_photos(album_name, album_id, qtd):
    if exists('%s' % album_name) == False:
        mkdir('%s' % album_name)
    chdir('%s' % album_name)
    try:
        photos = (facebook_api.get_connections(album_id, 'photos'))['paging']['next']
        photos = (((((photos.split('&after='))[0]).split('limit='))[0]) + 'limit=' + str(qtd))
        photos = ((json.loads((urlopen(photos)).read().decode('utf8')))['data'])
        for p in photos:
            down(((p['images'])[0])['source'])
            print('\n')
    except:
        pass
    chdir('..')


facebook_api = GraphAPI(getpass("Token:"))
user_id = (facebook_api.get_object("me"))['id']
albums = (facebook_api.get_connections(user_id, 'albums'))['data']
for a in albums:
    try:
        album_name = a['name']
        album_id = a['id']
        qtd = a['count']
        print('Saving Album: "%s"\nTotal Pics: %s\n\n' % (album_name, str(qtd)))
        down_photos(album_name, album_id, qtd)
    except:
        pass

# -------------------------------------------------------------------------------------------------- #
