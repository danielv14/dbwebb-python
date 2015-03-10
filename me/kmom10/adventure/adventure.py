"""
Welcome to Movie-quiz Adventure Game!
The point of the game is to get through 7 diffrent rooms and finish the game.
To get from one room to the other you have to solve small puzzles and finding a note in each room. 
On the note you can read a movie-related question and if you shout the correct answer the door to the next room opens.

*** The first two rooms are "guided" and are designed to help you understand the game and how it works.
    From the thrid room it gets a little bit harder.

*** Remember that you can always type help to get a list of available commands. 
    You can also type q och quit to quit the game anytime you like.

*** Remember that all your input has to be in lowercase.

*** You have a notebook at your hand where it is recommended you write down the correct 
    answers to the questions on the notes as the previous correct answers might come in handy in one of the rooms...

Have fun!

"""
import argparse
import helper as helper
import config
# Argparsing 
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--version", help="Display program version.", action="store_true")
parser.add_argument("-i", "--info", help="Description of the game", action="store_true")
parser.add_argument("-a", "--about", help="Info about the developer", action="store_true")
parser.add_argument("-c", "--cheat", help="Get cheats for the game", action="store_true")
args = parser.parse_args()
if args.version:
    print("Version 0.2 BETA")
    exit() # without exit() the main funct starts.
if args.info:
    print(__doc__)
    exit()
if args.about:
    print("Hi! I'm Daniel and i'm the developer of this game.")
    print("I study at BTH and this game is the final project for the course in programming with python.")
    exit()
if args.cheat:
    print("Soo you've decided to cheat, huh?\nHere's how you do it:")
    print("All doors require you to shout the correct answer.")
    print("If you know the right answer beforehand")
    print("you don't have to interact with objects in the rooms to find the note with the question.")
    print("\nHere's the right answers:")
    print('Room1: 3\nRoom2: 1977\nRoom3: christopher nolan\nRoom4: alfred\nRoom5: sean bean')
    print('Room6: james cameron\nRoom7: batty and after that 37ndnny')
    print("\nIn room 6 you have to make a jump to get to the door. Type 'fly' in that room to skip the jump.")
    print('In the first room you can type "room 7" to go directly to the last room.\n')
    exit()
def room1():
    """
    You are now standing in the first room. It is very dark and scary.
    Suddenly your guide Robo appears out of thin air and he tells you that he is your guide thoughout the game.
    Here in the first room the task is very simple. 
    Robo says he's just gonna ask you a rather simple movie related question and 
    if you answer correctly you can enter the next room.
    *** Remember to write down the right answer in your notebook. Type 'help' or 'notebook' for more info. ***
    """
    room1_choice = input('\n>>> ')

    if room1_choice == 'help':
        helper.choices()
        room1()
    elif room1_choice == 'info':
        print('Not much to say about this room. Its kinda like a tutorial area.')
        room1()
    elif room1_choice == 'forward':
        if config.question_room1 == 0:
            print('You cant go forward until you answer the question right')
            room1()
        else:
            print(chr(27) + "[2J" + chr(27) + "[;H")
            print(room2.__doc__)
            room2()
    elif room1_choice == 'back':
        print('If you go back to the main menu all the doors will shut.')
        print('Still wanna go back? yes? no?')
        are_you_sure = input('\n>>> ')
        if are_you_sure == 'yes':
            print('You are going back to the main menu.')
            main()
        elif are_you_sure == 'no':
            print('You are staying in room 1.')
            room1()
        else:
            print('Invalid input')
            room1()
    elif room1_choice == 'look':
        print('Nothing to see in this tutorial room. Try and answer Robos question.')
        room1()
    elif room1_choice == 'clue':
        print('There are 3 Lord of the Rings movies. To move on to the next level type "shout 3" ')
        room1()
    elif room1_choice == 'shout 3':
        config.question_room1 = 1
        print('Well done. Room 1 is completed. You can now move forward.')
        room1()
    elif room1_choice == '3':
        print('That is the correct answer. Try and shout it so the door to the next room opens.')
        room1()
    elif room1_choice == 'quit':
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print('You have quit the game.')
    elif room1_choice == 'q':
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print('You have quit the game.')
    elif room1_choice == 'room 7':
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(room7.__doc__)
        room7()
    elif room1_choice == 'notebook':
        helper.notebook_text()
        helper.notebook()
        room1()
    else:
        print('That is not valid input. Try entering help or clue to progress with the game.')
        room1()

