'''
Short python program that appends sentiment for given data
by Chait Sayani, Cole Hanson, James Craig
'''
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import csv
analyser = SentimentIntensityAnalyzer()

#initialize arrays
sentenceArray = []
sentimentArray = []

file = open('comments.txt')

#iterate through lines and calculate sentiments
for line in file:
    fields = line.split('$$$$$')
    for x in fields:
        sentenceArray.append(x)


for sent in sentenceArray:
    sentimentArray.append(analyser.polarity_scores(sent)['compound'])

print(len(sentimentArray))

#write out file
wtr = csv.writer(open('test.csv', 'w'), delimiter=',', lineterminator='\n')

for x in sentimentArray : 
    wtr.writerow ([x])