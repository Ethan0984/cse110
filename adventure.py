print()
print('You are going on a camping trip and are driving down a road leading a camping area.')
print('There is a fork in the road ahead; going Left would take you into the deep woods,')
print('while going Right would take you up into the mountains.')
print()
direction = str(input('Do you go LEFT or RIGHT? ')).lower()
if direction == "left":
    print()
    print('You decide to find a camping spot down in the deep woods. You set up your tent and go to sleep, but in the middle')
    print('of the night you wake up hearing noises outside. You make up your mind and leave your tent to find out what is')
    print('making the noises, but as soon as you exit the tent, the noises stop, and all you hear is an eerie silence.')
    print()
    tent = str(input('Do you CONTINUE searching for the source of the sound or GO BACK to your tent? ')).lower()
    if tent == "continue":
        print()
        print('You decide to walk around and try and find the source of the sound. As you are walking through the dark searching, you see')
        print('a hollow trunk. You walk over to look inside, but all you see is darkness leading downward. You hear the noise again, and')
        print('it is most definitely coming from whatever lurks below')
        print()
        trunk = str(input('Do you CONTINUE or GO BACK to your tent? '))
        if trunk == "continue":
            print()
            print('You decide to continue down the ominous gap in the trunk. You jump in, unsure of what is yet to come. After falling for an incredibly long,')
            print('time, you land on the cold, hard ground, immediately dying on impact. You never did figure out what that noise was.')
        elif trunk == "go back" or "goback":
            print()
            print('You decide to go back to your tent. Unfortunately, in the darkness of the night, you are unable to locate your tent, and accidentally wander')
            print('right into the den of a mother bear, who proceeds to rip you to shreds. Very unfortunate end.')
    elif tent == "go back" or "goback":
        print()
        print('You decide to go back inside your tent and try and forget what happened. You drift off to sleep, and wake up ready for')
        print("breakfast. On your way home, you see a Chick-fil-a and a McDonald's that are open for breakfast.")
        print()
        breakfast = str(input("Do you want to go to CHICKFILA or MCDONALDS for breakfast?")).lower()
        if breakfast == "chickfila":
            print()
            print('You decide to go to Chick-fil-a for breakfast. You eat your food, and go home to the boring monotony of your everyday life.')
        elif breakfast == "mcdonalds":
            print()
            print("You decide to go to McDonald's for breakfast. You get a stomach ache from the food, stop concentrating on the road, and run")
            print('straight into a tree, dying in the process.')
        else:
            print('Try again')
    else:
        print('Try again')
elif direction == "right":
    print()
    print('You decide to find a camping spot up in the mountain. You drive up to the camping area, set up your tent, and sleep all')
    print('the way through the night. When morning comes, you pack up all your stuff, load it in your car, and start back down the')
    print('mountain road. This time, however, as you are driving down, a deer leaps in front of your car, and you swerve to avoid it.')
    print('Because you swerved, you crash your car into the wall of the mountain, stranding you there.')
    print()
    crash = str(input("Do you want to LOOK for help or make a SHELTER? ")).lower()
    if crash == "look":
        print()
        print("You decide to look for help nearby. You walk down the road some ways until at last, you see a vehicle on the side of the road.")
        print("However, it seems to be abandoned, with no sign of the owners anywhere near. The sunroof is open, and you know how to hotwire")
        print("cars.")
        print()
        car = str(input("Do you want to STEAL the car or LEAVE it alone and keep looking for something else? ")).lower
        if car == "steal" or " steal" or "steal ":
            print()
            print("You decide to commit a minor felony and steal the car. You climb in through the top, hotwire the car, and start driving away. As you get")
            print("further away from the spot you were at, you begin to hear is police sirens. You hope that they are not for you, but it is in vain, as within")
            print("minutes you can see multiple cop cars chasing you. You are still in a high up area, so you can only think of 3 possible choices to make.")
            print()
            final = str(input("You can either drive off a CLIFF, PULL OVER, or keep up the CHASE and try to escape. What do you choose? ")).lower
            if final == "cliff" or " cliff" or " cliff":
                print()
                print("You drive off the cliff and die. Not the brightest choice, but they didn't take you alive, so at least that's something.")
            elif final == "pull over":
                print()
                print("You decide to pull over. The cops arrest you for grand theft auto, and put you in prison for 3 years, in which time you join a gang, start a gang war,")
                print("and get murdered.")
            elif final == "chase" or " chase" or "chase ":
                print()           
                print("You decide to risk it all and continue the chase. After 2 hours of evading cops, stealing others cars, and going at ridiculous speeds, you actually") 
                print("manage to escape the clutches of the law. Unfortunately, when you get home, your neighbor shoots you. Not for any particular reason, he just does.")
                print("So naturally, you die.")
            else:
                print("Try again")
        elif car == "leave" or " leave" or "leave ":
            print()
            print("Your morals win this time, and you leave the car in search of help. As you are wandering, you become lost in the woods, and accidentally wander")
            print("into an area in which you can see a deer. You are pretty hungry, and are starting to seriously consider killing the deer for food.")
            print()
            deer = str(input("Do you try and HUNT the deer, or do you LOOK somewhere else? ")).lower
            print
            if deer == "hunt":
                print()
                print("You decide to hunt the deer. You approach it slowly, grabbing a stick to stab it with. Unfortunately, your eyesight is not that great, and as you get closer,")
                print("you realize it is not actually a deer, but a moose. The moose then kills you good and dead.")
            elif deer == "look":
                print()
                print("You decide not to hunt the deer, and to look somewhere else for food and shelter. You wander for days on end, until you find a mushroom that looks edible-ish.")
                print("You eat the mushroom. Unfortunately, it was not, in fact, edible, and you die a slow death of poisoning.")
            else:
                print('Try again')
        else:
            print('Try again')
    elif crash == "shelter":
        print()
        print("You decide to make a shelter and try and rough it in the wild. You set up your tent in a good spot, and go out into the woods to")
        print("look for some food to eat. As you are wandering around, you come across another tent that has a lot of materials inside, and nobody")
        print('even close to it.')
        print()
        theft = str(input("Do you want to STEAL the supplies or LOOK somewhere else? ")).lower()
        if theft == "steal":
            print()
            print("You decide to steal the supplies from the tent. However, as you are making your way back to your tent, some people that are likely")
            print("the owners of the tent see you with their supplies, and take them back, shooting you in the process because they were, unfortunately,")
            print("serial killers.")
        elif theft == "look":
            print()
            print("You decide to look somewhere else for food. Unfortunately for you, as you are walking along a cliff looking for something to eat, a mountain")
            print("goat decides he doesn't like the look of you, and pushes you off, ultimately leading to your demise.")
        else:
            print('Try again')
    else:
        print('Try again')
else:
    print('Try again')