#Text to Speech

import os

while (True):
	statement = input("What would you like me to say: ")
	os.system("say " + statement)

	
	if statement == 'stop':
		break