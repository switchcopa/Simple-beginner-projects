import random 

while True: 
    choices = ["rock", "paper", "scissors"]
    player = None 
    computer = random.choice(choices)

    while player not in choices:
        player = input("Would you like to choose rock, paper or scissors? ").lower()

    if player == computer:
        print("Player:", player)
        print("Computer:", computer)
        print("Draw!")

    elif player == "rock":
        if computer == "scissors":
            print("Player:", player) 
            print("Computer:", computer)
            print("Player wins!")   
        elif computer == "paper":
            print("Player:", player) 
            print("Computer:", computer)
            print("Computer wins!")

    elif player == "scissors":
        if computer == "rock":
            print("Player:", player) 
            print("Computer:", computer)
            print("Computer wins!")
        elif computer == "paper":
            print("Player:", player) 
            print("Computer:", computer)
            print("Player wins!")

    elif player == "paper":
        if computer == "scissors":
            print("Player:", player) 
            print("Computer:", computer)
            print("Computer wins!")
        elif computer == "rock":
            print("Player:", player) 
            print("Computer:", computer)
            print("Player wins!")
        
    play_again = input("Play again? (y/n)").lower() 
    
    if play_again != "y":
        break
