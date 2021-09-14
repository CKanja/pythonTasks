print("Welcome to the number game!")
num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number "))
operation = input("Choose an operation: addition, subtraction, division, multiplication, modulus: ")

guess = int(input("Before we calculate the answer for you, what do you think the answer is? #QuickMaths: "))

def checkAnswer(answer,guess):
    if answer == guess:
        print ("well done!")
    else:
        print ("try again!")

if operation.lower() == "addition":
    answer = num1 + num2
    checkAnswer(answer,guess)

elif operation.lower() == "subtraction":
    answer = num1 - num2
    checkAnswer(answer,guess)

elif operation.lower() == "division":
    answer = num1 / num2
    checkAnswer(answer,guess)

elif operation.lower() == "multiplication":
    answer = num1 * num2
    checkAnswer(answer,guess)

elif operation.lower() == "modulus":
    answer = num1 % num2
    checkAnswer(answer,guess)

else:
    print("kindly read instructions")