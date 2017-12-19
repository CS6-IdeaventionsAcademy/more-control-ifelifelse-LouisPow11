#Louis Powers
#12-5-2017
#bob's_cave_Adventure
#A text based adventure 

def right_cave():
    print ("You go to the right and find a river with a boat")
    print ("You could go to the boat and sail away, you could walk along the border of the river, or you could swim across")
    print ("Please type Swim, walk, or boat")
    choice = input("Enter S for Swim, W for Walk, or B for Boat: ").upper()
    return choice

def wrong_answer():
    print ("You bad person")
    print ("Please don't do that again")

def right_cave():
    print ("You find a tunnel that starts to slopes upward.")
    print ("You see a passage way and a rope you could climb down.")
    print ("Please type in rope or passage")
    rope_choice == "ROPE" or rope_choice == "R":.upper()
    return choice

print ('~`'*60)
print ('''Welcome to
 ____  _____  ____  ___      __    ____  _  _  ____  _  _  ____  __  __  ____  ____ 
(  _ \(  _  )(  _ \/ __)    /__\  (  _ \( \/ )( ___)( \( )(_  _)(  )(  )(  _ \( ___)
 ) _ < )(_)(  ) _ <\__ \   /(__)\  )(_) )\  /  )__)  )  (   )(   )(__)(  )   / )__) 
(____/(_____)(____/(___/  (__)(__)(____/  \/  (____)(_)\_) (__) (______)(_)\_)(____)
         ''')
print ('~`'*60)

 
print ("You see a cave go right or left")
cave_choice = input("Enter right or left").upper()
if cave_choice == "RIGHT" or cave_choice == "R":
    choice = right_cave()
    if choice == "BOAT" or choice == "B":
        print ("You sit in the boat and it starts to leak you start falling down and start to drown. YOU ARE DEAD")
    elif choice == "WALK" or choice == "W":
        print ("You walk and trip into the river and drown YOU DIE")
    elif choice == "SWIM" or choice == "S":
        print ("You start swiming untill you see an island but you all so see a piece of wood because your very tired of swiming you could go on the wood.")
        print ("please type w for wood or i island")
    elif choice == "WOOD" or choice == "W":
        print ("You go on the wood and find that there is a torch on one side of the river and the other side there is a bright light")
        print ("Please type either light or torch")
    elif choice == "ISLAND" or choice == "I":
        print ("You keep swiming and faint then drown and DIE")
    elif choice == "LIGHT" or choice == "L":
        print ("You paddle over to the light you get too exited and jump on to land and jump to the light and find that its a mirror it brakes and you get stabbed with one of the shards, YOU DIE") 
    elif choice == "TORCH" or choice == "T":
        print ("You walk to the torch and see that it shines light on gold and jewels YOU WIN")
    else:
        wrong_answer()
    
elif left_choice == "LEFT" or left_choice == "L":
    print ("You find a tunnel that starts to slopes upward.")
    print ("You see a passage way and a rope you could climb down.")
    print ("Please type in rope or passage")
    if rope_choice == "ROPE" or rope_choice == "R":
        print("you go down the rope like a monkey, you could walk along a little longer or go back up the rope")
        print ("Please type in go back or walklong")
    elif pass_choice == "PASSAGE" or pass_choice == "P":
        print("You see a dragon breathing and huffing and it blows fire on you, you DIE")
    elif back_choice == "BACK" or back_choice == "B":
        print("You go back up the rope and a dragon is infront of you, you DIE")
    elif walk_long_choice == "WALKLONG" or walk_choice == "W":
        print("You walk along and see a computer or there is a speaker that is on.")
        print ("please type speaker or computer")
    elif speaker_choice == "SPEAKER" or speaker_choice == "S":
        print ("You walk up to the speaker it has a motion sensor so it blasts 20,000 hertz")
    elif speaker_choice == "COMPUTER" or speaker_choice == "C":
        print ("You go on the computer and see that there is a big sign that says claim 100 bitcoins YOU WIN.")
else:
    print ("PLEASE DONT TYPE RANDOM THINGS")
