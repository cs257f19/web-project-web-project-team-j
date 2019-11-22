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
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

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

    editedBool = False
    controvBool = False
    badSentBool = False
    goodSentBool = False
    gildedBool = False
    keywordBool = False
    maxScoreBool = False
    minScoreBool = False

    if request.method == 'POST':

        # get keywords, other comment specs from submitted form

        try:
            keywords = request.form['keywords']
            queryResult = ds.KeywordSearch(keywords)
            for comment in queryResult:
                if comment in comments:
                    pass
                else:
                    comments.append(comment)
            keywordBool = True
        except:
            pass

        try:
            goodSentiment = request.form['goodSentiment']
            goodSentBool = True
        except:
            pass

        try:
            badSentiment = request.form['badSentiment']
            badSentBool = True
        except:
            pass

        if badSentBool and goodSentBool:
            badSentBool = False
            goodSentBool = False

        elif badSentBool and not goodSentBool:
            queryResult = ds.getSentimentBad()
            for comment in queryResult:
                if comment in comments:
                    pass
                else:
                    comments.append(comment)

        elif goodSentBool and not badSentBool:
            queryResult = ds.getSentimentGood()
            for comment in queryResult:
                if comment in comments:
                    pass
                else:
                    comments.append(comment)

        try:
            scoreLow = request.form['scoreLow']
            if scoreLow != "":
                minScoreBool = True
        except:
            pass

        try:
            scoreHigh = request.form['scoreHigh']
            if scoreHigh != "":
                minScoreBool = True
        except:
            pass

        if minScoreBool and maxScoreBool:
            queryResult = ds.getScoreInRange(scoreLow, scoreHigh)
            for comment in queryResult:
                if comment in comments:
                    pass
                else:
                    comments.append(comment)

        elif minScoreBool and not maxScoreBool:
            queryResult = ds.getScoreAbove(scoreLow)
            for comment in queryResult:
                if comment in comments:
                    pass
                else:
                    comments.append(comment)

        elif maxScoreBool and not minScoreBool:
            queryResult = ds.getScoreBelow(scoreHigh)
            for comment in queryResult:
                if comment in comments:
                    pass
                else:
                    comments.append(comment)

        try:
            edited = request.form['edited']
            queryResult = ds.getEdited('TRUE')
            for comment in queryResult:
                if comment in comments:
                    pass
                else:
                    comments.append(comment)
            editedBool = True
        except:
            pass

        try:
            gilded = request.form['gilded']
            queryResult = ds.getGuilded()
            for comment in queryResult:
                if comment in comments:
                    pass
                else:
                    comments.append(comment)
            gildedBool = True
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
            controvBool = True
        except:
            pass

        print(comments)

        if gildedBool:
            filterGilded(comments)

        if badSentBool:
            filterForBadSentiment(comments)

        if goodSentBool:
            filterForGoodSentiment(comments)

        if controvBool:
            filterControversial(comments)

        if editedBool:
            filterEdited(comments)

        if keywordBool:
            filterForKeywords(comments, keywords)

        if minScoreBool and maxScoreBool:
            filterScore(comments, scoreLow, scoreHigh)

        if minScoreBool and not maxScoreBool:
            filterScore(comments, scoreLow)

        if maxScoreBool and not minScoreBool:
            filterScore(comments, -1000, scoreHigh)

    return render_template('resultsTemplate.html', comments=comments)

def filterForBadSentiment(list):
    for entry in list:
        if entry.getSentiment() > 0:
            print("removed good sent")
            list.remove(entry)

def filterForGoodSentiment(list):
    for entry in list:
        if entry.getSentiment() < 0:
            print("removed good sent")
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

def filterScore(list, scoreMin= -1000, scoreMax=2000):
    for entry in list:
        if (entry.getScore() > int(scoreMax)) or (entry.getScore() < int(scoreMin)):
            list.remove(entry)


def filterForKeywords(list, keywords):
    for entry in list:
        if keywords.lower() not in (entry.getBody()).lower():
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
