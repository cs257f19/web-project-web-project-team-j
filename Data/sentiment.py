from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import csv
analyser = SentimentIntensityAnalyzer()

sentenceArray = []
sentimentArray = []

file = open('comments.txt')

for line in file:
    fields = line.split('$$$$$')
    for x in fields:
        sentenceArray.append(x)

#print(len(sentenceArray))
#print(sentenceArray[0])

for sent in sentenceArray:
    #print(analyser.polarity_scores(sent))
    #print(analyser.polarity_scores(sent)['compound'])
    sentimentArray.append(analyser.polarity_scores(sent)['compound'])

print(len(sentimentArray))

#resultfile = open("C:\Users\csWork\Classes\sentiment_webProj",'wb')
#wr = csv.writer(resultfile)

wtr = csv.writer(open('test.csv', 'w'), delimiter=',', lineterminator='\n')

for x in sentimentArray : 
    wtr.writerow ([x])