#Text to Speech with stopping option

import os

while (True):
	statement = input("What would you like me to say (type stop to stop the program): ")
	os.system("say " + statement)

	
	if statement == 'stop':
		break


print("End Program, have a nice day.")