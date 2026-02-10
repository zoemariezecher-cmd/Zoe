""" Rock Paper Scissors Lizard Spock """

# import random function for using random.randrange
import random

# helper functions 

def name_to_number(name):
    """ name_to_number """
    if name == "rock":
        return 0
    elif name == "spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3 
    elif name == "scissors":
        return 4
    else:
        return -1
    
def number_to_name(number):
    """ number_to_name """
    if number == 0:
        return "rock"
    elif number == 1:
        return "spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return " Error "
        
def rpsls(player_choice):
    """ rpsls """
  
    #convert player's choice by using number_to_name
    player_number = name_to_number(player_choice)
    
    #compute random guess for comp_choice by using random.randrange
    comp_number = random.randrange(0, 5)
    
    
    #compute difference of comp_number and player_number 
    difference = (comp_number - player_number) % 5    

    
    # determine winner
    if difference < 3:
        player_win = False
    else:
        player_win = True
    
    #convert comp_number to comp_choice by using number_to_name
    comp_choice =  number_to_name(comp_number)
    
    #results
    print " Player chooses " + player_choice
    print " Computer chooses " + comp_choice
    if player_win:
        print "Player wins!"
    elif comp_number == player_number:
        print "It's a Tie!"
    else:
        print "Computer wins!"
        
player_choice = raw_input( 'Choose character.Options: rock, paper, scissor,lizard, spock')

rpsls(str(player_choice))