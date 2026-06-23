print("WELCOME TO THE QUIZ!!")
while True:
    playgame=input("ARE YOU READY FOR THE QUIZ?\nYES or NO?")

    if playgame.lower()=="yes":
        print("Let's start the Quiz!!")
        break                         #exits the loop
    elif playgame.lower()=="no":
        print("Maybe next time :)")
        quit()        #will quit the game
    else:
        print("Invalid input❌\nPlease type YES or NO:")   #no break here so loop will repeat until valid value

count=0

while True:
    answer=input("What does RAM stands for?")

    if not answer.strip():   #if the answer is blank
        print("Blank answers not valid..answer again:")
        continue          #continue the loop from start
    if answer.lower()=="random access memory":
        print(" YOUR ANSWER IS CORRECT :)")
        count+=5             #increase the value by 5
    else:
        print("YOUR ANSWER IS INCORRECT:(")
        break            #exits the loop

while True:
    answer=input("Which language is known for web page styling?")

    if not answer.strip():
        print("Black spaces not valid..answer again:")
        continue 
    if answer.lower()=="css":
        print("YOUR ANSWET IS CORRECT :)")
        count+=5
    else:
        print("YOUR ANSWER IS INCORRECT:(")
        break 

while True:
    answer=input("What sysmbol is used for comments in Python?")
    if not answer.strip():
        print("Blank spaces not allowed..answer again:")
        continue
    if answer.lower()=="#":
        print("YOUR ANSWER IS CORRECT :)")
        count+=5
    else:
        print("YOUR ANSWER IS INCORRECT:(")
        break 

while True:
    answer=input("Which data type stores TRUE or FALSE values?")
    if not answer.strip():
        print("Blank spaces not valid..answer again:")
        continue 
    if answer.lower()=="boolean":
        print("CORRECT :)")
        count+=5
    else:
        print("YOUR ANSWER IS INCORRECT:(")
        break

print("Your total score is:" + str(count))

percentage= (count/20)*100
print("Your total percentage is:" + str(percentage))

if percentage>50:
    print("YOU DID GREAT!!🙌")
else:
    print("NEED MORE PRACTICE!!")