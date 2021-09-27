import random
counter = 0
number = random.randint(0,100)

guess = int(input("Please enter a number: "))
counter+=1
while guess!= number:
    if guess > number:
        print("Too high")

    elif guess < number:
        print('Too low')

    guess = int(input("Please make another guess "))


    counter +=1

print("Correct!\nNumber of trials: ", counter)
