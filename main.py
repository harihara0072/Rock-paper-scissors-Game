#Importing the random library to choose value randomly
import random

#asking the user to enter his/her choice
user_choice = input("Enter your choice:").lower()

#checking if it is valid choice
if user_choice in ["rock", "paper", "scissors"]:
    
    #taking a number randomly between 0, 1, 2 and assigning the respective option.
    random_num = random.randint(0, 2)
    if random_num == 0:
        computer_choice = "rock"
    elif random_num == 1:
        computer_choice = "paper"
    else:
        computer_choice = "scissors"
    
    #Creating a dictionary with all the possible cases
    result = {"rock":["paper", False, "scissors", True], "paper":["rock", True, "scissors", False], "scissors":["rock", False, "paper", True] }
    
    #If the users choice is equal to the computers choice then its a tie
    if user_choice == computer_choice:
        print(f'computer chooses: {computer_choice}')
        print("User and computer tie!")
    
    
    else:
        
        #Checking the result from the dictinary created earlier
        temp = result[user_choice]
        
        #checking the value is true/False
        if temp[temp.index(computer_choice) + 1]:
            print(f'computer chooses: {computer_choice}')
            print("You, the user, win! ")
        else:
            print(f'computer chooses: {computer_choice}')
            print("I, the computer, win!")

#When the user enter a invalid choice asking to enter a valid choice.            
else:
    print("Enter a valid choice")
