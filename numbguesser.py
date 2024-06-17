import random
live_dead=0     

def guess():   
    global live_dead
    random_number = random.randrange(101)
    guesses=8
    i=1   #on default it is 0 to 100
    while(i<=guesses):
        ur_guess=int(input("your guess:"))
        if ur_guess < random_number:
            print("your guess is less :( REMAINING GUESSES:"+str(guesses-i))
            i+=1
        elif ur_guess > random_number:
            print("your guess is greater :( REMAINING GUESSES:"+str(guesses-i))
            i+=1
        else:
            print("your guessed it right :) ")
            print("you guessed it in "+str(i)+" times!!")
            print(" record: "+str(i))
            print("now you may pass")
            live_dead=1
            break
    if live_dead == 1:
        print("You passed")
        print("You are the chosen warrior \n You are the strongest warrior this place has seen enjoy")
        print("Congratultions !!!! You win this bout..")
    else:
        print("You are a dead man...you say after looking at the man besides him grinning")
        print("He laughs ... yet another fool who thinks he can challenge..")
        print("(A GODLY LIGHT APPEARS MAKING YOU DISINTEGRATE INTO NOTHINGNESS YOU DIE )")
        print("GAME OVER")