#!/usr/bin/env python3
'''
    example_flask_app.py
    Jeff Ondich, 22 April 2016
    Modified by Eric Alexander, January 2017

    A slightly more complicated Flask sample app than the
    "hello world" app found at http://flask.pocoo.org/.
'''
import flask
from flask import render_template
import json
import sys
import datasource

app = flask.Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def home():
    comments = []
    errors = []

    ds = datasource.DataSource()

    if requests.method == "POST":
        #get keywords, other comment specs from submitted form
        keywords = request.form['keywords']
        edited = request.form['edited']
        gilded = request.form['gilded']
        controversial = request.form['controversial']
        goodSentiment = request.form['goodSentiment']
        badSentiment = request.form['badSentiment']
        scoreLow = request.form['scoreLow']
        scoreHigh = request.form['scoreHigh']

        #return proper results based on score params
        if scoreLow and scoreHigh:
            queryResult = ds.getScoreInRange(scoreLow, scoreHigh)
            comments.append(queryResult)
        elif scoreLow and not scoreHigh:
            queryResult = ds.getScoreAbove(scoreLow)
            comments.append(queryResult)
        elif scoreHigh and not scoreLow:
            queryResult = ds.getScoreBelow(scoreHigh)
            comments.append(queryResult)

    return render_template('resultsTemplate.html', comments=comments)



if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
