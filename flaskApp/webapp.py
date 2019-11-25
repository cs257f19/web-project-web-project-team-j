'''
########################################
#    Flask app for Reddimentary        #
#    CS257                             #
#    Web Team J:                       #
#        @hansonc2, @craigj2, @sayanic #
#                                      #
########################################
'''
#import dependencies
import flask
from flask import render_template, request
import json
import sys
import datasource

#creates a flask app
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

    #initializes booleans for filtering purposes
    badSentBool = False
    goodSentBool = False
    maxScoreBool = False
    minScoreBool = False

    if request.method == 'POST':

        print(request.form)
        # get keywords, other comment specs from submitted form

        #A series of try commands that conditionally execute queries based on user input
        try:
            keywords = request.form['keywords']
            if keywords != "":
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
        #returns everything if both good and bad sentiment are selected
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
        #sets filtering booleans for a score query
        try:
            scoreLow = request.form['scoreLow']
            if scoreLow != '':
                minScoreBool = True
        except:
            pass

        try:
            scoreHigh = request.form['scoreHigh']
            if scoreHigh != '':
                maxScoreBool = True
        except:
            pass
        #begins appending the queries into a comment array 
        if minScoreBool and maxScoreBool:
            queryResult = ds.getScoreInRange(scoreLow, scoreHigh)
            for comment in queryResult:
                if comment in comments:
                    pass
                else:
                    comments.append(comment)

        if minScoreBool and not maxScoreBool:
            queryResult = ds.getScoreAbove(scoreLow)
            for comment in queryResult:
                if comment in comments:
                    pass
                else:
                    comments.append(comment)

        if maxScoreBool and not minScoreBool:
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

        #removes comments that dont fit the query conditions
        Results = filterResults(comments, request.form)
        #comment array is pushed to be rendered
        return render_template('resultsTemplate.html', comments=Results)

def filterResults(comments, form):
    '''
    Takes a comment array and conditionally filters it based on the criteria outlined
    in the user query
    Input: an array of comment objects, and a form request
    output: filtered array of comment objects
    '''
    for field in form.keys():
        #for loop iterates through the fields (query conditions) to check filter criteria
        for comment in comments[:]:
            #for loop iterates through comments and removes accordingly
            if field == 'keywords':
                if field[1] != '':
                    if request.form[field].lower() not in comment.getBody().lower():
                        comments.remove(comment)

            if field == 'edited':
                if comment.getEdited() == 'FALSE':
                    comments.remove(comment)

            if field == 'gilded':
                if comment.getGuilded() == 0:
                    comments.remove(comment)

            if field == 'controversial':
                if comment.getControversiality() == 0:
                    comments.remove(comment)

            if field == 'goodSentiment':
                print("type",type(comment.getSentiment()))
                if float(comment.getSentiment()) < 0:
                    comments.remove(comment)

            if field == 'badSentiment':
                if float(comment.getSentiment()) > 0:
                    comments.remove(comment)

            if field == 'scoreLow':
                if request.form[field] != '':
                    if comment.getScore() < int(request.form[field]):
                        comments.remove(comment)

            if field == 'scoreHigh':
                if request.form[field] != '':
                    if comment.getScore() > int(request.form[field]):
                        comments.remove(comment)


    return comments

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


@app.route('/dataviz.html', methods = ['GET'])
def dataviz():
        '''
        Returns dataviz.html when requested
        '''
        return render_template('dataviz.html')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
