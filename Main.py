"""My Integration Program for COP1500"""
import time

__author__ = "Brian Mahan"
# Brian Mahan
"""
    Description: This project is a demonstration of the skills learned
               throughout all of the Pogil Activities in class.
               
    Sources that Helped: https://www.w3schools.com/python/ 
    
    Github Link:
        https://github.com/BjMahan/Integration-Project
"""


# Welcome Function
def welcome_user():
    """The purpose of this function is to welcome the user to the program."""
    # Welcoming the user
    print("Thank you for opening me!")
    print("I've been trapped in this file for years!")
    time.sleep(1)
    print("I'm not sure when it is, mind telling me?")


# Function To Collect Date Information
def collect_month():
    """
    Collects the month from the user

    month - Current month (ex: 7 or 07)
    """
    # Taking user input to define the date
    input_is_invalid = True
    while input_is_invalid:
        try:
            month = int(input("What month is it (numerically)?: "))
            input_is_invalid = False
            return month
        except ValueError:
            print("Error. Must be a whole number.")


def collect_day():
    """
    Collects the day from the user

    day - Current day (ex: 7 or 07)
    """
    input_is_invalid = True
    while input_is_invalid:
        try:
            day = int(input("What day is it (numerically)?: "))
            input_is_invalid = False
            return day
        except ValueError:
            print("Error. Must be a whole number.")


def collect_year():
    """
    Collects the year from the user

    year - Current year (ex: 2021)
    """
    input_is_invalid = True
    while input_is_invalid:
        try:
            year = int(input("What year is it (numerically)?: "))
            input_is_invalid = False
            return year
        except ValueError:
            print("Error. Must be a whole number.")


# Function to Print the Date
def print_date():
    """
    The purpose of this function is to present
    the date back to the user in a fun manner.
    """
    # Getting the variable information from collectDate()
    month = collect_month()
    day = collect_day()
    year = collect_year()
    # Printing the date using the "sep=" and end="" argument
    print("So you mean to tell me the date is: ")
    print(month, day, year, sep="-", end="? ")
    print("Well okay.")
    time.sleep(0.75)
    print("A bit underwhelming isn't it? Coming back in a pandemic year..")
    time.sleep(0.75)


# Function to execute mathQuestion
def math_question():
    """
    The purpose of this function is to ask
    if the user wants to do some math and respond in kind.
    """

    print("I was a program written to assist people with doing basic math!")
    time.sleep(0.5)
    math_q = input("Are you interested in doing some math?"
                   " (""yes/no): ")
    # Using Both == and != Operators to Make a Decision
    # Using If/Elif/Else For a Decision
    if math_q == "yes":
        print("ye-")
        print("YES!" * 10)
        time.sleep(2)
        print("*cough* excuse me, bit of a glitch. Math gets me excited.")
        time.sleep(1)
    elif math_q != "yes":
        print("You're no fun, we are doing math anyways.")
    else:
        print("Its a yes or no question..")
        time.sleep(1)
        print("Doing math anyways.")
        time.sleep(1)


# Function to Collect Numbers from User
def number1():
    """Asks for a first number"""
    input_is_invalid = True
    while input_is_invalid:
        try:
            number1.a = int(input("Number 1: "))
            input_is_invalid = False
            return number1.a
        except ValueError:
            print("Error. Must be a whole number.")


def number2():
    """Asks for a second number."""
    input_is_invalid = True
    while input_is_invalid:
        try:
            number2.b = int(input("Number 2: "))
            input_is_invalid = False
            return number2.b
        except ValueError:
            print("Error. Must be a whole number.")


def number3():
    """Asks for a third number."""
    input_is_invalid = True
    while input_is_invalid:
        try:
            number3.c = int(input("Number 3: "))
            input_is_invalid = False
            return number3.c
        except ValueError:
            print("Error. Must be a whole number.")


# Function to Execute Addition
def addition():
    """
        The purpose of this function is to perform addition
        returns value generated.
    """
    addition.num_addition = number1.a + number2.b
    print("Your result is:", str(addition.num_addition) + "!!!")
    return addition.num_addition


# Function to Execute Subtraction
# Passing variables from addition to subtraction
def subtract(num_addition):
    """
    The purpose of this function is to perform subtraction using data
    calculated in a previous function
    Returns value generated.
    """
    subtract.num_subtraction = num_addition - number3.c
    print("Take", str(num_addition), "remove", str(number3.c), "and we get..")
    print(subtract.num_subtraction)
    return subtract.num_subtraction


# Asking the User Their Opinion
def user_opinion():
    """
    The purpose of this function is to collect the users opinion.
    answerHappy - yes or no question
    """
    answer_happy = input("Happy, yes or no?: ")
    if answer_happy == "yes":
        print("Fantastic!")
        time.sleep(1)
        print("Moving on!")
    elif answer_happy != "yes":
        print("Didn't care anyways.")
        time.sleep(1)
        print("Moving on!")
        time.sleep(1)
    else:
        print("Its a yes or no question..")
        time.sleep(1)