def room2():
    """
    You are now in the 2nd room and after the first room you are feeling confident about finishing the 
    game because of the first simple question Robo gave you.
    Robo is silent in this room though annd you might have to look around to see what you are suppose to do in here...
    """
    room2_choice = input('\n>>> ')
    if room2_choice == 'help':
        helper.choices()
        print('\nFrom this room and anwards you might interact with objects.')
        print('The commands for that is as follows:')
        helper.object_choices()
        room2()
    elif room2_choice == 'info':
        print('This is the second room and last tutorial room.')
        room2()
    elif room2_choice == 'forward':
        if config.question_room2 == 0:
            print('You cant go forward until you get the question right.')
            room2()
        else:
            print(chr(27) + "[2J" + chr(27) + "[;H")
            print(room3.__doc__)
            room3()
    elif room2_choice == 'back':
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(room1.__doc__)
        room1()
    elif room2_choice == 'look':
        print('You look around and see an old barrel in the corner.')
        print('To get a list how to interact with the barrel type help.')
        print('If you are uncertain about how to proceed type clue.')
        room2()
    elif room2_choice == 'clue':
        if config.clue_room2 == 0:
            print('Ok. You are suppose to "kick barrel" to expose a note.')
            print('Then you have to "read note" to read the question. Answer correctly by "shout" the correct answer.')
            room2()
        else:
            print('The right answer is 1977.')
            room2()
    elif room2_choice == 'object':
        print('There is just the old barrel in the room.')
        room2()
    elif room2_choice == 'look barrel':
        print('The barrel is old and fragile. You see inbetween the woodplanks a note inside the barrel.')
        room2()
    elif room2_choice == 'open barrel':
        print('The barrel cannot be opened. Maybe if you try and open it with a little force...')
        room2()
    elif room2_choice == 'kick barrel':
        print('You kick the barrel open with a few kicks. You can now see and read the note.')
        config.barrel_room2 = 1 # Once the barrel is kicked you can interact with the note
        room2()
    elif room2_choice == 'move barrel':
        print('There is really no point in moving the barrel.')
        room2()
    elif room2_choice == 'read note':
        if config.barrel_room2 == 0:
            print('You cannot read the note since its inside the barrel. Try something else.')
            room2()
        else:
            print('You read the note and it says:\nWhen was the first Star Wars movie released? ')
            config.clue_room2 = 1 # Change the clue to give a the correct answer
            room2()
    elif room2_choice == '1977':
        print('That is the correct answer! Try shouting it to open the door.')
        room2()
    elif room2_choice == 'shout 1977':
        config.question_room2 = 1
        print('You shout: 1977!!!!! as the door to the next room opens.')
        room2()
    elif room2_choice == 'q':
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print('You have quit the game')
    elif room2_choice == 'quit':
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print('You have quit the game')
    elif room2_choice == 'notebook':
        helper.notebook_text()
        helper.notebook()
        room2()
    else:
        print('That is not valid input')
        room2() 

