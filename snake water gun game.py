import random
import time
computer_score = 0
user_score = 0

if __name__ == '__main__':
    print("Welcome to Game of snake water gun...")
    mylist = ["snake","water", "gun"]
    i=0
    print("Enter your choice from the following \n A. Snake \n B. Water \n C. Gun")
    user_choice = ""
    while(i<10):
        i+=1
        print("\nAttempt Number: " ,i )
        computer_choice =str(random.choices(mylist))
        a = input()
        if a=='A' or a=='a':
            user_choice = "['snake']"
            print("Your choice is snake.")
        elif a=='B' or a=='b':
            user_choice = "['water']"
            print("Your choice is water.")
        elif a=='C' or a=='c':
            user_choice = "['gun']"
            print("Your choice is gun.")
        else:
            print("Print enter valid character")
            i=i-1
            continue
        time.sleep(1)
        if user_choice == "['snake']" and computer_choice== "['water']":      #first choice
            computer_score = computer_score + 1
            print("My Score is now increased to", computer_score)
        elif user_choice =="['water']"and computer_choice == "['gun']":
            computer_score = computer_score + 1
            print("My Score is now increased to", computer_score)
        elif user_choice== "['gun']" and computer_choice =="['snake']":
            computer_score = computer_score + 1
            print("My Score is now increased to", computer_score)
        elif computer_choice == "['gun']" and user_choice == "['snake']":
            user_score = user_score + 1
            print("Your Score is now increased to", user_score)
        elif computer_choice == "['snake']" and user_choice == "['water']":
            user_score = user_score + 1
            print("Your Score is now increased to", user_score)
        elif computer_choice == "['water']" and user_choice =="['gun']":
            user_score = user_score + 1
            print("Your Score is now increased to", user_score)
        elif computer_choice == user_choice:
            print("\nYeah...We have same choices")
            continue

    print("Your score is : " + str(user_score))
    print("Computer score is : " + str(computer_score))
    if user_score > computer_score:
        print("Congrats! You Won")
    elif user_score==computer_score:
        print("game draw")
    else:
        print("Let's have another try")