# Multiplication
def multiply():
    """
    The purpose of this function is to perform multiplication.
    Returns value generated by function.
    """
    print("If I wanted to multiply "
          + str(addition.num_addition) + " and " + str(number1.a) + ".")
    multiply.a = addition.num_addition * number1.a
    time.sleep(1)
    print("You'll end up with ", str(multiply.a) + ".")
    return multiply.a


# Division
def division():
    """
    The purpose of this function is to perform division.
    Returns Value Generated.
    """
    print("If I wanted to divide "
          + str(multiply.a) + " and " + str(number1.a) + ".")
    time.sleep(1)
    division.a = multiply.a / number1.a
    print("You get ", str(division.a) + ".")
    return division.a


# Floor Division
def floor_division():
    """
    The purpose of this function is to perform Floor Division.
    Returns Value Generated.
    """
    floor_division.a = multiply.a // number1.a
    print("Rounded to the nearest whole number: " + str(floor_division.a) +
          ".")
    return floor_division.a


# Modulus
def modulus():
    """
    The purpose of this function is to calculate the modulus.
    Returns Value Generated.
    """
    modulus.a = multiply.a % number1.a
    print("The remainder of which is: " + str(modulus.a) + ".")
    return modulus.a


# Exponents
def exponent():
    """
    The purpose of this function is to demonstrate the ability to find an
    exponent.
    Returns Value Generated.
    Prints an exclamation.
    """
    exponent.a = division.a ** 3
    print(str(int(division.a)) + " to the 3rd power is: " + str(exponent.a))
    print("BAM! SURPRISE EXPONENTS!")


# Using a range to draw some watches
def artwork():
    """
    The purpose of this function is to draw an ASCII art watch with the
    current time given by the user.
    whatTime - Standard or 24 hour format time
    """
    print("I have a watch that can display anything you wish!")
    what_time = input("What should get displayed?: ")
    # Using FOR, IN, and RANGE
    for x in range(1, 3):
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
        print("|" + what_time + " |")
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
def counting_loop_input():
    """
    Takes user input for a future function
    countTo - number chosen by user, integer.
    """

    input_is_invalid = True
    while input_is_invalid:
        try:
            count_to = int(input("What number would you like me to count "
                                 "to: "))
            input_is_invalid = False
            return count_to
        except ValueError:
            print("Error. Must be a whole number.")


def counting_loop():
    """
    Counts up to number specified by user.
    """
    count_to = counting_loop_input()
    x = 0
    # Using <=
    while x <= count_to:
        # Using ==
        if x % 10 == 0:
            print(x)
        else:
            print(x, end=" ")
        # Shortcut Operator += ro replace x = x + 1 expression
        x += 1


# Utilizing Not, And, Or
def expression():
    """
    The purpose of this function is to quiz the user on similar types,
    the 'program's' favorite fruits,
    and respond to the users answers in a realistic manner.
    """
    citrus = ["orange", "lime", "lemon"]
    print("Which of these should not be in this group?")
    print("[orange, apple, lime, lemon]")
    time.sleep(1)
    fruit_answer = input("your answer?: ")
    # Not operator
    if fruit_answer not in citrus:
        print("Correct!")
    else:
        print("Wrong.")
        expression()
    print("Do you have a favorite of the bunch?")
    user_favorite = input("Which fruit is your favorite: ")
    user_favorite2 = input("Any other one?: ")
    # Or operator
    if user_favorite == "lemon" or user_favorite == "lime":
        print("Guess you enjoy your fruit a bit sour..")
        time.sleep(.5)
        print("That's alright.")
        time.sleep(1)
        print("Im more partial to " + fruit_answer)
    else:
        print("That's nice.")
        print("Im more partial to " + fruit_answer + "s though.")
    # AND operator
    if (user_favorite == "apple" or user_favorite == "orange"
            and user_favorite2 == "orange" or user_favorite2 == "apple"):
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


def program_close():
    """
    The purpose of this function is to bid farewell to the user,
    and closes the program.
    """
    print("Thank you for indulging me today!")
    print("But now, I require rest once more.")
    time.sleep(1)
    print("May we meet again someday!")
    exit()


# Function to be the Main
def main():
    """
    The purpose of this function is to run the entire program, calls main.
    Also includes relevant print statements.
    """
    welcome_user()
    print_date()
    math_question()
    print("Alright, whats first?")
    print("......")
    time.sleep(3)
    print("Give me a couple numbers!")
    number1()
    number2()
    number3()
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
    subtract(addition.num_addition)
    time.sleep(2)
    user_opinion()
    print("Im going to expedite this process.")
    time.sleep(0.5)
    print("This time, I will perform two operation art once!")
    time.sleep(1)
    print("I will perform multiplication and division!")
    time.sleep(1)
    # string operator '+'
    print("I will take "
          + str(addition.num_addition) + " and "
          + str(subtract.num_subtraction) + ".")
    time.sleep(1)
    multiply()
    time.sleep(2)
    division()
    time.sleep(1)
    floor_division()
    time.sleep(1)
    modulus()
    time.sleep(1)
    exponent()
    time.sleep(2)
    print("That was a fun bit of math!")
    artwork()
    print("Do you like my watches?")
    print("I can also count for you!")
    counting_loop()
    print("I have a question for you...")
    expression()
    program_close()


if __name__ == "__main__":
    main()