def room3():
    """
    You are now in the 3rd room of 7. Feeling cocky yet? It's not been so hard yet has it?
    Up until now you've been kinda guided through the game. Time to step it up!
    """
    room3_choice = input('\n>>> ')
    if room3_choice == 'help':
        helper.choices()
        helper.object_choices()
        room3()
    elif room3_choice == 'info':
        print('This room, unlike the other previous rooms, are fully lit. You notice the room is very small')
        room3()
    elif room3_choice == 'forward':
        if config.question_room3 == 0: #Is the room done yet or not?
            print('You cannot go forward as of yet.')
            room3()
        else:
            print(chr(27) + "[2J" + chr(27) + "[;H")
            print(room4.__doc__)
            room4()
    elif room3_choice == 'back':
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(room2.__doc__)
        room2()
    elif room3_choice == 'look':
        print('You look around and see two boxes stacked on eachother. Nothing else')
        room3()
    elif room3_choice == 'clue':
        if config.clue_room3 == 0:   
            print('Maybe the note is in one of the boxes?')
            print('The boxes are not one obeject. They are named first box and second box.')
            room3()
        else:
            print('Psst! christopher nolan directed the dark knight trilogy.')
            room3()
    elif room3_choice == 'object':
        print('You see 2 boxes stacked on eachother in the middle of the small room')
        room3()
    elif room3_choice == 'look boxes':
        print('The first box on the top has a label "Empty" while the second box below has a label "Important".')
        print('You think to yourself that the note might be in the second box.')
        room3()
    elif room3_choice == 'open first box':
        print('You open the first box and as the label suggested it is empty...')
        room3()
    elif room3_choice == 'open second box':
        if config.box1 == 0: #You cannot open the second box until you move or kick the first box
            print('You cannot open the second box until you have moved the first box.')
            room3()
        else:
            print('You open the second box and find the note.')
            config.note_room3 = 1 #Make the note available.
            room3()
    elif room3_choice == 'kick first box':
        print('You kick the first box and it hits the floor and slides away a bit')
        config.box1 = 1 # The first box is now moved and the second box is available for open command
        room3()
    elif room3_choice == 'kick second box':
        print('Really no need to kick the second box around. Try opening it instead')
        room3()
    elif room3_choice == 'move first box':
        print('You move the first box, making the second box openable')
        config.box1 = 1 #Move first box and make the second box available for interaction
        room3()
    elif room3_choice == 'move second box':
        print('No need to move around the second box. Try to open it instead')
        room3()
    elif room3_choice == 'read note':
        if config.note_room3 == 0: # if you somehow try to read the note before you have interacted with the boxes
            print('Hey now! You are not suppose to able to read the note as of yet...')
            room3()
        else:
            print('You read the note:')
            print('Who directed the "Dark Knight" trilogy?')
            config.clue_room3 = 2
            room3()
    elif room3_choice == 'christopher nolan':
        print('Correct! try and shout your answer. You should know this by now...')
        room3()
    elif room3_choice == 'shout christopher nolan':
        print('You shout: CHRISTOPHEEEER NOOOLAN! as the door to the next room opens.')
        config.question_room3 = 1 # room is now completed and you can move on.
        room3()
    elif room3_choice == 'q':
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print('You have quit the game')
    elif room3_choice == 'quit':
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print('You have quit the game')
    elif room3_choice == 'notebook':
        helper.notebook_text()
        helper.notebook()
        room3()
    else:
        print("That's not a valid command.")
        room3()

def room4():
    """
    You are now in the 4th room. Robo pats you on the back and says you are on your way to finish the game.
    """
    room4_choice = input('\n>>> ')
    if room4_choice == 'help':
        helper.choices()
        helper.object_choices()
        room4()
    elif room4_choice == 'info':
        print('This room is small and not as cold as the previous rooms.')
        room4()
    elif room4_choice == 'back':
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(room3.__doc__)
        room3()
    elif room4_choice == 'forward':
        if config.question_room4 == 0:
            print('You cannot go forward as of yet.')
            room4()
        else:
            print(chr(27) + "[2J" + chr(27) + "[;H")
            print(room5.__doc__)
            room5()
    elif room4_choice == 'look':
        print('You look around and see a note on the floor.')
        room4()
    elif room4_choice == 'clue':
        if config.clue_room4 == 0:
            print('Maybe interact with the note somehow.')
            room4()
        else:
            print('The answer is "alfred".')
            room4()
    elif room4_choice == 'object':
        print('All you can see is the single note lying on the middle of the floor in the room.')
        room4()
    elif room4_choice == 'look note':
        print('The note is really small.')
        room4()
    elif room4_choice == 'read note':
        print('The note is very small and reads:')
        print('What is the first name of Batmans butler?')
        room4()
    elif room4_choice == 'open note':
        print('Cannot open the note.')
        room4()
    elif room4_choice == 'kick note':
        print('Nothing to kick unless you like to kick around a small note... Focus on what the note says.')
        room4()
    elif room4_choice == 'move note':
        print('No need to move around the note. Focus on what the note says')
        room4()
    elif room4_choice == 'alfred':
        print("Well aren't you a smart person! You solved the rather simple puzzle.\nAs always: shout your answer")     
        room4()
    elif room4_choice == 'shout alfred':
        print('You shout "AAAAAALFREEEEED!" as loud as you can and the door to the next room opens')
        config.question_room4 = 1
        room4()
    elif room4_choice == 'q':
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print('You have quit the game.')
    elif room4_choice == 'quit':
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print('You have quit the game.')
    elif room4_choice == 'notebook':
        helper.notebook_text()
        helper.notebook()
        room4()
    else:
        print('Thats not valid input. Try again or type help.')
        room4()

