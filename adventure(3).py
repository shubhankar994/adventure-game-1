import time
import random

def print_pause(message):
    print(message)
    time.sleep(0)

def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if response == option1:
            break
        elif response == option2:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response

def intro(villain):
    print_pause("You find yourself standing in an open field, " 
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {villain} is somewhere around here, "
                "and has been terrifying the near by village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.\n")

def begins(items,villain):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print("What would you like to do?")
    choice = valid_input("(Please enter 1 or 2)\n", "1", "2")
    if choice == "1":
        print_pause("You approach the door of the house.")
        print_pause(f"You are about to knock when the door opens and out steps a {villain}.")
        print_pause(f"Eep! This is the {villain}'s house!")
        print_pause(f"The {villain} attacks you!")
        fight(items,villain)
    elif choice == "2":
        print_pause("You peer cautiously into the cave.")
        cave(items)

def fight(items,villain):
    if "sword" in items:
        fight_scene = valid_input("Would you like to "
                                  "(1) fight or "
                                  "(2) run away?\n", "1", "2")
        if fight_scene == "1":
            print_pause(f"As the {villain} moves to attack, you unleash your new sword.")
            print_pause("The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.")
            print_pause(f"But the {villain} takes one look at your shiny new toy and runs away")
            print_pause(f"You have rid the town of the {villain}. You are victorious!\n")
            play_again(items)
            
        elif fight_scene == "2":
            print_pause("You run back into the field. Luckily, you don't seem to have been followed.\n")
            begins(items)
    else:
        fight_scene = valid_input("Would you like to (1) fight or (2) run away?\n", "1", "2")
        if fight_scene == "1":
            print_pause("You do your best...")
            print_pause(f"but your dagger is no match for the {villain}.")
            print_pause("You have been defeated!\n")
            play_again(items)
            
        elif fight_scene == "2":
            print_pause("You run back into the field. Luckily, you don't seem to have been followed.\n")
            begins(items)

def cave(items):
    if "sword" in items:
        print_pause("You've been here before, and gotten all the good stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.\n")
        begins(items)
        
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword with you.")
        items.append("sword")
        print_pause("You walk back out to the field.\n")
        begins(items)

def play_again(items):
    play_again = valid_input("Would you like to play again? "
                             "Please say 'Yes' or 'No'.\n","yes", "no")
    if "yes" in play_again:
        print("Loading...\n")
        time.sleep(0)
        play_game()
    elif "no" in play_again:
        print("OK, goodbye!")

def play_game():
    items = []
    villains = ['troll', 'pirate', 'dragon', 'zombie', 'bear', 'tiger']
    villain = random.choice(villains)
    intro(villain)
    begins(items,villain)

#villains = ['troll', 'pirate', 'dragon', 'zombie']
#villain = random.choice(villains)

play_game()