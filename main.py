#Print Heading and explanation
print()
print("    ======================")
print("Welcome to the Custom Car Center")
print("    =======================")
print()
#Instructions to user
print("Below please enter the letter of the selection you're looking for ")
print()
#List of choices for make&model
print("       ~Make & Model~")
print()
print("What model of car are you ordering?")
print()
print("   a. Lightning Speedster ")
print("   b. Eco Leaf ")
print("   c. Harp Chord ")
print("   d. Cheveron Jolt ")
#Show selection
FirstSelection = input("Please enter 'a' - 'd':   ")
print()
print("    You selected", FirstSelection)
print()
print()
# List through all the extras and show choices after each question
print("         Customize")
print()
print()
# 4-door option, show selection
print("Would you like to upgrade to the 4-door option?")
print()
print("  a. Yes")
print("  b. No")
UpgradeOne = input("Please enter 'a' or 'b':  ")
print()
print("    You selected", UpgradeOne)
print()
print()
# car color, show selection, input any text value
print("What color would you like your car to be? ")
print("You can pick any color:  ")
print()
color = input("My color choice is:    ")
print()
print()
print("You chose:", color)
print()
print()
#deluxe weather package, show selection
print("Would you like to add the deluxe weather package?")
print()
print("   a. Yes")
print("   b. No")
UpgradeTwo = input("Please enter 'a' - 'b':   ")
print()
print("    You selected", UpgradeTwo)
print()
print()
# interior  
# custom engine multiple choice
print("     Interior")
print("What engine would you like the car to have")
print()
print("   a. I-4 Entry Engine")
print("   b. V-6 Performance Engine")
print("   c. Eco Diesel Engine")
Engine = input("Please enter 'a' - 'd':   ")
print()
print("    You selected", Engine)
print()
print()
# heated seats select yes or no
print("Would you like to add the heated seats?")
print()
print("   Yes")
print("   No")
Seats = input("Please enter Yes or No:   ")
print()
print("   You selected", Seats)
print()
# be sure to summarize all items from above
print()

print("=================================================================")
print("            Summary")
print()
# display item details with answers
print("You have selected the following:")
print()  
print("    Make & Model:  ", FirstSelection)
print("    Upgrade to 2-door: ", UpgradeOne)
print("    Deluxe Weather Package: ", UpgradeTwo)
print("    Color: ", color)
print("    Engine: ", Engine)
print("    Seats: ", Seats)
print("=================================================================")
print()