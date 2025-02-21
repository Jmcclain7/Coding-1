# 1. Which phython operator would you use if you were 
# developing a shopping application and wanted to get the 
# sum of all items in a person's shopping cart?

# Arithmatic Operator
# getting the total checkout amount for items in a cart
bookbag= 20.00
pens= 10.00
notebooks= 10.00
coffeMug= 20.00

total = bookbag + pens + notebooks + coffeeMug
print(total)

# 3. Which python operator would you use if you wanted to 
# determine if a user is old enough to
#purchase a video game?

# Comparision operator
# checking if someone is old enough to buy game

age = 14
ageToBuy = 17

print(age >= ageToBuy)

# 3. Boys Latin has asked you to develop a program to track
# students who are eligable to attend the spring college 
# tour feild trip. The school would like to the program
# check each students's ID and do the following: check if 
# the student has taken the coding 1 programming class,
# and the students grade level. If the student has taken
# the coding class and is in the 12th grade, they may go on
# the trip. If the student's ID does not meet this condition
# they cannot attend the trip
# logical operator
#we need to check if the student is in 12 AND has taken 
# coding class.

studentGrade = 11
studentHasTakenCode = True

print(studentGrade == 12 and studentHasTakenCode == True)

number=203
print(str) (number)

number=205
print(str) (number)

number=450
print(str) (number) 

Input - is a speacial keyword that lets us pass data into our program.(this function will always turn the text you pass into a string data type)

Let x = *welcome to coding*
Let y = input(*what is your name?)
print(x+y)

Datacasting - is a family of built-in function(or special keywords),that allow us to change a data type from one thing to another.__annotations__

4 primary data casting function

str() - changes a data type into a string.
int() - changes a data into a integer.
float() - changes a data type into a float.
bool() - changes a data type into a boolean
Ex: a =34
b+int(input)(205)
print(a+b)

Print - the print function is a speacial keyword that allows us to pass data inside the round brackets and display it in our terminal.list

x = * welcome to phython coding*
print(x)

Common types of errors 
Syntax error: there was an issue with how you wrote a coding symbol or you wrote you code out of order- such as operators, brackets, etc
Name Error: There was an error with the name of a variable our function; could be misspelling
Type Error: There was an issue with data type you are trying to use; such as combining a sting with an trigger.
Indentation Error: There was an issue with you spaced out lines in a function.
Index Error: You are trying to access a piece of data that does not excist in a list.