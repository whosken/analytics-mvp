#!/usr/bin/python
# -*- coding: utf-8 -*-

import flask
import datetime

import db

app = flask.Flask(__name__)

@app.route('/')
def dashboard():
    return flask.render_template('dashboard.html')

@app.route('/poll/sentiments')
@app.route('/poll/sentiments/<since_datetime>')
def sentiments(since_datetime=None):
    sentiments = db.latest_sentiments(get_datetime_tuple(since_datetime))
    next_url = flask.url_for('sentiments',since_datetime=get_datetimekey())
    return flask.jsonify(sentiments=sentiments, nextUrl=next_url)
  
def get_datetimekey():
    return u';'.join(datetime.datetime.now().timetuple())
  
def get_datetime_tuple(key):
    return key.split(';')[:6]
  

if __name__ == '__main__':
    import tornado.wsgi
    import tornado.httpserver
    import tornado.ioloop
    
    (tornado.httpserver
     .HTTPServer(tornado.wsgi.WSGIContainer(app))
     .listen(5000))
    tornado.ioloop.IOLoop.instance().start()
    