def room5():
    """
    This is the 5th room and you're almost finished with the game! All the rooms are starting to look the same to you.
    The walls are all the same. The stonefloors are all cold and very hard beneath your feet.
    Robo tells you to look around because he can see something in this room...
    """
    room5_choice = input('\n>>> ')
    # The alternatives to user input
    if room5_choice == 'help':
        helper.choices()
        helper.object_choices()
        room5()
    elif room5_choice == 'info':
        print(room5.__doc__)
        room5()
    elif room5_choice == 'forward':
        if config.question_room5 == 0:
            print('You cannot go forward as of yet.')
            room5()
        else:
            print(chr(27) + "[2J" + chr(27) + "[;H")
            print(room6.__doc__)
            room6()
    elif room5_choice == 'back':
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(room4.__doc__)
        room4()
    elif room5_choice == 'look':
        print('You look around and see a large cabinett in the middle of the room.')
        room5()
    elif room5_choice == 'clue':
        if config.clue_room5 == 0:
            print('Maybe the note is in the cabinett?')
            room5()
        elif config.clue_room5 == 1:
            print('Look again in the cabinett.')
            room5()
        else:
            print('Psst! The correct answer is Sean Bean')
            room5()
    elif room5_choice == 'object':
        print('The only object you can see is the cabinett in the middle of the room.')
        room5()
    elif room5_choice == 'look cabinett':
        if config.clue_room5 == 1:
            print('You look inside and see a note on the cabinett floor.')
            room5()
        else:
            print("You approach the cabinett. It doesnt seem locked.")
            room5()
    elif room5_choice == 'look note':
        if config.note_room5 == 0:
            print("You can't see the note yet.")
            room5()
        else:
            print('The note is small and covered in dust.')
            room5()
    elif room5_choice == 'open cabinett':
        print('You slowly reach and try to open the cabinett.')
        print('You sigh with relief as the cabinett is not locked and you open it up.')
        config.note_room5 = 1 # The cabinett is now opened and you can read the note.
        config.clue_room5 = 1 # Clue changes.
        room5()
    elif room5_choice == 'kick cabinett':
        print('On second though... No need to kick the cabinett.')
        room5()
    elif room5_choice == 'move cabinett':
        print("You can't move the cabinett. It's too heavy.")
        room5()
    elif room5_choice == 'read note':
        if config.note_room5 == 0:
            print("You can't read the note since the cabinett is closed.")
            room5()
        else:
            print('You remove the dust from the note with you hand and read:')
            print("Who playes Boromir in Peter Jackson's The Lord of the Rings?")
            config.clue_room5 = 2 #The clue now gives the right answer.
            room5()
    elif room5_choice == 'sean bean':
        print("That's the right answer! As always..Shout it!")
        room5()
    elif room5_choice == 'shout sean bean':
        print("You shout: SEAAAAAN BEEEEEEAN!!!! as the door to the next room opens.")
        config.question_room5 = 1 #The door is now open as you have answered correctyly.
        room5()
    elif room5_choice == 'q':
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print('You have quit the game.')
    elif room5_choice == 'quit':
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print('You have quit the game.')
    elif room5_choice == 'notebook':
        helper.notebook_text()
        helper.notebook()
        room5()
    else:
        print("That's not valid input.")
        room5()

