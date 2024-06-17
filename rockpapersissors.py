import random
def rpsgame():
    user_wins=0
    comp_wins=0
    while user_wins < 5 or comp_wins < 5 :
        choices=["rock","paper","scissors"]
        user_input=input("CHOOSE /ROCK/PAPER/SCISSORS or Q to quit ").lower()
       
        if user_input=="q":
            make_sure=input("There might be unknown consequences for leaving the old man are you sure..(y or n)").lower()[0]
            if make_sure=="y":
                print("IF you dont wanna play get lost")
                break
            elif user_input=="n":
                continue 
        if user_input not in ["rock","paper","scissors"]:
            print("invalid choice bitch..")            
            continue
        else:
            random_choice=random.randrange(0,3)    
        #0:rock 1:paper 2:scissors
        if user_input==choices[random_choice]:
            print("viscious looking man chose:",choices[random_choice])
            print("man its a tie a 1/3 chance..")
        elif random_choice == 0 and user_input=="paper":
            print("viscious looking man chose:",choices[random_choice])
            user_wins += 1
            print("You lucky son of a bitch")
        elif random_choice == 1 and user_input=="scissors":
            print("viscious looking man chose:",choices[random_choice])
            user_wins += 1
            print("You lucky son of a bitch")
        elif random_choice == 2 and user_input=="rock":
            print("viscious looking man chose:",choices[random_choice])
            user_wins += 1
            print("You lucky son of a bitch")
        else:
            comp_wins +=1
            print("viscious looking man chose:",choices[random_choice])
            print("guess my luck aint half bad")
            print("Dont lose hope man")
    if comp_wins==5:
        print("huh you lost you really are a bitch lover..")
        print("guess i will kill you . but wait do you want slow or fast death..")
        print("who cares i will just kill you after cutting all your limbs and organs")
        print("HA HAHAHHA  HAHAHA HAHAH AHAHHA ")
        print("GAME OVER A MANIAC HAS CAPTURED YOU AND WOULD TORTURE YOU TILL YOU CANT FEEL PAIN")
    elif user_wins==5:
        print("well whatever i would let you pass this time seeing you are so good in this game")
        print("Your score was "+str(user_wins)+" and mine was "+ str(comp_wins))
        print("I guess i would let you live you can pass..")
        print("Conratulations player you passed and avoided iminent death by the brute ...")