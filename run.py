from game import gameplay

if __name__ == "__main__":
    print("""Welcome to DEAD AND WOUNDED!!!
    Try to guess the four digit numbers with no duplicate values\n""")

    response = 'Y'
    # checking if to continue playing game or exit
    while response == "Y" or response == "YES":
        gameplay()
        print("")
        response = input("Would you like to play again? (Y/N): ").upper()
        print("")
    else:
        print("Thank You for Playing!")