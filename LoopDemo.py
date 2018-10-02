#A loop is a programming structure that can repoeat a section of code.
#A loop can run the same code exactly over and over or with some thought
#It can generate a pattern.

#There are two broad categories of loops.
#Conditional Loops (while): These loop as long as a condition is true.
#Counted Loops (for): These loops use a counter to keep track of how many times the loop has run.

#You can use any loop in any situation, but usually from a design perspective,
#there is a better loop in terms of coding.


#If you know in adance how many times a loop should run, a COUNTED LOOP is better.


#If you don't know how many times a loop should run, CONDITIONAL LOOP is better.

import os
import webbrowser
import sleep
print("****************************")


#A while loop evaluates a condtion when it is first reached.
#If condtion is true, it enters the loop block
word = ""

while len(word) < 6 or word.isalpha() == False:

	word = input("Please enter a word larger than 5 letters: ")
	#Loop block
	if len(word) <6:
		print("You had one job. YOU HAD TO ENTER A WORD LARGER THAN 5 LETTERS AND YOU MESSED IT UP")
		os.system("say Why u gotta be this dumb")

	if (word.isalpha() == False):
		print("THAT AIN'T ONE WORD")


print(word+" is seriously long!")
webbroswer.open("")

	#When we reach the botttom of the block we check the conditin again. If it is true, we go back to the top and runs it again.


	






