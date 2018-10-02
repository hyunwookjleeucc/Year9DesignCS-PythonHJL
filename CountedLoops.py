
#When we think of a for loop, I want to think about
#Count: The variable that holds the current count
#Check: The check that is done each time the loop runs
#Cjange: The change applied to the count each time the loop runs

import webbrowser as web

print("*********************")

for i in range(-44, 137, 1):
	print(i)
	if (i %2 == 0):
		print(str(i)+" is even")
	else:
		print(str(i)+"is odd")
		web.open("https://www.youtube.com/watch?v=zEpB4aNHllA")
		












