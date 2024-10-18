from colorama import Fore,Style
import os
from time import sleep
from random import randint, shuffle


# _____                   _             _   _____                          _   
#|_   _|__ _ __ _ __ ___ (_)_ __   __ _| | |  ___|__  _ __ _ __ ___   __ _| |_ 
#  | |/ _ \ '__| '_ ` _ \| | '_ \ / _` | | | |_ / _ \| '__| '_ ` _ \ / _` | __|
#  | |  __/ |  | | | | | | | | | | (_| | | |  _| (_) | |  | | | | | | (_| | |_ 
#  |_|\___|_|  |_| |_| |_|_|_| |_|\__,_|_| |_|  \___/|_|  |_| |_| |_|\__,_|\__|

# A function used in menus to print borders/line breaks
def printBorder(border_width):
    for i in range(0,border_width):
        end = ""
        if i==border_width-1: end = "\n" 
        if i%2 == 0:
            print(Fore.LIGHTRED_EX + "=", end=end)
        else:
            print(Fore.RED + "=", end=end)




# _____ _ _        ___ ___  
#|  ___(_) | ___  |_ _/ _ \ 
#| |_  | | |/ _ \  | | | | |
#|  _| | | |  __/  | | |_| |
#|_|   |_|_|\___| |___\___/ 

def readQuiz(dir):
    # "Week5/Quiz Assignment/Quizes/Python Beginner Quiz.txt"

    with open(dir,"r") as quiz_file:
        return quiz_file.readlines()


#  _   _ ___     
# | | | |_ _|___ 
# | | | || |/ __|
# | |_| || |\__ \
#  \___/|___|___/

# Quiz game menu interface
def menuUI():
    os.system("cls")
    printBorder(33)
    print(Fore.LIGHTRED_EX + "      Quiz Game!" )
    printBorder(33)
    print(Fore.LIGHTRED_EX + "1." + Fore.LIGHTWHITE_EX + " Start Quiz")
    print(Fore.LIGHTRED_EX + "2." + Fore.LIGHTWHITE_EX + " Quit")
    user_input = input(Fore.LIGHTRED_EX + Style.DIM + "\n> " + Style.NORMAL)  # User input
    print(Style.RESET_ALL)
    return user_input

def questionUI(question, options):
    os.system("cls")

    printBorder(33)
    print(Fore.LIGHTRED_EX + "      Quiz Question!" )
    printBorder(33)
    
    # Display the question
    print(Fore.LIGHTWHITE_EX + question + "\n")
    
    # Display the options (assuming 'options' is a list of 4 choices)
    print(Fore.LIGHTRED_EX + "1." + Fore.LIGHTWHITE_EX + " " + options[0])
    print(Fore.LIGHTRED_EX + "2." + Fore.LIGHTWHITE_EX + " " + options[1])
    print(Fore.LIGHTRED_EX + "3." + Fore.LIGHTWHITE_EX + " " + options[2])
    print(Fore.LIGHTRED_EX + "4." + Fore.LIGHTWHITE_EX + " " + options[3])
    
    # Ask for the user's input
    user_input = input(Fore.LIGHTRED_EX + Style.DIM + "\nSelect your answer (1-4): " + Style.NORMAL)
    print(Style.RESET_ALL)
    
    return user_input

def finalScoreUI(score, max_score):
    os.system("cls")

    printBorder(33)
    print(Fore.LIGHTRED_EX + "      The Results!" )
    printBorder(33)
    
    # Display the options (assuming 'options' is a list of 4 choices)
    print(Fore.LIGHTRED_EX + "> " + Fore.LIGHTWHITE_EX + f"You got {score} out of {max_score}")
    
    # Ask for the user's input
    input(Fore.LIGHTRED_EX + Style.DIM + "\n Hit enter to continue" + Style.NORMAL)
    print(Style.RESET_ALL)




#  _                          
# | |    ___   ___  _ __  ___ 
# | |   / _ \ / _ \| '_ \/ __|
# | |__| (_) | (_) | |_) \__ \
# |_____\___/ \___/| .__/|___/
#                  |_|    

def questionLoop(question_info):
    question = question_info[0]
    right_answer = question_info[1]
    mutliple_choice = question_info[2:6] 
    
    valid_answer = False
    while valid_answer != True:
        
        user_input = questionUI(question,mutliple_choice)
        
        if user_input in ["1","2","3","4"]:
            valid_answer = True

    if right_answer == user_input:
        return True
    return False

def quizLoop(quiz):
    correct_count = 0

    for question in quiz:
        answer = questionLoop(question.split("|"))
        if answer == True:
            correct_count += 1
    
    score = (correct_count*5) + ((len(quiz)-correct_count) * -2)
    if score < 0:
        score = 0

    finalScoreUI(score, len(quiz)*5)
    




def mainMenuLoop():
    os.system("cls")
    exit = False
    while exit != True:
        user_input = menuUI()

        if (user_input == "2"): # Quit Game
            exit = True

        elif (user_input == "1"):
            quiz = readQuiz("Week5/Quiz Assignment/Quizes/Python Beginner Quiz.txt")
            shuffle(quiz)
            quizLoop(quiz)


mainMenuLoop()