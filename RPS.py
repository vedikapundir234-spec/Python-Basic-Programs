import sys
import random
from enum import Enum 

def playrps():                            #function
    class RPS(Enum):
        ROCK=1
        PAPER=2
        SCISSORS=3
    

    playerchoice=input("\nEnter:\n1 for rock\n2 for paper\n3 for scissors:\n\n")
    if playerchoice not in ["1","2","3"]:           #using lists 
        print("You must enter 1,2,or 3")
        return playrps()                   #recursion
    player=int(playerchoice)                   #convert playerchoice to integer


    computerchoice=random.choice("123")
    computer=int(computerchoice)  

    print("\nYou chose:"+str(RPS(player)).replace('RPS.',''))
    print("Python chose:"+str(RPS(computer)).replace('RPS.',''))

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

    print("\nPlay Again?")

    while True:
            playagain=input("\nPress:\nY for Yes  or\n Q to Quit\n\n")
            if playagain.lower() not in {"y","q"}:
                continue
            else:
                break

    if playagain.lower() == "y":
            return playrps()
    else:
            print("THANKYOU FOR PLAYING🥳")
            sys.exit("END")

playrps()

