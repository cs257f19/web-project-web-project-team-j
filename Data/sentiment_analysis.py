
#from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import datasource

#analyser = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):
    #score = analyser.polarity_scores(sentence)
    #print("{:-<40} {}".format(sentence, str(score)))


db = ds()
cursor = db.connection.cursor()
query = "SELECT * FROM mydata"
cursor.execute(query)
results = cursor.fetchall()
comments = []

with open('comments.txt', 'w') as f:
    for result in results:
        comment = result[6]
        f.write(comment + '\n')
f.close()