def room6():
    """
    You are now standing in the 6th room of seven and you can almost see the finishline.
    Robo pats you on your shoulder and says: 
    "Well done so far! Hope you have learned something from all the questions
    or did you already know the answers?"
    
    This room is not like the other rooms. The first thing you see is that 
    the wall with the door facing the final room is made of some kind of transparent material.
    You squint your eyes and see in the 7th and final room only a pedestal in the middle of the room.
    You think to yourself that: "Huh, the final room doesn't seem to hard..."

    You see that you will have to do some jumping in this room. 
    To get to the other side of the room where you can see the note you will have to jump across the room.
    The command "jump" will let you try to jump across the room.
    """
    from random import randint
    jump_other_side = randint(1, 5)
    room6_choice = input('\n>>> ')
    # The choices
    if room6_choice == 'help':
        helper.choices()
        helper.object_choices()
        room6()
    elif room6_choice == 'info':
        print(room6.__doc__)
        room6()
    elif room6_choice == 'forward':
        if config.jump_room6 == 0:
            print('You cannot go to the next room since you are not across the room yet.')
            room6()
        elif config.question_room6 == 0:
            print('You cannot go to the next room yet.')
        elif config.question_room6 == 1:
            print('You cannot go to the next room yet.')
            room6()
        else:
            print(chr(27) + "[2J" + chr(27) + "[;H")
            print(room7.__doc__)
            room7()
    elif room6_choice == 'back':
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(room5.__doc__)
        room5()
    elif room6_choice == 'look':
        print('You look around. Nothing to do in this room but jump to the platform.')
        print('You see a small ladder to your left which tells you that if you fail to jump you can try again.')
        room6()
    elif room6_choice == 'clue':
        if config.clue_room6 == 0:
            print('You have to try and jump over to the other side of the room')
            print('You have a new command to help you jump and that is:\njump')
            room6()
        else:
            print('Psst! james cameron is correct.')
            room6()
    elif room6_choice == 'q':
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print('You have exit the game.')
    elif room6_choice == 'quit':
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print('You have exit the game.')
    elif room6_choice == 'jump':
        if jump_other_side == 2:
            print('Your mind is focused on making this jump...You run and you...')
            print('Phew! You made the jump. You can now read the note!')
            print("You look behind yourself and see that the")
            print("floor rearranged itself and you don't have to jump anymore in this room.")
            config.question_room6 = 1
            config.jump_room6 = 1
            room6()
        else:
            print('Your mind is focused on making this jump..You run and you...')
            print('...did not make the jump and you have to try again.')
            room6()
    elif room6_choice == 'read note':
        if config.question_room6 == 1:
            print('You read the note and it says:')
            print('Who directed Terminator 2?')
            config.clue_room6 = 1
            room6()
        else:
            print('You cannot read the note since it is across the room.')
            room6()
    elif room6_choice == 'object':
        print('Nothing to interact with in this room except the note.')
        room6()
    elif room6_choice == 'james cameron':
        print('That is correct. As always: SHOOUUT IT!')
        room6()
    elif room6_choice == 'shout james cameron':
        print('You shout: JAAAAAMES CAAAAAMEROOOON!! as the door to the next room opens')
        config.question_room6 = 2
        room6()
    elif room6_choice == 'fly':
        print('Cheatcode fly acivated!')
        print('Flying over the room and skipping the jump..')
        config.jump_room6 = 1
        config.question_room6 = 1
        room6()
    elif room6_choice == 'notebook':
        helper.notebook_text()
        helper.notebook()
        room6()
    else:
        print('That is not valid input.')
        room6()

