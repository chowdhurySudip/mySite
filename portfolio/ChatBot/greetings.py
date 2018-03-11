from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
import sys

dbpath = os.path.join(os.path.dirname(__file__), 'Database', 'db.sqlite3')
# print(dbpath)
if not os.path.exists(dbpath):
	print("No Database FOund!")
	sys.exit(1)

print("Database Found")
greet = ChatBot("GreetingsBot", database=dbpath, read_only=True)

def get_response(req):
	return str(greet.get_response(req))
