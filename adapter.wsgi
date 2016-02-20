import os
import sys
import bottle

sys.path = ['/home/grzybek/Projects/BottleTest/'] + sys.path
os.chdir(os.path.dirname(__file__))

import server_apache

application = bottle.default_app()
