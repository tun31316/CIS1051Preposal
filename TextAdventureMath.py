import math
import random
import operator #used https://stackoverflow.com/questions/30926323/how-to-do-a-calculation-on-python-with-a-random-operator/30926409
from operator import add, mul, sub
import time


name = input("What is your name? ")
print("The only way you will escape my labrynth is if you can correctly answer all ten of my questions.")
print("Make a mistake", name, "and you will be punished")
print("Make three mistakes or get sent back too far and you will have to restart")
print("")
print("You have 3 options for each question: hard, normal, and easy.")
print("getting a hard question right means you move up 3 rounds")
print("getting a hard question wrong means you go back 3 rounds")
print("getting a normal question right means you move up a round")
print("getting a normal question wrong means you go back a round")
print("getting an easy question right means you move up a round")
print("getting an easy question wrong means you go back 2 rounds")

def Rounds():
    difficulty = input("Please enter a difficulty. (Easy/Normal/Hard)")
    round = 0
    lives = 3
    total_time = 0
    while round < 10:
        if difficulty == "Easy" or difficulty == "easy":
            x = random.randint(1, 20)
            y = random.randint(1, 15)
            n = random.randint(1, 2)
            question = int((x - y)**n)
            start = time.time()
            print("Answer the question", "(", x, "-", y, ")", "^", n)
            value = int(input("Answer:"))
            if value == question:
                end = time.time()
                timeelapsed = end - start
                total_time += timeelapsed
                round += 1
                print("Correct! You move one step closer to escaping. Time taken :", timeelapsed)
                print("Passed round:", round)
                if round > 9:
                    print("You're pretty good! Try a higher difficulty")
                    print("Total time taken is", total_time)
                elif round == 7:
                    print("Wow! You're getting too close!")
                elif round == 9:
                    print("Oh dear only one more")
            else:
                round -= 2
                lives -= 1
                print("Wrong! You move back 2 rounds")
                print("The correct answer was:", question)
                while round < 0 or lives == 0:
                    print("You have lost! You must restart")
                    Rounds()
        elif difficulty == "Normal" or difficulty == "normal":
            x = random.randint(30, 51)
            y = random.randint(15, 31)
            n = random.randint(1, 2)
            operators = {"+": operator.add, "-": operator.sub, "*": operator.mul}
            op = random.choice(["+", "-", "*"])
            question = operators[op](x, y)
            start = time.time()
            print("Answer the question", "(", x, op, y, ")")
            value = int(input("Answer:"))
            if value == question:
                end = time.time()
                timeelapsed = end - start
                total_time += timeelapsed
                round += 1
                print("Correct! You move one step closer to escaping. Time taken :", timeelapsed)
                print("Passed round:", round)
                if round > 9:
                    print("You're pretty good! Try a higher difficulty")
                    print("Total time taken is", total_time)
                elif round == 7:
                    print("Wow! You're getting too close!")
                elif round == 9:
                    print("Zoinks! only one more")
            else:
                round -= 1
                lives -= 1
                print("Wrong! You move back 2 rounds")
                print("The correct answer was:", question)
                while round < 0 or lives == 0:
                    print("You have lost! You must restart")
                    Rounds()
        elif difficulty == "Hard" or difficulty == "hard":
            x = random.randint(51, 75)
            y = random.randint(15, 31)
            n = random.randint(2, 3)
            operators = {"+": operator.add, "-": operator.sub, "*": operator.mul}
            op = random.choice(["+", "-", "*"])
            question = (operators[op](x, y))**n
            start = time.time()
            print("Answer the question", "(", x, op, y, ")", "^", n)
            value = int(input("Answer:"))
            if value == question:
                end = time.time()
                timeelapsed = end - start
                total_time += timeelapsed
                round += 3
                print("Correct! You move one step closer to escaping. Time taken :", timeelapsed)
                print("Passed round:", round)
                if round > 9:
                    print("I'm like 99% sure you used a calculator")
                    print("Total time taken is", total_time)
                elif round == 6:
                    print("Wow! You're getting pretty close!")
                elif round == 9:
                    print("You're solving these yourself right??")
                elif round == 3:
                    print("Can you keep that up?")
            else:
                round -= 3
                lives -= 1
                print("Wrong! You move back 3 rounds")
                print("The correct answer was:", question)
                while round < 0 or lives == 0:
                    print("You have lost! You must restart")
                    Rounds()
        else:
            print("Please enter a valid input")
            Rounds()
    while round > 10:
        print("Wow you actually escaped...Do you wanna try a higher difficulty?")

Rounds()    
