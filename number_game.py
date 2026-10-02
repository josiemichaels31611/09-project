import random
def  set_range():
    '''this sets the min and max from user input'''
    global min, max
    min = input("Min: ")
    max = input("Max: ")
    while min.isdigit() == False:
        min = input("Min: ")
    while max.isdigit() == False:
        max = input("Max: ")
    if min >= max:
        print("Error Min >= Max")
        max = input("Max: ")
    while max.isdigit() == False:
        max = input("Max: ")
    min = int(min)
    max = int(max)
 

set_range()
target = random.randint(min,max)
Comp_count = []
Player_count = []
comp_max = max
comp_min = min
comp_guess = (comp_max + comp_min) // 2
Comp_range = []
another_round = True


def comp_play():
    '''This function finds the number directly in half of an updated min and max'''
    global comp_guess, comp_max, comp_min, comp_replay
    if target < comp_guess:
        Comp_count.append(comp_guess)
        comp_max = comp_guess - 1
        comp_guess = (comp_max + comp_min) // 2
        comp_replay = True
    elif target > comp_guess:
        Comp_count.append(comp_guess)
        comp_min = comp_guess + 1
        comp_guess = (comp_max + comp_min) // 2
        comp_replay = True
    else:
        Comp_count.append(comp_guess)
        print("Computer Search done")
        comp_replay = False
        return
def player_int():
        global player_guess
        player_guess = input("Enter Guess: ")
        while player_guess.isnumeric() == False: #---Maybe make function to return a int if it is a string
            player_guess = input("Enter Guess: ")

def player():
    '''This function tells the user lower or higher and handles weather player guessed the target'''
    player_int()
    player_guess = int(player_guess)
    while player_guess > max or player_guess < min: #constantly runs so when
        print("error")
        player_guess = int(input("Enter a guess: "))
    if player_guess == target:
        print("Done") #------------------------Player got target
        Player_count.append(player_guess)
    else:
        if player_guess > target:
            print("Lower")
            Player_count.append(player_guess)
        elif player_guess < target:
            print("higher")
            Player_count.append(player_guess)
comp_replay = False
player_replay = False
def print_results():
    '''Prints the results'''
    if len(Player_count) < len(Comp_count):
        winner = "Player"
    if len(Player_count) > len(Comp_count):
        winner = "Computer"
    if len(Player_count) == len(Comp_count):
        winner = "Tie"
    print(f"""
=========FINAL RESULTS=========

Player Guesses:
{Player_count}
Player Guess Count:{len(Player_count)}

Computer Guesses:
{Comp_count}
Player Guess Count:{len(Comp_count)}

Winner: {winner}
""")
def reset():
    '''This function resets the variables'''
    global comp_min,comp_max,Player_count, Comp_count, player_guess, comp_guess
    comp_min = min
    comp_max = max
    Player_count = []
    Comp_count = []
    player_guess = None
    comp_guess = (comp_max + comp_min) // 2

while True:
    target = random.randint(min,max)
    player_int()
    player()
    comp_replay = True
    while comp_replay == True:
        comp_play()
    while player_guess != target:
        player_int()
        player()
    print_results()
    player_input = input("Another round?(y for yes, other for no): ").strip().lower()
    if player_input != "y":
        break
    reset()
    set_range()