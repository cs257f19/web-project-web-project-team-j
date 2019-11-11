

class Comment():

    def __init__(self):
        self.subreddit = ""
        self.subreddit_ID = ""
        self.author = ""
        self.score = 0
        self.stickied = ""
        self.link_ID = ""
        self.body = ""
        self.contoversiality = 0
        self.retrieved_on = 0
        self.edited = ""
        self.ID = ""
        self.guilded = 0
        self.parent_ID = ""
        self.created_UTC = 0
        self.sentiment = 0

    def __str__(self):
        return str(self.score)

    def getAuthor(self):
        '''
        Retrieves the author of a comment

		Returns:
			author of the comment (str)
        '''
        return self.author

    def setAuthor(self, author):
        '''
        sets the author of a comment

        Parameters:
            author - the author of the comment
        '''
        self.author = author

    def getScore(self):
        '''
        Retrieves the score of a comment

		Returns:
			score of the comment (int)
        '''
        return self.score

    def setScore(self, score):
        '''
        sets the score of a comment

        Parameters:
            score - the score of the comment
        '''
        self.score = score

    def getBody(self):
        '''
        Retrieves the body(text) of a comment

		Returns:
			body of the comment (str)
        '''
        return self.body

    def setBody(self, body):
        '''
        sets the body(text) of a comment

        Parameters:
            body - the body of the comment
        '''
        self.body = body

    def getControversiality(self):
        '''
        Retrieves the controversiality of a comment

		Returns:
			controversiality of the comment (int)
        '''
        return self.controversiality

    def setControversiality(self, controversiality):
        '''
        sets the controversiality of a comment

        Parameters:
            controversiality - the controversiality of the comment (int)
        '''
        self.controversiality = controversiality

    def getEdited(self):
        '''
        Retrieves the edited status of a comment

		Returns:
			edited status of a comment ('TRUE'/'FALSE')
        '''
        return self.edited

    def setEdited(self, edited):
        '''
        sets the edited status of a comment

        Parameters:
            edited - the edited status of the comment ('TRUE'/'FALSE')
        '''
        self.edited = edited

    def getGuilded(self):
        '''
        Retrieves the guilded status of a comment

		Returns:
			guilded status of the comment (int)
        '''
        return self.guilded

    def setGuilded(self, guilded):
        '''
        sets the guilded status of a comment

        Parameters:
            guilded - the guilded status of the comment
        '''
        self.guilded = guilded


    def getTimeCreated(self):
        '''
        Retrieves the time a comment was created in UTC

		Returns:
			The time a comment was created (int)
        '''
        return self.created_UTC

    def setTimeCreated(self, time):
        '''
        sets the guilded status of a comment

        Parameters:
            time - the time a comment was created
        '''
        self.created_UTC = time


    def getSentiment(self):
        '''
        Retrieves the sentiment score (-1,1) of a comment

		Returns:
			The sentiment score of a comment (float)
        '''
        return self.sentiment

    def setTimeCreated(self, sentimentScore):
        '''
        sets the sentiment score of a comment

        Parameters:
            sentimentScore - sentiment score of a comment (from -1 to 1)
        '''
        self.sentiment = sentimentScore
