#!/usr/bin/python
# -*- coding: utf-8 -*-

import flask

import db

app = flask.Flask(__name__)

@app.route('/')
def dashboard():
    pass
  
@app.route('/poll/sentiments')
def sentiments():
    pass
