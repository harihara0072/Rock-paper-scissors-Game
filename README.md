# Rock-paper-scissors-Game


 “Rock-paper-scissors is a hand game that is played by two people.
The players count to three in unison and simultaneously "throw" one of three
hand signals that correspond to rock, paper or scissors. The winner is
determined by the rules:
• Rock smashes scissors
• Scissors cuts paper

 Python program to ask the user’s choice of Rock paper scissors. The
program then, randomly, chooses a choice for itself (the computer) and then
compares it with the user’s choice. The final output should show, the user’s
choice, the program’s choice and the winner.

Algorithm:

1. The program asks the user to enter his choice and and verify if that is a valid option or not. 
2. The program will generate a number randomly between 0-2 and assign the option as follows:
       0- Rock, 1- Paper, 2- Scissors
3. Then it uses the results dictionary, where the keys are user_choices and the values are a list of all the other possible
   choices and who wins the game(True/False) in the next index, to find the result of the game by searching for the computer 
   option in that list.
4. If it is true then the user wins the game and False when losses. 
5. Then it will print all the details of result. 

Steps to execute:
1. Run the next three cells to run the program. 

Expected Output:

1. When the users choice is "rock" and based on the computers choice it will print the output.
2. If the users any other value apart from Rock, Paper, Scissors then the program prints saying to enter a valid option.
    
