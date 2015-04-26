from random import randint

field = []

for x in range(1, 5):
    field.append(["^'|'^"] * 5)

def print_field(field):
    for row in field:
        print " ".join(row)
        
print "After spotted the monster behind the right bush; it leaped out and made for run into the open field."
print
print "You grabbed rifle from your back and then steadily aimed at the monster in the distance."
print

def random_row(field):
    return randint(1, len(field))

def random_col(field):
    return randint(1, len(field))

hit_1 = random_row(field)
hit_2 = random_col(field)

print hit_1
print hit_2

for shot in range(3):
    print
    print "Aim and shoot!"
    print
    guess_row = int(raw_input("Guess Row: ")) - 1
    guess_col = int(raw_input("Guess Col: ")) - 1
    print
    if guess_row == hit_1 - 1 and guess_col == hit_2 - 1:
        print "You got him! Monster's down!" 
        print
        field[guess_row][guess_col] = "  X  "
        print_field(field)
        print
        print "You confirmed your kill, and dragged it back to your shed."
        print
        break
    elif shot == 2:
        field[guess_row][guess_col] = "  O  "
        print_field(field)
        print
        print "Monster was too far and escaped."
        print
        print hit_1
        print hit_2
        print
        print "Game Over"
        print
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print "Oops, your aim is way off."
            print
            print_field(field)
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