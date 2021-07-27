""" The run file to initialize the game """

from game import gameplay

if __name__ == "__main__":
    print("""Welcome to DEAD AND WOUNDED!!!
    You are to guess the n-digits number with no duplicate values
    The n-digits number is determined by three difficulty levels
    Easy = 4-digits, Medium = 5-digits, Hard = 6-digits
    """)

    response = 'Y'
    # check to continue or exit game
    while response == "Y" or response == "YES":
        gameplay()
        print("")
        response = input("Would you like to play again? (Y/N): ").upper()
        print("")

    # end of game
    print("Thank You for Playing!")