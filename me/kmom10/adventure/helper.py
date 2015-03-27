"""
This is the helper file that will be loaded if you type help.
"""

def choices():
    """
    description of the choices you can do in a room
    """
    print('\nRobo says that in every room you have som helping commands:\n')
    print('info)                get a description of the room.')
    print('help)                get a list of available commands.')
    print('forward)             go forward to the next room if its unlocked.')
    print('back)                go back to previous room.')
    print('look)                look around.')
    print('clue)                get a clue to how you complete this room.')
    print('shout <your answer>) shout your answer to open the door to the next room.')
    print('notebook)            Open your notebook where you can write down answers.')

def object_choices():
    """
    Print ways to interact with objects
    """
    print('\nRobo says that you can interact with objects like this:\n')
    print('object)              See all the objects in the room')
    print('look <object-name>)  Get a description of the object')
    print('open <object-name>)  Open the object if possible')
    print('kick <object-name>)  Kick the object if possible')
    print('move <object-name)   Move the object if possible')
    print('read note)           Read the note to get movie related question. The note can only be read.')



def notebook_text():
    """
    notebook helper text to print first time you open the notebook
    """
    print('What would you like to do with the notebook?')
    print('You can interact with the notebook with the following commands: read, write and delete.')
    print("When you're done type 'done' to get back to the current room.")
    print("Type 'help' to get some info about how the notebook works.")


def notebook():
    """
    notebook to write down the right answers
    """
    notebook_choice = input('\n>>> ')

    if notebook_choice == 'read':
        notebook_read = open('notebook.txt', 'r')
        print('\nYou read the content from your notebook:\n')
        print(notebook_read.read()) 
        notebook()   

    elif notebook_choice == 'write':
        notebook_append = open('notebook.txt', 'a')
        print('What do you want to write down?')
        content = input('\n>>> ')
        notebook_append.write(content)
        notebook_append.write('\n')
        notebook_append.close()
        print("You take out your pen and write down:")
        print(content)
        notebook()

    elif notebook_choice == 'done':
        print("You put the notebook back in your pocket and can now interact with the room again.")

    elif notebook_choice == 'delete':
        try:
            open('notebook.txt', 'w')
            print('The notebook has been reset.')
            notebook()
        except IOError:
            print("Can't find the file 'notebook.txt")
            notebook()

    elif notebook_choice == 'help':
        print('You can either read your notebook or write new lines to it.')
        print("You can also delete all the content from the notebook.")
        print("Be aware as this command erases all the content of the notebook.")
        print("When you're done with the notebook you can have to put it away to go on with the room..")
        print('The idea is to write down the correct answers from all the rooms to your notebook')
        print('The Commands are:')
        print('help)    view this text.')
        print('read)    read content of the notebook.')
        print('write)   write something down in the notebook.')
        print('done)    put the notebook away and continue with the room.')
        print('\nA tip is to write like this:')
        print("Room 1: your-answer")
        print("This makes the note easier to read and understand as it's organized better.")
        notebook()
    
    else:
        print("That's not valid input.")
        notebook()


def startscreen_art():
    """
    Ascii art for start screen
    """
    return r"""
      __  __         _                 _    
     |  \/  |_____ _(_)___   __ _ _  _(_)___
     | |\/| / _ \ V / / -_) / _` | || | |_ /
     |_|  |_\___/\_/|_\___| \__, |\_,_|_/__|
                               |_|          
    """
                   

def congratulations():
    """
    Ascii art for finished game
    """
    art = '''\

    ╔═══╗──────────────╔╗───╔╗────╔╗
    ║╔═╗║─────────────╔╝╚╗──║║───╔╝╚╗
    ║║─╚╬══╦═╗╔══╦═╦══╬╗╔╬╗╔╣║╔══╬╗╔╬╦══╦═╗
    ║║─╔╣╔╗║╔╗╣╔╗║╔╣╔╗║║║║║║║║║╔╗║║║╠╣╔╗║╔╗╗
    ║╚═╝║╚╝║║║║╚╝║║║╔╗║║╚╣╚╝║╚╣╔╗║║╚╣║╚╝║║║║
    ╚═══╩══╩╝╚╩═╗╠╝╚╝╚╝╚═╩══╩═╩╝╚╝╚═╩╩══╩╝╚╝
    ──────────╔═╝║
    ──────────╚══╝
    
    '''
    print(art)









