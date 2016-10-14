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
    since = get_datetime(since)
    sentiments, latest = db.latest_sentiments(since)
    next_url = flask.url_for('sentiments',since=get_datetimekey(latest))
    return flask.jsonify(sentiments=sentiments, nextUrl=next_url)
  
def get_datetimekey(latest):
    return u';'.join(map(unicode, latest.timetuple()[:6]))
  
def get_datetime(key):
    if not key:
        return datetime.datetime.now() - datetime.timedelta(hours=1)
    return datetime.datetime(*map(int, key.split(';')))