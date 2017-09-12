#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, render_template, url_for, request, redirect
from pymongo import MongoClient
from redis import Redis

r = Redis(host='redis', port=6379)
app = Flask(__name__)

m = MongoClient('mongo', 27017)
db = m.tododb

@app.route('/')
def todo():
    _items = db.tododb.find()
    items = [item for item in _items]
    return render_template('todo.html', items=items)


@app.route('/new', methods=['POST'])
def new():
    item_doc = {
        'name': request.form['name'],
        'description': request.form['description']
    }
    db.tododb.insert_one(item_doc)
    return redirect(url_for('todo'))


@app.route('/redis')
def hello():
    r.incr('hits')
    return 'I have been seen %s times' % r.get('hits')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
