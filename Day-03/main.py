print("Welcome to Treasure Island.\nYour mission is to find the treasure")

left_or_right = input("You're at a cross road. Would you like to go 'left' or 'right'?: ").lower()

if left_or_right == 'left':

    swim_or_wait = input("You come to a lake. There is an island in the middle of the lake. "
                         "Would you like to 'wait' for a boat or 'swim' across?: ").lower()

    if swim_or_wait == 'wait':

        red_blue_yellow = input("You arrive at the island unharmed/ There is a house with 3 doors. One 'red', "
                                "one 'yellow' and one 'blue'. Which colour do you choose?: ").lower()

        if red_blue_yellow == 'yellow':
            print("You have seized the treasure and won!")
        elif red_blue_yellow == 'blue':
            print("You have encountered a pack of wolves and scream as they ravage your body.")
        elif red_blue_yellow == 'red':
            print("You've been burnt by a fire and been reduced to ashes.")

        else:
            print("Game Over.")
    else:
        print("You've been attacked by trout.\nGame Over.")
else:
    print("You've fallen into a hole.\nGame Over.")
