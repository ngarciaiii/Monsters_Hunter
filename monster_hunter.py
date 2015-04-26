from random import randint

print
print "MONSTER HUNTER"
print

print "You were hiking on a trail in dense forest, and then you saw three monsters nearby. Each ran off in different directions."
print
print "Grotesque monster 'Piggy' fled forward on the trail. 'Were-lion' sprinted off-road, and a giant 'Centipede' crawled into cave."
print

name = raw_input("What is your name? ")
monster = raw_input("Which monster do you wish to pursue? ")
weapon = raw_input("Take a weapon with you, what would it be? ")
print

print "So the fearless hunter %s is armed with deadly %s, and then went off to track %s down." % (name, weapon, monster)
print

print "You arrived at the dead end, and there were 9 bushes. Wide open field with nothing in sight beyond the bushes. Obviously %s had to be behind one of those bushes." % (monster) 
print
print "It's getting dark and you are only able to kill %s during the daylight. Hurry catch %s before nightfall." % (monster, monster) 
print

# Generates a number from 1 through 10 inclusive
right_bush = randint(1, 9)
print "Cheat: "
print right_bush
print

guesses_left = 3
# Start your game!
while guesses_left > 0:
    guess = int(raw_input('Which bush? '))
    print
    if guess == right_bush:
        print
        print "You found %s!" % (monster)
        print
        field = []

        for x in range(0, 5):
            field.append(["^'|'^"] * 5)

        def print_field(field):
            for row in field:
                print " ".join(row)

        print
        print "After spotted, it leaped out and made for a run into the open field."
        print
        print "You grabbed rifle from your back, and then steadily aimed at %s in the distance." % (monster)
        print

        def random_row(field):
            return randint(1, len(field))

        def random_col(field):
            return randint(1, len(field))

        hit_1 = random_row(field)
        hit_2 = random_col(field)
        print "Cheat: "
        print hit_1
        print hit_2
        print

        for shot in range(6):
            print
            print "Aim and shoot!"
            print
            guess_row = int(raw_input("Aim vertically (1-5): ")) - 1
            guess_col = int(raw_input("Aim horizontally (1-5): ")) - 1
            print
            if guess_row == hit_1 - 1 and guess_col == hit_2 - 1:
                print "You got %s! It's down!" % (monster)
                print
                field[guess_row][guess_col] = "  X  "
                print_field(field)
                print
                print "You confirmed your kill, and dragged it back to your shed."
                print
                break
            elif shot == 5:
                field[guess_row][guess_col] = "  O  "
                print_field(field)
                print
                print "%s was too far and escaped." % (monster)
                print
                print "Aim coordination: "
                print hit_1
                print hit_2
                print
                print "Game Over"
                break
            else:
                if guess_row not in range(5) or guess_col not in range(5):
                    print "Oops, your aim is way off."
                    print
                elif (field[guess_row][guess_col] == "  O  "): 
                    print "You shot in that direction already"
                    print
                    print_field(field)
                    print
                else:
                    print "Missed! The monster isn't stopping!"
                    print
                    field[guess_row][guess_col]= "  O  "
                    print_field(field)
        break
    elif guess != right_bush: 
        print "Wrong bush! Hurry! It's almost nightfall!"
        print
        guesses_left -= 1
else:
    print
    print "Sun disappeared from the horizon. Blood splattered everywhere! You're lying on the ground with your guts pulled out. The monster is devouring you."
    print
    print "The monster was hiding behind that bush:" 
    print right_bush
    print
