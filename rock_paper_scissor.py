"""
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input),
compare them, print out a message of congratulations to the winner,
and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""
import random as r
count1 = 0
count2 = 0

def play_again():
    
    again = raw_input("Would you like to continue : Yes or No")
    if again == 'Yes':
        play()
    else:
        exit

def count_points(player_points,player):
    
    global count1
    global count2


    if int(player) == 1:
        it = "Computer"
    elif int(player) == 2:
        it = "Player 2"
        
    if player_points==1:
        count1 = count1 + 1
        
    elif player_points==2:
        count2 = count2 + 1
    elif player_points==0:
        count1=count1
        count2=count2

    if count1>count2:
        print "Player 1 leads."
    elif count2>count1:
        print "{} leads.".format(it)
    else:
        print "Total points a tie. No one is leading."
    
    

def play():
    print "Choose an opponent: Press 1 for Computer or Press 2 for \
    \ Player 2. Press Exit to stop playing the game. "    
    player = raw_input("")
    if player == "Exit":
        exit
    elif int(player) == 1:
        print "Welcome to the game."
        pl_chance1 = raw_input("Choose from rock, paper, scissors")
        options = ['rock','paper','scissors']
        comp_chance1 = r.choice(options)
        if pl_chance1 == 'rock' and comp_chance1 == 'rock':
            print "Its a tie!"
            player_points=0
            count_points(player_points,player)
            play_again()
        elif pl_chance1 == 'paper' and comp_chance1 == 'rock':
            player_points=1
            
            print "Congratulations! You win. Paper beats rock and Computer picked {}. ".format(comp_chance1)
            count_points(player_points,player)
            play_again()
        elif pl_chance1 == 'scissors' and comp_chance1 == 'rock':
            player_points=2
            
            print "Sorry you lost! Rock beats scissors and Computer picked {}. ".format(comp_chance1)
            count_points(player_points,player)
            play_again()
        elif pl_chance1 == 'rock' and comp_chance1 == 'paper':
            player_points=2
            
            print "Sorry you lost! Paper beats rock and Computer picked {}. ".format(comp_chance1)
            count_points(player_points,player)
            play_again()
        elif pl_chance1 == 'rock' and comp_chance1 == 'scissors':
            player_points=1
            
            print "Congratulations! You win. Rock beats scissors and Computer picked {}. ".format(comp_chance1)
            count_points(player_points,player)
            play_again()
        elif pl_chance1 == 'paper' and comp_chance1 == 'scissors':
            player_points=2
            
            print "Sorry you lost! Scissors beats paper and Computer picked {}. ".format(comp_chance1)
            count_points(player_points,player)
            play_again()
        elif pl_chance1 == 'paper' and comp_chance1 == 'paper':
            player_points=0
            
            print "Its a tie!"
            count_points(player_points,player)
            play_again()
        elif pl_chance1 == 'scissors' and comp_chance1 == 'scissors':
            print "Its a tie!"
            player_points=0
            count_points(player_points,player)
            play_again()
        elif pl_chance1 == 'scissors' and comp_chance1 == 'paper':
            player_points=1
            
            print "You win. Scissors beats paper and Computer picked {}. ".format(comp_chance1)
            count_points(player_points,player)
            play_again()
            
    elif int(player) == 2:
        print "Welcome to the game."
        pl_chance1 = raw_input("Player 1 - Choose from rock, paper, scissors")
        comp_chance1 = raw_input("Player 2 - Choose from rock, paper, scissors")
        
        if pl_chance1 == 'rock' and comp_chance1 == 'rock':
            player_points=0
            print "Its a tie!"
            count_points(player_points,player)
            
            
            play_again()
        elif pl_chance1 == 'paper' and comp_chance1 == 'rock':
            player_points=1
            print "Player 1 wins. Paper beats rock. "
            count_points(player_points,player)
            
            
            play_again()
        elif pl_chance1 == 'scissors' and comp_chance1 == 'rock':
            player_points=2
            print "Player 2  wins. Rock beats scissors. "
            count_points(player_points,player)
            
            
            play_again()
        elif pl_chance1 == 'rock' and comp_chance1 == 'paper':
            player_points=2
            print "Player 2 wins. Paper beats rock. "
            count_points(player_points,player)
            
            
            play_again()
        elif pl_chance1 == 'rock' and comp_chance1 == 'scissors':
            player_points=1
            print "Player 1 wins. Rock beats scissors"
            count_points(player_points,player)
            
            
            play_again()
        elif pl_chance1 == 'paper' and comp_chance1 == 'scissors':
            player_points=2
            
            
            print "Player 2 wins. Scissors beats paper. "
            count_points(player_points,player)
            play_again()
        elif pl_chance1 == 'paper' and comp_chance1 == 'paper':
            player_points=0
            
            
            print "Its a tie!"
            count_points(player_points,player)
            play_again()
        elif pl_chance1 == 'scissors' and comp_chance1 == 'scissors':
            player_points=0
            
            
            print "Its a tie!"
            count_points(player_points,player)
            play_again()
        elif pl_chance1 == 'scissors' and comp_chance1 == 'paper':
            player_points=1
            
            
            print "Player 1 wins. Scissors beats paper. "
            count_points(player_points,player)
            play_again()
        

play()
    
