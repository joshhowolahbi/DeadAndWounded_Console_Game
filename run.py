""" The run file to initialize the game """

from game import gameplay

if __name__ == "__main__":
    print("""Welcome to DEAD AND WOUNDED!!!
    Try to guess the four digits number with no duplicate values\n""")

    response = 'Y'
    # check to continue or exit game
    while response == "Y" or response == "YES":
        gameplay()
        print("")
        response = input("Would you like to play again? (Y/N): ").upper()
        print("")

    # end of game
    print("Thank You for Playing!")