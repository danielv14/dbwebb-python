"""
Docstring
"""
import marvin as marvin

def main():
    """
    This is the main method, I call it main by convention.
    Its an eternal loop, until q is pressed. 
    It should check the choice done by the user and call a appropriate 
    function.
    """
    while True:
        marvin.menu()
        choice = input("--> ")
        keyterm = 'citat' #Get marvin to quote something
        choicelist = 'visa'
        choicenumber = 'antal'
        choiceplocka = 'plocka'
        choicekasta = 'kasta'
        words = choice.split()


        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            return
        
        elif choice == "1":
            marvin.myNameIs()

        elif choice == "age":
            marvin.calculateAge()

        elif choice == "moon":
            marvin.calculateMoon()

        elif choice == "minute":
            marvin.calculateHours()

        elif choice == "celcius":
            marvin.calculateCelcius()

        elif choice == "word":
            marvin.word()

        elif choice == "minmax":
            marvin.minmax()

        elif choice == "sum":
            marvin.sum_and_average()

        elif choice == 'grade':
            marvin.grade()

        elif choice == 'guess':
            marvin.guess()

        elif choice == 'strings':
            marvin.strings()

        elif choice == 'throw':
            marvin.throwword()

        elif keyterm in words:
            marvin.randomquote()

        elif choicelist in words:
            marvin.visaallt()

        elif choicenumber in words:
            marvin.listallnumber()

        elif choiceplocka in words:
            marvin.plockaupp()

        elif choicekasta in words:
            marvin.removeitem()
        
        else:
            print("That is not a valid choice. You can only choose from the menu.")          
            
        input("\nPress enter to continue...")

if __name__ == "__main__":
    print(main.__doc__)
    main()
