#This file will go through the basics of string manipulation

#Strings are collectison of characters

#Strings are closed in "" or ''

# "Justin"
# "Paul is cold"
# "Paul is cool!"

#Two things we need to talk about when we think of strings
#index- Always starts at 0

#length

#Example
#  0123    012345
# "Paul"  "Monkey"

#len("Paul") = 4

#len("Monkey") = 6

name = "Justin"

print(name) # I can print strings

sentence = name + " is human" #concatination is adding strings
print(sentence)

# I can access specific letters

fLetter = name [0] #name at 0
print(fLetter)
letters1 = name [0:2] #inclusive:exclusive
print(letters1)

letters2 = name [2:]
print(letters2)

letters2a = name [2:len(name)] #formal way of writing letters2
print(letters2a)

letters3 = name [:2]
print(letters3)

lname = len(name) #Length of string
print(lname)

# if I want to print out all letters

for i in range(len(name)):
	print(name[i])