def room7():
    """
    You are finally in the 7th and last room. 
    You see the pedestal in the middle of this room just like you saw it from the 6th room
    and it doesn't seem to be any harder than just read the note and answer the question.
    Robo is cautious and think's that that surely the last and final room has to be harder than this?
    No jumping? No hidden notes?
    """
    room7_choice = input('\n>>> ')
    # The choices
    if room7_choice == 'help':
        helper.choices()
        helper.object_choices()
        room7()
    elif room7_choice == 'info':
        print(room7.__doc__)
        room7()
    elif room7_choice == 'forward':
        if config.question_room7 == 0:
            print("You're in the last room.")
            room7()
        else:
            print('You step through the door and win')
            room7()
    elif room7_choice == 'back':
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(room6.__doc__)
        room6()
    elif room7_choice == 'look':
        print('You look around and can only se the pedestal in the middle of the room.')
        print('This room however has a small crack in the roof')
        print('A beam of light shines though and shines on the pedestal.')
        room7()
    elif room7_choice == 'clue':
        if config.clue_room7 == 0:
            print("Doesn't seem to be much to do in this room except to read the note...")
            room7()
        elif config.clue_room7 == 1:
            print("Would the genre of the movie help? It's a sci-fi movie. ")
            config.clue_room7 += 1
            room7()
        elif config.clue_room7 == 2:
            print('Another clue to help you figure out the movie.')
            print('Harrison Ford is in both this movie and the movie from room 2.')
            print('Although it is not Ford who delivers the quote.')
            config.clue_room7 += 1
            config.reward = 4
            room7()
        elif config.clue_room7 == 3:
            print('Rutger Hauer is the actor whose character delivers the quote.')
            config.clue_room7 += 1
            config.reward = 3
            room7()
        elif config.clue_room7 == 4:
            print("Hauer's character first name is Roy and his last name is very similar to 'Betty'.")
            config.clue_room7 += 1
            config.reward = 2
            room7()
        else:
            print("Hmm.. You're not gonna get a high reward since you needed this many clues.")
            print("The correct answer is: batty.")
            config.reward = 1
            room7()
    elif room7_choice == 'q':
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print('You have exit the game.')
    elif room7_choice == 'quit':
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print('You have exit the game.')
    elif room7_choice == 'read note':
        print("You slowly pick up the note and read:")
        print("\nSoo you have finally reached the last room. I guess congratulations are in order.")
        print("There's just one last question standing in your way of winning the game. Do you think you'll make it?")
        print("If you thought the last question would be hard, you're right.")
        print("I saved the hardest one for last of course. ")
        print("I am willing to give you 5 clues before giving away the correct answer.")
        print("You'll be rewarded by how few clues you needed.")
        print("The question is...")
        input("\n(press enter) ")
        print("\n'Tears in rain' is part of a famous quote from a movie.")
        print("What's the last name of the character delivering the quote?")
        config.clue_room7 = 1 #Give first level of clue
        room7()
    elif room7_choice == 'object':
        print('Really not much to interact with in this room except the note.')
        room7()
    elif room7_choice == 'look pedestal':
        print("You look at the pedestal. It seems to be a very old pedestal made of white marble.")
        print("On the pedestal lays the final note with the final question to answer.")
        room7()
    elif room7_choice == 'open pedestal':
        print("Can't open it.")
        room7()
    elif room7_choice == 'kick pedestal':
        print("You try and kick the pedestal but it won't move an inch.")
        room7()
    elif room7_choice == 'move pedestal':
        print('You try and move the pedestal but it is pointless.')
        room7()
    elif room7_choice == 'batty':
        print("That's correct! Shout it loud!")
        room7()
    elif room7_choice == 'shout batty':
        print('You inhale and shout for the last time..\nBAAAAAAATTYYYYYY echoes throughout the room.')
        input('\n(press enter) ')
        print('The floor starts to shake and you suddenly hear a voice:')
        print('So you think you have finished the game now, huh?')
        print('I just need ONE more thing from you and I hope you have been paying attention from the start...')
        print('Shout the last character from every correct answer in order from the first to the last room!')
        print('\nHmm..you think to yourself. ')
        print('Hopefully you have been written down the answers in your notebook...')
        room7()
    elif room7_choice == 'shout 37ndnny':
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print('You give it your best shot and shout 37ndnny as its not that easy to pronounce it.')
        print('\n"That is correct!" says the voice as the room fills with a bright light.')
        print('It feels as if you are floating away.')
        input('(press enter) ')
        finish()
    elif room7_choice == '37ndnny':
        print('Shout it!')
        room7()
    elif room7_choice == 'notebook':
        helper.notebook_text()
        helper.notebook()
        room7()
    else:
        print('Not valid input')
        room7()


def finish():
    """
    finish
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    helper.congratulations()
    print("\nCongratulations! You've won the game!")
    print('\nBased on how many clues it got you to finish room 7 your reward is:', config.reward * 1000, 'points')
    try:
        open('notebook.txt', 'w')
        print('The notebook has been reset.')
    except IOError:
        print("Can't find the file 'notebook.txt")
    




def main():
    """
    main function
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(helper.startscreen_art())
    print(__doc__)
    print('Lets start the adventure, shall we?')
    print('\nType start to start the game or q (quit) to quit the game.')

    choice = input('\n>>> ')

    if choice == 'start':
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(room1.__doc__)
        print('Robo says:\nHow many Lord of the Rings movies are there?')   
        room1()

    elif choice == 'q':
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print('You have quit the game. Bye Bye!')
    elif choice == 'quit':
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print('You have quit the game. Bye Bye!')
    elif choice == 'notebook':
        helper.notebook()
        main()
    else:
        print('Not a valid command.')
        main()
    
if __name__ == "__main__":
    main()

