import random, time 

word_bank = {
    "easy": [
        "dog", "cat", "code", "tree", "game", "book", "fish", "star", "frog", "blue",
        "fire", "rock", "ship", "moon", "rain", "milk", "wind", "wave", "leaf", "gold"
    ],
    "medium": [
        "python", "banana", "castle", "forest", "rocket", "planet", "guitar", "island", "school", "animal",
        "zombie", "camera", "glitch", "hunter", "blaster", "monster", "jungle", "script", "desert", "pirate"
    ],
    "hard": [
        "keyboard", "computer", "dinosaur", "volcano", "triangle", "dragonfly", "treasure", "fireball", "vampires", "backpack",
        "mountain", "lightning", "airplane", "sandstorm", "grappling", "wilderness", "astronaut", "darkness", "builder", "internet"
    ],
    "expert": [
        "spaceship", "earthquake", "blacksmith", "underworld", "blueprints", "storyboard", "microphone", "controller", "screenshot", "moonlight",
        "watermelon", "graveyards", "explosions", "programmer", "soundtrack", "battlezone", "campground", "rollercoast", "mechanical", "powerplant"
    ],
    "impossible": [
        "extraordinary", "teleportation", "multiplication", "transformation", "entertainment", "implementation", "infrastructure",
        "responsibility", "revolutionary", "misunderstood", "characterized", "unpredictable", "communication", "overconfident",
        "miscalculation", "consciousness", "synchronizing", "reconstruction", "imprisonment", "impossibility"
    ]
}

Hangman_phases = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

coins = 0 

print("       🔥🎮 Welcome to Hangman! 🎮🔥        ")

play = str(input("Would you like to play 🎲? (y/n) ")).lower()
if play in ["yes", "ye", "y"]:
    while True:
        difficulty = input("Select your difficulty: (easy, medium, hard, expert, impossible)  ").lower()
        
        if difficulty in word_bank:
            word = random.choice(word_bank[difficulty])
            board = ["_"] * len(word)
            letters = list(word)

            phase = 0 
            current_phase = Hangman_phases[phase]
            print(current_phase)
            
            print(" ".join(board))

            while True:
                found = False

                guess = input("\nNow guess a letter 😈   ").lower()
                time.sleep(1)
                
                for index, letter in enumerate(letters):
                    if letter == guess:
                        found = True
                        board[index] = letter

                if found == True:
                    print(" ".join(board), "♦️  You guessed right!  ♦️")
                else:
                    print("Wrong! 😟  ")
                    phase += 1 
                    current_phase = Hangman_phases[phase]
                    print(current_phase)
                
                if current_phase == Hangman_phases[-1]:
                    print("You fucking lost hahaaaaa HE'S DEAD NOW!")
                    break

                if not "_" in board:
                    print("\nYOU WON LET'S GOOOO")
                    print("HERE'S 100 COINS JUST FOR YOU")
                    coins += 100 
                    print("Your coins:", coins)
                    break

            play_again = input("\nWould you like to play again? (y/n)  ").lower()
            if not play_again in ["yes", "ye", "y"]:
                print("Have a good day!")
                break            
            
               
else:
    print("Well then screw you!")
