import random
import arts_day_4


# Defining Random_Python's available choices
moves = ['rock', 'paper', 'scissors']

# Importing the arts into their respective variables
rock = arts_day_4.rock
paper = arts_day_4.paper
scissors = arts_day_4.scissors

# Initializing User score and Random_Python score
user_score = 0
comp_score = 0
    
while True:
    print("\n\nWelcome to the python 'Rock' 'Paper' 'Scissors' Championship\nHere you will compete against the Ultimate RPS player, the 'Random_Python'")
    
    # Taking Users input
    user_move = input("Pick your hand:\n").lower()
    # Taking Random_Python's input
    index = random.randint(0, 2)
    comp_move = moves[index]

    # If user chose rock, the possible results
    if user_move == 'rock':
        print(f"\nYou chose rock{rock}")
        if comp_move == 'rock':
            print(f"\nRandom_Python chose rock{rock}")
            print("\nIt's a TIE!")
        elif comp_move == 'paper':
            print(f"\nRandom_Python chose paper{paper}")
            print(f"\n'Rock' loses to 'paper'.\nYou lost against a number generator! Shame on you!")
            comp_score+=1
        elif comp_move == 'scissors':
            print(f"\nRandom_Python chose scissors{scissors}")
            print("\n'Rock' wins against 'Scissors'.\nYou win!")
            user_score+=1

    # If user chose paper, the possible results
    elif user_move == 'paper':
        print(f"\nYou chose paper{paper}")
        if comp_move == 'rock':
            print(f"\nRandom_Python chose rock{rock}")
            print("\n'Paper' wins against 'Rock'.\nYou win!")
            user_score+=1
        elif comp_move == 'paper':
            print(f"\nRandom_Python chose paper{paper}")
            print("\nIt's a TIE!")
        elif comp_move == 'scissors':
            print(f"\nRandom_Python chose scissors{scissors}")
            print("\n'Paper' loses to 'Scissors'.\nYou lost against a number generator! Shame on you!")
            comp_score+=1

    # If user chose scissors, the possible results
    elif user_move == 'scissors':
        print(f"\nYou chose scissors{scissors}")
        if comp_move == 'rock':
            print(f"\nRandom_Python chose rock{rock}")
            print("\n'Scissors' loses against 'Rock'.\nYou lost against a number generator! Shame on you!")
            comp_score+=1
        elif comp_move == 'paper':
            print(f"\nRandom_Python chose paper{paper}")
            print("\n'Scissors' wins agiainst 'Rock'.\nYou win!")
            user_score+=1
        elif comp_move == 'scissors':
            print(f"\nRandom_Python chose scissors{scissors}")
            print("\nIt's a TIE!")
            
    print(f"The score is {user_score}:{comp_score}")

    confirmation = input("\nWould you like to challenge the Random_Python once more.\n").lower()
    if confirmation == 'yes':
        continue
    else:
        break



