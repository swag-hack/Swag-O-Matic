#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Daniel
#
# Created:     03/03/2017
# Copyright:   (c) Daniel 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from ConfigParser import ConfigParser

config = ConfigParser()
#config.read('data/configs.ini')
config.add_section('Watch')
config.set('Watch', 'Vid_Fle', 'data/playlists.txt')
config.set('Watch', 'Min_Delay', 5)
config.set('Watch', 'Max_Delay', 3600)
config.set('Watch', 'Advance', True)
config.set('Watch', 'Sleep', 10)

config.add_section('Scrape')
config.set('Scrape', 'Vid_Fle', 'data/playlists.txt')
config.set('Scrape', 'Cat_Fle', 'data/catas.txt')
config.set('Scrape', 'Sort_Min', True)


with open('data/configs.ini','w') as conf:
    config.write(conf)