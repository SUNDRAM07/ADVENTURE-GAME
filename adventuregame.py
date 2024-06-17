import random
import rockpapersissors
import numbguesser
def deaths():
    if croc =="yes":
        print("you removed clothes and went ahead to take the safe way ignoring the warning.")
        print("as soon as you entered the river\n 4 crocodiles jumped on you eating you \npeice by peice")
        print("The worst part is \n you didnt lose consiousness until your heart was eaten")  
        print("You died the WORST kind of death possible")
        print("GAME OVER")
def left():
    print("You continue walking to the end for 5 mins \nbut there is one man at the end of the road \nhe is looking vicious")
    confront=input("Would you like to confront him??\n(if you don't confront him you would need to chose the other path...)\nyes or no ")
    if confront=="yes":
        print("You go confront him...")
        print("He is surprisingly sweet.. He says there is a small rule you have to follow if you want to pass ")
        print("Play rock paper and scissors if you win 5 matches against me i will let you go")
        play_rps=input("play rock paper scissors with him..").lower()[0]    
        if play_rps=="y":
            rockpapersissors.rpsgame()
        else:
            game()
    elif confront=="no":
            game
def game():
    print("You are at the end of a dirt road ")
    twopaths=input("you are at a cross section would you like to go left or right ").lower()
    
    if twopaths=="left":
        left()
    elif twopaths=="right":
        right()
      
def right():
    global croc
    print("You have chosen to go to right..lets see")
    print("You arrived at a bridge accross a river")
    print("You have got 3 options \n either swim accross the river or cross the bridge")
    soc=input("swim or cross or go back? ").lower()
    if soc =="swim":
        print("You chose to swim underneath the bridge \nthinking it will be safe")
        croc=input("As soon as you enter. you see something suspicious in water still wanna go ").lower()                   
        if croc=="yes":
            deaths()
        if croc=="no":
            print("where do you wanna go..")
            right()
    elif(soc=="cross"):
        print("So you choose to cross the bridge...")
        print("well it looks like a normal bridge its a fine bridge to cross ...")
        approach=input("you are crossing the bridge...\n at the end of the bridge there seems to be a weird person standing ...he looks puzzled \n do you want to approach him? ")                
        if approach == "yes":
            print ("He is a friendly man but he looks puzzled")
            assure=input("\"ayo friendo this is dead endo do you wanna cross the bridge??  \"")
            if assure=="yes":
                print("very well but remember you need to help me out then ..")
                print("(You are confused)")
                print("\"well mister we have to guess a number it will be from 1 to 100 and we have only 8 tries..\"")
                print("Remember failiure means death")
                last=input("Are you ready? ")
                if last=="yes":
                    numbguesser.guess()
                elif last=="no":
                    s_thoughts=input("what happened do you not want to proceed").lower()
                    if s_thoughts=="yes":
                        right()
                    elif s_thoughts=="no":
                        numbguesser.guess()
            elif assure=="no":
                print("All right then get lost before i kill you myself")
                right()
        elif approach=="no":
            print("you chose to go back.....")
            right()
    elif soc=="go back":
        print("you chose to go back to start position.........")
        game()
        


def win():
    print("You are the chosen warrior \n You are the strongest warrior this place has seen enjoy")
    print("Congratultions Player: "+name+" !!!! You win this bout..")
    
play=input("Would you like to play this adventure game? ").lower()[0]

if play=="n":
    makesure=input("YOU sure you wanna leave this game .. this adventure game is a lot of fun..?").lower()[0]
    if makesure=="y":
        print("YOU LOSE")
    else:
        name=input("Enter your name adventurer.")
        game()    
elif play=="y":
    name=input("Enter your name adventurer.")
    game()
    