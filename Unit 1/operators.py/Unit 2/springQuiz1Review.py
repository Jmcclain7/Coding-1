# 4. Create a function that asks a user for their birth year using the input() function and then calculates their age.

def ageCalculator():
    response = input('What is your birth year')
    age = 2025 - int(response)
    print(age) 

ageCalculator()

# 5. What is the difference between a parameter and an argument in a function? Provide an example. Please write your answer in complete sentences as a string data type.

'parameter is placeholder data that goes in the function definition'

'argument is real data that goes into the function call'

def sandwishTray(orderCount):
    # ingredients
    #condiments
    #packaging
    #napkins
    print('you will get' + orderCount + 'sandwich trays')
sandwichTray(3) 


# 6. You have been hired by Target to develop a gift card kiosk app that will alow users to reload their gift cards by a set amount.
# Your program should ask the user to enter a gift card amount followed by the amount they want to add to it.
# Next, your program should calculate the new amount by adding the new added amount to the old balance. 
# Finally, your program should print out a message telling the user "congrats! Your new balance is (the new total) dollars.

def giftCardUpdate():
    currentBalance = input('how much is on your gift card')
    updateAmount = input('how much do you want to add')
    newBalance = int(currentBalance) + int(updateAmount)
    print('you have' + str(newBalance) + "on card")

giftCardUpdate()