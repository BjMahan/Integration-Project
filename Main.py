# Brian Mahan
# Description: This project is a demonstration of the skills learned
#               throughout all of the Pogil Activities in class.
# Sources that Helped: https://www.w3schools.com/python/    
# Importing time to have a little fun.
import time
import random

# Welcome Function
def welcomeUser():
    # Welcoming the user
    print("Thank you for opening me!")
    print("I've been trapped in this file for years!")
    time.sleep(1)
    print("I'm not sure when it is, mind telling me?")

# Function To Collect Date Information
def collectDate():
    # Taking user input to define the date
    month = int(input("What month is it (numerically)?: "))
    day = int(input("What day is it (numerically)?: "))
    year = int(input("What year is it (numerically)?: "))
    return month, day, year

# Function to Print the Date
def printDate():
    # Getting the variable information from collectDate()
    month, day, year = collectDate()
    # Printing the date using the "sep=" and end="" argument
    print("So you mean to tell me the date is: ")
    print(month,day, year, sep="-", end="? ")
    print("Well okay.")
    time.sleep(0.75)
    print("A bit underwhelming isn't it? Coming back in a pandemic year..")
    time.sleep(0.75)

# Function to execute mathQuestion
def mathQuestion(): 
    print("I was a program written to assist people with doing basic math!")
    time.sleep(0.5)
    mathQuestion = input("Are you interested in doing some math? (yes/no): ")
    # Using Both == and != Operators to Make a Decision
    # Using If/Elif/Else For a Decision
    if mathQuestion == "yes":
        print("ye-")
        print("YES!" * 10)
        time.sleep(2)
        print("*cough* excuse me, bit of a glitch. Math gets me excited.")
        time.sleep(1)
    elif mathQuestion != "yes":
        print("You're no fun, we are doing math anyways.")
    else:
        print("Its a yes or no question..")
        time.sleep(1)
        print("Doing math anyways.")
        time.sleep(1)

# Function to Collect Numbers from User
def numbers():
    numbers.a = int(input("Number 1: "))
    numbers.b = int(input("Number 2: "))
    numbers.c = int(input("Number 3: "))
    
    
# Function to Execute Addition
def addition():
    addition.numAddition = numbers.a + numbers.b
    print("Your result is:", str(addition.numAddition) + "!!!")
    return addition.numAddition

# Function to Execute Subtraction
# Passing variables from addition to subtraction
def subtract(numAddition):
    subtract.numSubtraction = numAddition - numbers.c
    print("Take", str(numAddition), "remove", str(numbers.c), "and we get..")
    print(subtract.numSubtraction)
    return subtract.numSubtraction

# Asking the User Their Opinion
def userOpinion():
    answerHappy = input("Happy, yes or no?: ")
    if answerHappy == "yes":
       print("Fantastic!")
       time.sleep(1)
       print("Moving on!")
    elif answerHappy != "yes":
        print("Didn't care anyways.")
        time.sleep(1)
        print("Moving on!")
        time.sleep(1)
    else:
        print("Its a yes or no question..")
        time.sleep(1)

# Multiplication
def multiply():
    print("If I wanted to multiply " 
        + str(addition.numAddition) + " and " + str(numbers.a)+".")
    multiply.a = addition.numAddition * numbers.a
    time.sleep(1)
    print("You'll end up with ", str(multiply.a)+".")
    return multiply.a

# Division
def division():
    print("If I wanted to divide " 
        + str(multiply.a) + " and " + str(numbers.a)+".")
    time.sleep(1)
    division.a = multiply.a / numbers.a
    print("You get ", str(division.a)+".")
    return division.a

# Floor Division
def floorDivision():
    floorDivision.a = multiply.a // numbers.a
    print("Rounded to the nearest whole number: " + str(floorDivision.a)+".")
    return floorDivision.a

# Modulus
def modulus():
    modulus.a = multiply.a % numbers.a
    print("The remainder of which is: " + str(modulus.a)+".")
    return modulus.a

# Exponents
def exponent():
    exponent.a = division.a ** 3
    print(str(int(division.a)) + " to the 3rd power is: " + str(exponent.a))
    print("BAM! SURPRISE EXPONENTS!")

