import sys
import random
from enum import Enum 

class RPS(Enum):
    ROCK=1
    PAPER=2
    SCISSORS=3

print(" ")

playerchoice=input("Enter:\n1 for rock\n2 for paper\n3 for scissors:\n\n")
player=int(playerchoice)                   #convert playerchoice to integer

if player<1 or player>3:
    sys.exit("you must enter 1,2,or 3")    #sys.exit exits the code

computerchoice=random.choice("123")
computer=int(computerchoice)  

print(" ")

print("You chose:"+str(RPS(player)).replace('RPS.',''))
print("Python chose:"+str(RPS(computer)).replace('RPS.',''))
print(" ")

if player==1 and computer==3:
    print("You Win!🥇")
elif player==2 and computer==1:
    print("You Win!🥇")
elif player==3 and computer==2:
    print("you win!🥇")
elif player==computer:
    print("TIE GAMEE!🫨")
else:
    print("Python Win!🐍")
  