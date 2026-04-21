#Project 1
import random


secret_Number= random.randint(1,100)
count=0
guess_Chances = 10


user_Name = input("Hi, what is your name?")
print(f"Hello {user_Name}, welcome to Guessing Game")
user_choice = input("Do you want to play with me? (yes/no) ")
if user_choice == "no" or user_choice == "No":
    print("thank you for your time")
elif user_choice == "yes" or user_choice == "Yes":

    while guess_Chances > 0:
        test_number = int(input("please enter your guess? (range:1-100)"))
        if test_number < secret_Number:
            print(f"your guess {test_number} is too low,Try again")

        elif test_number > secret_Number:
            print(f"your guess {test_number} is too high,Try again")
        else:
            print("Congratulations! you Find it")
            print(f"your guess {test_number} is correct")
            break
        guess_Chances -= 1
        print(f"{guess_Chances} guesses left")
        count+=1
    print("Game Over,thank you for playing")
else:
    print("sorry, I didn't get it")
