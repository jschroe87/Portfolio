#Text RPG
#by Eber

import cmd
import textwrap
import sys
import time
import random

screen_width = 100

#Spieler

class player():
    def__init__(self):
        self.name = ''
        self.job = ''
        self.hp = 0
        self.status = []
        self.location = 'start'
        self.game_over = False

myPlayer = player()

#title screen

def title_screen_selection():
    option = input("> ")
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help','quit']:
        print("Please enter a valid command.")
        option = input("> ")
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()


def title_screen():
    os.system('clear')
    print('###############################################')
    print('# Welcome to the mysterious island game!      #')
    print('###############################################')
    print('                  - Play -                     ')
    print('                  - Help -                     ')
    print('                  - Quit -                     ')
    print('             Copyright 2019 Eber               ')
    title_screen_selection()

def help_menu():
    print('###############################################')
    print('#               - Help Menu -                 #')
    print('###############################################')
    print('   - Use up, down, left and right to move -    ')
    print('      - Type your commands to do them -        ')
    print('     - Use "look" to inspect something -       ')
    print('          - Good luck and have fun! -          ')
    title_screen_selection()

#####Game #######

def start_game():



###### Map #####

ZONENAME = '',
DESCRIPTION = 'description',
EXAMINATION = 'examine',
SOLVED = False,
UP = 'up', 'north',
DOWN = 'down', 'south',
LEFT = 'left', 'west',
RIGHT = 'right', 'east',

solved_places = { 'a1':False, 'a2':False, 'a3':False, 'a4':False,
                  'b1':False, 'b2':False, 'b3':False, 'b4':False,
                  'c1':False, 'c2':False, 'c3':False, 'c4':False,
                  'd1':False, 'd2':False, 'd3':False, 'd4':False,
                  }
zonemap ={
    'a1':{
        ZONENAME = "The Beach",
        DESCRIPTION = 'the beach you woke up.',
        EXAMINATION = 'the white sand lurs into the silent ocean.',
        SOLVED = False,
        UP = '',
        DOWN = 'b1',
        LEFT = '',
        RIGHT = 'a2',

    },
    'a2':{
        ZONENAME = "The western Forest",
        DESCRIPTION = 'description',
        EXAMINATION = 'examine',
        SOLVED = False,
        UP = '',
        DOWN = 'b2',
        LEFT = 'a1',
        RIGHT = 'a3',

    },
    'a3':{
        ZONENAME = "The Mountain",
        DESCRIPTION = 'description',
        EXAMINATION = 'examine',
        SOLVED = False,
        UP = '',
        DOWN = 'b3',
        LEFT = 'a2',
        RIGHT = 'a4',
    },
    'a4':{
        ZONENAME = "The Swamp",
        DESCRIPTION = 'description',
        EXAMINATION = 'examine',
        SOLVED = False,
        UP = '',
        DOWN = 'b4',
        LEFT = 'a3',
        RIGHT = '',

    },
    'b1':{
        ZONENAME = "The eastern Forest",
        DESCRIPTION = 'description',
        EXAMINATION = 'examine',
        SOLVED = False,
        UP = 'a1',
        DOWN = 'c1',
        LEFT = '',
        RIGHT = 'b2',

    },
    'b2':{
        ZONENAME = "The Plateau",
        DESCRIPTION = '',
        EXAMINATION = '',
        SOLVED = False,
        UP = 'a2',
        DOWN = 'c2',
        LEFT = 'b1',
        RIGHT = 'b3',

    },

}

##### GAME INTERACTIVITY ######

def print_location():
    print('\n'+('#'*(4+len(myPlayer.location))))
    print('# '+ myPlayer.locatio.upper()+ ' #')
    print('# '+ zonemap[myPlayer.location][DESCRIPTION] +' #')
    print('\n'+('#'*(4+len(myPlayer.location))))

def prompt():
    print("\n"+ "===================")
    print("what would you like to do?")
    action = input("> ")
    acceptable_actions =['move', 'go', 'travel','walk', 'quit', 'examine', 'inspect', 'interact', 'look']
    while action.lower() not in acceptable_actions:
        print("Unknown action, try again. \n")
        action = input("> ")
    if action.lower() ='quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel','walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        payer_examine(action.lower())

def player_move(myAction):
    ask = "Where would you like to move to?\n"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        movement_handler()
        print_location()

    elif dest in ['down', 'south']:
    elif dest in ['left', 'west']:
    elif dest in ['right', 'east']:


def movement_handler(destination):
    print("\n"+"You have moved to "+ destination + ".")
    myPlayer.location = destination

def player_examine(action):
    if zonemap[myPlayer.location][SOLVED]:
        print("You have already exhausted this zone")
    elif:
        print("You can look around here.")


##### GAME FUNTIONALITY #######

def start_game():
    return

def main_game_loop():
    while myPlayer.game_over is False:
        prompt()

def setup_game():
    os.system('clear')

    #Character selection

    question1 = "Hello, what's your name? \n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
        player_name = input("> ")
        myPlayer.name = player_name
    #Job
    question2 = "What was your former profession? \n"
    question2added = "(You can play as engineer,sailor,journalist or prisoner) \n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
        player_job = input("> ")
        valid_jobs = ['engineer', 'sailor','journalist','prisoner']
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print("You are now a "+ player_job"!\n")
        while player_job.lower() not in valid_jobs:
            if player_job.lower() in valid_jobs:
                myPlayer.job = player_job
                print("You are now a "+ player_job"!\n")

        if myPlayer.job is 'engineer':
            self.hp = 110
        elif myPlayer.job is 'sailor':
            self.hp = 90
        elif myPlayer.job is 'journalist':
            self.hp = 80
        elif myPlayer.job is 'prisoner':
            self.hp = 130

        ###Introduction
        question3 = "Welcome, " + player_name +" the "+ player_job ".\n"
        for character in question3:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
            player_name = input("> ")
            myPlayer.name = player_name

        speech1 ="With a stolen hot air balloon you are stranded on this mysterious island!"
        speech2 ="You have no items with you, because you had to throw them all into the sea to get to the island!"
        speech3 ="You are all alone on the island and you must try to survive as long as possible!"
        speech4 ="Your former profession can be useful in your struggle for survival!"
        for character in speech1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.03)
        for character in speech2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.03)
        for character in speech3:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.03)
        for character in speech4:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.02)
        os.system('clear')
        print("#######################")
        print("#   Let's start now!  #")
        print("#######################")
        main_game_loop()

title_screen()
