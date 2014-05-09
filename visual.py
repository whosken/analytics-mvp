#!/usr/bin/python
# -*- coding: utf-8 -*-

import flask

import db

app = flask.Flask(__name__)

@app.route('/')
def dashboard():
    return flask.render_template('dashboard.html')
  
@app.route('/poll/sentiments')
def sentiments():
    pass

if __name__ == '__main__':
    import tornado.wsgi
    import tornado.httpserver
    import tornado.ioloop
    
    (tornado.httpserver
     .HTTPServer(tornado.wsgi.WSGIContainer(app))
     .listen(5000))
    tornado.ioloop.IOLoop.instance().start()
    