'''
########################################
#    Flask app for Reddimentary        #
#    CS257                             #
#    Web Team J:                       #
#        @hansonc2, @craigj2, @sayanic #
#                                      #
########################################
'''
import flask
from flask import render_template, request
import json
import sys
import datasource

app = flask.Flask(__name__)

@app.route('/results', methods = ['GET', 'POST'])
def get_results():
    '''
    Gets fields of submitted query and calls DB API with the query params.

    Returns:
        -results.html page formatted with comments
    '''
    comments = []
    errors = []
    ds = datasource.DataSource()

    if request.method == "POST":
        #get keywords, other comment specs from submitted form
        # **CURRENTLY SUPPORTS SCORE QUERIES ONLY**
        try:
            scoreLow = request.form['scoreLow']
        except:
            pass

        try:
            scoreHigh = request.form['scoreHigh']
        except:
            pass

        if scoreLow and scoreHigh:
            queryResult = ds.getScoreInRange(scoreLow, scoreHigh)
            for x in queryResult:
                comments.append(x)
        elif scoreLow and not scoreHigh:
            queryResult = ds.getScoreAbove(scoreLow)
            for x in queryResult:
                comments.append(x)
        elif scoreHigh and not scoreLow:
            queryResult = ds.getScoreBelow(scoreHigh)
            for x in queryResult:
                comments.append(x)

        try:
             edited = request.form['edited']
             queryResult = ds.getEdited("TRUE")
             for comment in queryResult:
                 if comment in comments:
                     pass
                 else:
                     comments.append(comment)
            #filterEdited(comments)
        except:
            pass
'''
        if edited:
            queryResult = ds.getEdited("TRUE")
            for comment in queryResult:
                if comment in comments:
                    pass
                else:
                    comments.append(comment)
        else:
            queryResult = ds.getEdited("FALSE")
            for comment in queryResult:
                if comment in comments:
                    pass
                else:
                    comments.append(comment)
'''

        try:
             gilded = request.form['gilded']
             queryResult = ds.getGuilded()
             for comment in queryResult:
                 if comment in comments:
                     pass
                 else:
                     comments.append(comment)
            #filterGilded(comments)
        except:
            pass


        try:
             controversial = request.form['controversial']
             queryResult = ds.getControversial()
             for comment in queryResult:
                 if comment in comments:
                     pass
                 else:
                     comments.append(comment)
            #filterControversial(comments)
        except:
            pass


        try:
             goodSentiment = request.form['goodSentiment']
             queryResult = ds.getSentimentGood()
             for comment in queryResult:
                 if comment in comments:
                     pass
                 else:
                     comments.append(comment)
            #filterForGoodSentiment(comments)
        except:
            pass

        try:
             badSentiment = request.form['badSentiment']
             queryResult = ds.getSentimentBad()
             for comment in queryResult:
                 if comment in comments:
                     pass
                 else:
                     comments.append(comment)
            #filterForBadSentiment(comments)
        except:
            pass

        try:
             keywords = request.form['keywords']
        except:
            pass

        if gilded:
            filterGilded(comments)

        if badSentiment:
            filterForBadSentiment(comments)

        if goodSentiment:
            filterForGoodSentiment(comments)

        if controversial:
            filterControversial(comments)

        if edited:
            filterEdited(comments)

    return render_template('resultsTemplate.html', comments=comments)

def filterForBadSentiment(list):
    for entry in list:
        if entry.getSentiment() > 0:
            list.remove(entry)

def filterForGoodSentiment(list):
    for entry in list:
        if entry.getSentiment() < 0:
            list.remove(entry)

def filterGilded(list):
    for entry in list:
        if entry.getGuilded() != 1:
            list.remove(entry)

def filterEdited(list):
    for entry in list:
        if entry.getEdited() != 'TRUE':
            list.remove(entry)

def filterControversial(list):
    for entry in list:
        if entry.getControversial() != 1:
            list.remove(entry)

@app.route('/', methods = ['GET', 'POST'])
def root():
    '''
    Returns home.html or redirects user to /results based on HTTP request

    Returns:
        -html page
    '''
    #redirect to /results if user submits a query
    if request.method == 'POST':
        return redirect(url_for('results'))
    #else display homepage
    else:
        return render_template('Home.html')


@app.route('/home.html', methods = ['GET'])
def homepage():
        '''
        Returns home.html when requested
        '''
        return render_template('Home.html')


@app.route('/about.html', methods = ['GET'])
def about():
        '''
        Returns about.html when requested
        '''
        return render_template('About.html')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
