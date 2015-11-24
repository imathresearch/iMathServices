'''
Created on Nov 23, 2015

@author: izubizarreta
'''
import sys

import tornado.ioloop
import tornado.web
from ListHandlers import ListHandlers

if __name__ == '__main__':
    Application = ListHandlers()
    app = Application.make_app()
    app.listen(int(sys.argv[1]))
    tornado.ioloop.IOLoop.current().start()
