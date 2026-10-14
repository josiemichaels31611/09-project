import random
import string
import time
import msvcrt
import os
def clear_keyboard_buffer(): 
    """Remove any pending keystrokes from the keyboard buffer.""" 
    while msvcrt.kbhit(): 
        msvcrt.getwch() 
    #msvcrt.kbhit() #checks for waiting keystrokes; msvcrt.getwch() removes one. Call the function after clearing the screen and immediately before accepting the player’s guess: 
level = 1 
def get_answer():
    '''This function gets the string for the player to remember.'''
    return ''.join(random.choices(string.ascii_letters, k=level +3))
    
def run_game():
    '''This function prints the level and string then asks for the player's guess.'''
    global guess, level, answer
    answer = get_answer()
    print(F"""
Level {level}
{answer}""")
    timer= "....."
    for dot in timer:
        print(dot)
        time.sleep(1)
    os.system("cls")
    clear_keyboard_buffer() 
    guess = input("Enter the string you just saw (case insensitive): ") 
    
def check_answer():
    '''This function checks if the guess is correct.'''
    global level
    if guess.lower() == answer.lower():
        print("Good Job!")
        time.sleep(3)
        os.system("cls")
        clear_keyboard_buffer()    
        level +=1
        run_game()
        check_answer()
    else:
        print(f"Answer: {answer} Guess: {guess}")
        results()


def results():
    '''This player prints off the player's results based off of how many levels were completed.'''
    global level
    if level == 1:
          print("You have successfully made it through level 0!")
    elif level == 2 or level == 3:
         print("Wow, did you even understand the game?")
    elif level >= 4 and level <= 7:
         print("Not bad, keep working at it.")
    elif level >= 8:
         print("Nice job! You're a memory master!")

def reset():
    global level
    level = 1             

while True:
    start=input("Enter Q to quit, press other to start the game: ")
    if start.upper() == "Q":
        break
    else:
        run_game()
        check_answer()
        replay=input("Would you like to play again? y/n: ")
        if replay.lower()=="y":
                reset()
                run_game()
                check_answer()
        else:
             break