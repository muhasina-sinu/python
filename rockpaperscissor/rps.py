
import random



score1 = 0
score2 = 0


def game():

    global score1
    global score2
    x = ['rock','paper','scissor']
    player1 = random.choice(x)
    print("Enter your choice : rock / paper / scissor"  )
    player2 = input()

    if player1.lower() == player2.lower():
        print("TIE")
    elif player1.lower() == "rock" and player2.lower() == "paper" :
        print("you won  "+player1 )
        score2+=1
    
    elif player1.lower() == "paper" and player2.lower() == "scissors" :
        print("you won  " +player1) 
        score2+=1


    elif player1.lower() == "scissor" and player2.lower() == "rock" :
        print("you won  "+player1 ) 
        score2+=1

    else:
        print("you lost! player1 = " +player1)
        score1+=1

    


#game()
#repeat = input("do you want to continue the game? (y/n)")
while True:
    game()
    repeat = input("do you want to continue the game? (y/n)")
    if repeat == 'y':
        continue
    else:
        break

print("scoreboard\ncomputer: "+str(score1)+"\nyou: "+str(score2))
