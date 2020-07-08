import random

playgame='y'
while playgame=='y':
    answer=random.randint(1,100)
    yourno=int(input("Guess a number between 1 and 100:"))
    counter=1

    while yourno!=answer:
        if(yourno>answer):
            print("Your number is larger than answer")
        elif(yourno<answer):
            print("Your answer is smaller than answer")
        yourno=int(input("Guess again a number between 1 and 100:"))   
        counter=counter+1
    
    print("yo got it in "+str(counter) +" times")
    playgame=input("continue? press 'y' to play 'n' to exit:")