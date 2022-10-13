print()
print('You are going on a camping trip and are driving down a road leading a camping area.')
print('There is a fork in the road ahead; going Left would take you into the deep woods,')
print('while going Right would take you up into the mountains.')
print()
direction = str(input('Do you go Left or Right? ')).lower()
if direction == "left":
    print()
    print('You decide to find a camping spot down in the deep woods. You set up your tent and go to sleep, but in the middle')
    print('of the night you wake up hearing noises outside. You make up your mind and leave your tent to find out what is')
    print('making the noises, but as soon as you exit the tent, the noises stop, and all you hear is an eerie silence.')
elif direction == "right":
    print()
    print('You decide to find a camping spot up in the mountain. You drive up to the camping area, set up your tent, and sleep all')
    print('the way through the night. When morning comes, you pack up all your stuff, load it in your car, and start back down the')
    print('mountain road. This time, however, as you are driving down, a deer leaps in front of your car, and you swerve to avoid it.')
    print('Because you swerved, your car barely hangs on to the road, and is teetering on the edge of a 100 foot fall.')
else:
    print('Try again')