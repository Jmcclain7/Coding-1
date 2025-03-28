# create a clone function where data that is passed in will be opied and then printed out

def cloneMachine(name):
    print('this is the original: '+ name)
    print('this is the clone: '+ name)

cloneMachine('Rob')

def cloneMachine(number):
    result= str(number)
    print('original number is: '+ result)
    print(2 * number)

cloneMachine(8)

def email(emailAddress, password):
    captcha = 'aseoep'

    if emailAddress and password:
        print('great you have access')
    if captcha == captcha:
        ('2 step complete')
    else:
        print('you cannot enter')

email('Rob','eiofeiwoj')

# 1. Create a function to find the area of a rectangle

height = 14
width = 24

def area(height, width):
    print(height * width)

area(13, 24)

# 2. Create a function that will find the payment amount for a loan with interest

#Honda Civic 24000
# 5 years
# 6.5% interest rate
def paymentAmount(principal, rate, time):
    totalRate = principal/rate
    totalPrincipal = principal + totalRate
    monthlyPayment = totalPrincipal/time
    print(monthlyPayment)

paymentAmount(24000, 6.5, 60)



# 1. Fix the function below so that it will print out the age value properly.

def printAge(age):
    print('I am '+  age + ' years old.')

printAge(str(10))

# 2. Fix the function below so that the 
# when it will print the result value properly.
def multiplyValues():
    num1 = input('Please enter a number: 78')
    num2 = input('Please enter another number: 2')
    print(int(num1) * int(num2))
    
multiplyValues()  

# 3. Create a function that will 
# count the number of characters in a string. 
# You will need to use the Python count() function 
# to accomplish this. 

# 4. Create a function that will convert hours into minutes. 
# Your function should take in 1 parameter that will represent 
# the hour and your function should calculate and return 
# how many minutes are in that amount of time. 