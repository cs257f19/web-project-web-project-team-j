import psycopg2
import getpass
from comment import *

class DataSource:

	def __init__(self):
		self.connection = psycopg2.connect(dbname = 'sayanic', user = 'sayanic', password = 'green299sunshine')

	def connector(self,user, password):
		'''
		Establishes a connection to the database with the following credentials:
			user - username (also the name of the database)
			password - the passsword for this database on perlman

		Returns: a database connection

		Note: exits if a connection is not established
		'''
		try:
			self.connection = psycopg2.connect(dbname = user, user = user, password = password)
		except Exception as e:
			print('Connection Error',e)
			exit()
		return self.connection

	def getScoreAbove(self,score):
		'''
		Retrieves all comments with a score greater than the specified score

		Parameters:
			connection- the connection to the database
			score - get all comments from the data with a score greater than this score

		Returns:
			A collection of comments with scores above the specified score, or None if the query fails
		'''
		try:
			cursor = self.connection.cursor()
			query = "SELECT * FROM mydata WHERE score > " + str(score) + "ORDER BY score DESC"
			cursor.execute(query)
			results = cursor.fetchall()

			# construct comment objects from the query
			comments = []
			for result in results:
				#instantiate new comment object
				comment = Comment()

				# set fields of comment object
				comment.setAuthor(result[2])
				comment.setScore(result[3])
				comment.setBody(result[6])
				comment.setBody(result[6])
				comment.setControversiality(result[7])
				comment.setEdited(result[9])
				comment.setGuilded(result[11])
				comment.setTimeCreated(result[13])


				comments.append(comment)

			#return list of comment objects
			return comments

		except Exception as e:
			print("Uh oh, something went wrong",e)
			return None

	def getScoreBelow(self, score):
		'''
		Retrieves all comments with a score less than the specified score

		Parameters:
			connection- the connection to the database
			score - get all comments from the data with a score lesser than this score

		Returns:
			A collection of all comments with scores below the specified score, or None if the query fails
		'''
		try:
			cursor = self.connection.cursor()
			query = "SELECT * FROM mydata WHERE score < " + str(score) + "ORDER BY score DESC"
			cursor.execute(query)
			results = cursor.fetchall()

			# construct comment objects from the query
			comments = []
			for result in results:
				#instantiate new comment object
				comment = Comment()

				# set fields of comment object
				comment.setAuthor(result[2])
				comment.setScore(result[3])
				comment.setBody(result[6])
				comment.setBody(result[6])
				comment.setControversiality(result[7])
				comment.setEdited(result[9])
				comment.setGuilded(result[11])
				comment.setTimeCreated(result[13])


				comments.append(comment)

			#return list of comment objects
			return comments

		except Exception as e:
			print("Uh oh, something went wrong",e)
			return None

	def getScoreInRange(self,start,end):
		'''
		Retrieves all comments with a score between the start and end bounds

		Parameters:
			connection- the connection to the database
			start - get all comments with scores greater than this score (and less than 'end' score)
			end -  get all comments with scores lesser than this score (and greater than the 'start' score)

		Returns:
			A collection of all comments with scores between the specified bounds, or None if the query fails
		'''
		try:
			cursor = self.connection.cursor()
			query = "SELECT * FROM mydata WHERE score BETWEEN " + str(start) + " AND " + str(end)
			cursor.execute(query)
			results = cursor.fetchall()

			# construct comment objects from the query
			comments = []
			for result in results:
				#instantiate new comment object
				comment = Comment()

				# set fields of comment object
				comment.setAuthor(result[2])
				comment.setScore(result[3])
				comment.setBody(result[6])
				comment.setBody(result[6])
				comment.setControversiality(result[7])
				comment.setEdited(result[9])
				comment.setGuilded(result[11])
				comment.setTimeCreated(result[13])


				comments.append(comment)

			#return list of comment objects
			return comments

		except Exception as e:
			print("Uh oh, something went wrong",e)
			return None

	def getGuilded(self):
		try:
			cursor = self.connection.cursor()
			query = "SELECT * FROM mydata WHERE gilded=1"
			cursor.execute(query)
			results = cursor.fetchall()

			# construct comment objects from the query
			comments = []
			for result in results:
				#instantiate new comment object
				comment = Comment()

				# set fields of comment object
				comment.setAuthor(result[2])
				comment.setScore(result[3])
				comment.setBody(result[6])
				comment.setBody(result[6])
				comment.setControversiality(result[7])
				comment.setEdited(result[9])
				comment.setGuilded(result[11])
				comment.setTimeCreated(result[13])


				comments.append(comment)

			#return list of comment objects
			return comments

		except Exception as e:
			raise e
			return None

	def getControversial(self):
		'''
		Retrieves all comments with a controversial flag

		Parameters:
			connection- the connection to the database

		Returns:
			A collection of all comments with controversial flags
		'''
		try:
			cursor = self.connection.cursor()
			query = "SELECT * FROM mydata WHERE controversiality=1"
			cursor.execute(query)
			results = cursor.fetchall()

			# construct comment objects from the query
			comments = []
			for result in results:
				#instantiate new comment object
				comment = Comment()

				# set fields of comment object
				comment.setAuthor(result[2])
				comment.setScore(result[3])
				comment.setBody(result[6])
				comment.setBody(result[6])
				comment.setControversiality(result[7])
				comment.setEdited(result[9])
				comment.setGuilded(result[11])
				comment.setTimeCreated(result[13])


				comments.append(comment)

			#return list of comment objects
			return comments

		except Exception as e:
			print("Uh oh, something went wrong",e)
			return None

	def KeywordSearch(self):
		'''
		Retrieves all comments with a comment body that contains the specified keyword

		Parameters:
			connection- the connection to the database
			keyword- get all comments with a comment body that contains this keyword

		Returns:
			A collection of all comments that contain the keyword
		'''
		pass

	def getSentimentGood(self):
		'''
		Retrieves all comments with a bad sentiment

		Returns:
			A collection of all comments with 'good' sentiment, or None if the query fails
		'''
		pass

	def getSentimentBad(self):
		'''
		Retrieves all comments with a good sentiment

		Returns:
			A collection of all comments with 'bad' sentiment, or None if the query fails
		'''
		pass

	def visualizeSentiment(self):
		pass

	def getEdited(self,input):
		if input == 'TRUE':
			cursor = self.connection.cursor()
			query = "SELECT * FROM mydata WHERE edited='TRUE'"
			cursor.execute(query)
			results = cursor.fetchall()

			# construct comment objects from the query
			comments = []
			for result in results:
				#instantiate new comment object
				comment = Comment()

				# set fields of comment object
				comment.setAuthor(result[2])
				comment.setScore(result[3])
				comment.setBody(result[6])
				comment.setBody(result[6])
				comment.setControversiality(result[7])
				comment.setEdited(result[9])
				comment.setGuilded(result[11])
				comment.setTimeCreated(result[13])


				comments.append(comment)

			#return list of comment objects
			return comments

		elif input == 'FALSE':
			cursor = self.connection.cursor()
			query = "SELECT * FROM mydata WHERE edited='FALSE'"
			cursor.execute(query)
			results = cursor.fetchall()

			# construct comment objects from the query
			comments = []
			for result in results:
				#instantiate new comment object
				comment = Comment()

				# set fields of comment object
				comment.setAuthor(result[2])
				comment.setScore(result[3])
				comment.setBody(result[6])
				comment.setBody(result[6])
				comment.setControversiality(result[7])
				comment.setEdited(result[9])
				comment.setGuilded(result[11])
				comment.setTimeCreated(result[13])


				comments.append(comment)

			#return list of comment objects
			return comments

		else:
			print("Uh oh, something went wrong")
			return None


def main():

	ds = DataSource()

	user = 'sayanic'
	password = 'green299sunshine'

	connection = ds.connector(user,password)
	#results = ds.getControversial(connection)
	results = ds.getScoreInRange(connection,2,10)

	#if results is not None:
		#print('results')
		#for item in results:
			#print(item)
	connection.close()
if __name__ == "__main__":
	main()
