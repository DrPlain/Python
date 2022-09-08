import random

#Defining functions
def get_choices():
    #Getting input
    player_choice = input("Enter a choice(rock, paper, scissors): ")

    #Declaring a list
    comp_options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(comp_options)

    #Declaring a dictionary
    choices = {"player": player_choice, "computer": computer_choice}

    return choices

def check_win(player, computer):
    print(f"You chose {player} and computer chose {computer}") #using f string to concatenate
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "paper":
            return "Paper covers rock. You lose"
        else:
            return "Rock smashes scissors. You won!"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock. You won!"
        else:
            return  "Scissors cuts paper. You lose"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper. You won!"
        else:
            return "Rock smashes scissors. You lose"
    else:
        return "Oops! You entered an invalid choice"

choices = get_choices()

#Accessing a dictionary
result = check_win(choices["player"], choices["computer"])
print(result)