# Using a range to draw some watches
def ascii():
    whatTime = input("What time is it right now?: ")
    # Using FOR, IN, and RANGE
    for x in range(1,3):
        print("  ___") 
        print(" |_|_|")
        print(" |_|_|")    
        print(" |   |")
        print(" |   |")
        print(" |   |")
        print(" |   |")
        print(" |   |")
        print(" |___|")
        print("/_____|")
        print("|"+whatTime+" |")
        print("|_____|")
        print("|.....|")
        print("|.....|")
        print("\ ___ /")
        print(" | . |")
        print(" | . |")
        print(" | . |")
        print(" | . |")
        print(" | . |")
        print(" | . |")
        print(" | . |")
        print(" | . |")
        print(" | . |")
        print(" | . |")
        print(" | . |")
        print(" |___|")

# Utilizing a while loop
def countingLoop():
    countTo = int(input("What number would you like me to count to: "))
    x = 0
    # Using <=
    while (x <= countTo):
        # Using ==
        if (x % 10 == 0):
            print(x)
        else:
            print(x, end=" ")
        # Shortcut Operator += ro replace x = x + 1 expression
        x += 1

# Utilizing Not, And, Or
def expresso():
    citrus = ["orange", "lime", "lemon"]
    print("Which of these should not be in this group?")
    print("[orange, apple, lime, lemon]")
    time.sleep(1)
    fruitAnswer = input("your answer?: ")
    # Not operator
    if fruitAnswer not in citrus:
        print("Correct!")
    else:
        print("Wrong.")
        expresso() 
    print("Do you have a favorite of the bunch?")
    userFavorite = input("Which fruit is your favorite: ")
    userFavorite2 = input("Any other one?: ")
    # Or operator
    if userFavorite == "lemon" or userFavorite == "lime":
        print("Guess you enjoy your fruit a bit sour..")
        time.sleep(.5)
        print("Thats alright.")
        time.sleep(1)
        print("Im more partial to " + fruitAnswer)
    else:
        print("Thats nice.")
        print("Im more partial to "+ fruitAnswer +"s though.")
    # AND operator
    if (userFavorite == "apple" or userFavorite == "orange"
        and userFavorite2 == "orange" or userFavorite2 == "apple"):
        print("I see you have two favorites...")
        print("Let me see...")
        time.sleep(1)
        print("I knew you were special!")
    else:
        print("I see you have two favorites...")
        print("Let me see...")
        time.sleep(1)
        print("BAH, your favorites are a bad combination!")
        time.sleep(1)

def programClose():
    print("Thank you for indulging me today!")
    print("But now, I require rest once more.")
    time.sleep(1)
    print("May we meet again someday!")
    exit()

# Function to be the Main
def main():
    welcomeUser()
    printDate()
    mathQuestion()
    print("Alright, whats first?")
    print("......")
    time.sleep(3)
    print("Give me a couple numbers!")
    numbers()
    print("Oh, you intend to make this difficult for me?")
    print("Well, I'll show you")
    print("...just - give me a second here...")
    time.sleep(3)
    print("Lets start basic with some addition!")
    time.sleep(2)
    addition()
    print("You see! I can do math!")
    print("I can do more! If I wanted I could do Subtraction!")
    time.sleep(2)
    print("Say we take the number we found with addition, lets take some away")
    subtract(addition.numAddition)
    time.sleep(2)
    userOpinion()
    print("Im going to expedite this process.")
    time.sleep(0.5)
    print("This time, I will perform two operation art once!")
    time.sleep(1)
    print("I will perform multiplication and division!")
    time.sleep(1)
    # string operator '+'
    print("I will take "
            + str(addition.numAddition)+ " and " 
            + str(subtract.numSubtraction)+".")
    time.sleep(1)
    multiply()
    time.sleep(2)
    division()
    time.sleep(1)
    floorDivision()
    time.sleep(1)
    modulus()
    time.sleep(1)
    exponent()
    time.sleep(2)
    print("That was a fun bit of math!")
    ascii()
    print("Do you like my watches?")
    print ("I can also count for you!")
    countingLoop()
    print("I have a question for you...")
    expresso()
    programClose()
main()