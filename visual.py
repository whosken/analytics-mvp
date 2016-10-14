#!/usr/bin/python
# -*- coding: utf-8 -*-

import flask
import datetime
import os

import db
import config

app = flask.Flask(__name__)

@app.route('/')
def dashboard():
    return flask.render_template(
        'dashboard.html',
        topic=config.get('TOPIC','TOPIC','python'))

@app.route('/poll/sentiments/')
@app.route('/poll/sentiments/<since>')
def sentiments(since=None):
    since = get_datetime_tuple(since)
    sentiments, latest = db.latest_sentiments(since)
    next_url = flask.url_for('sentiments',since=get_datetimekey(latest))
    return flask.jsonify(sentiments=sentiments, nextUrl=next_url)
  
def get_datetimekey(latest):
    return u';'.join(map(unicode, latest))
  
def get_datetime_tuple(key):
    if key: return map(int, key.split(';'))
    key = list(datetime.datetime.utcnow().timetuple()[:6])
    return key
  

if __name__ == '__main__':
    import tornado.wsgi
    import tornado.httpserver
    import tornado.ioloop
    
    (tornado.httpserver
     .HTTPServer(tornado.wsgi.WSGIContainer(app))
     .listen(os.environ.get('PORT') or 5000))
    tornado.ioloop.IOLoop.instance().start()
