import random


def generate_number(level):
    """
    A function to generate a n-digits number with no duplicates determined by level
    where zero could also be a leading number
    :param level: (int) determines the value n for the n-digits
    :return: (string) concatenated string of the randomly generated n-digits number
    """
    # generates a unique n-digits number from the range value without replacement in a list
    ran_values = random.sample(range(10), level)
    ran_value = ""
    for i in ran_values:
        # concatenate each int element in the list while parsing it as a string
        ran_value += str(i)

    return ran_value


def difficulty(level):
    """
    This function determines the n-digits number to generate based on difficulty level
    :param level: (int) determines the n-digits to be generated by the number generator
    :return: (string) n-digits based on difficulty level
    """
    e, m, h = 4, 5, 6
    easy_level = generate_number(e)
    medium_level = generate_number(m)
    hard_level = generate_number(h)

    if level == e:
        return easy_level
    elif level == m:
        return medium_level
    else:
        return hard_level


def gameplay():
    """
    Dead and Wounded gameplay:
        A n-digits random number is generated by computer as specified by difficulty
        A user is to guess the right numbers at the right indexes
        hints are provided by the computer if some numbers are guessed right
        also hints are provided if the index position of the numbers are right or wrong
        'dead' hint shows that a digit is present and at the right index
        'wounded' hint shows that a digit is present but at the wrong index
        user keeps submitting a guess until the correct value is guessed right
    Rules:
        no letters or punctuations allowed in the n-digits only integers allowed
        only the required n-digits number is allowed, no more or less
        no duplicate values are allowed in number
    :return: None
    """
    difficulty_level = int(input("Enter your difficulty level (4 or 5 or 6): "))

    print(f"Thank you! Now guess the {difficulty_level}-digits number\n")

    value = difficulty(difficulty_level)  # randomly generated number
    guessed_num = ""  # guessed number

    # dead or wounded count to provide user with hints
    dead_count = wounded_count = 0

    while guessed_num != value:

        guessed_num = input("What is your guessed number: ")

        # rules check
        # checks if guessed number contains numbers only
        if guessed_num.strip().isdigit():

            # checks the length of guessed number if more or less
            if len(guessed_num) > len(value) or len(guessed_num) < len(value):
                print(f"\n{guessed_num} is more or less than ({difficulty_level}) digits, please input a {difficulty_level}-digits number\n")

            # checks if guessed number contains duplicate values
            elif len(set(guessed_num)) < len(value):
                print(f"\n{guessed_num} has duplicate values, please input a no duplicate value number\n")

            # proceeds with gameplay if rules are met
            else:
                # checks if guessed number has the correct values and at the right index
                for i in range(len(guessed_num)):
                    if guessed_num[i] in value:
                        if i == value.index(guessed_num[i]):
                            dead_count += 1
                        else:
                            wounded_count += 1
                    else:
                        continue
                # prints hint at every attempt
                print(f'{guessed_num} : {dead_count} dead, {wounded_count} wounded')
                print("")
                dead_count = wounded_count = 0
        else:
            print(f"\n{guessed_num} is not an integer number, please input a {difficulty_level}-digits number\n")

    # guessed number is equal to value
    print("Congrats! you guessed the number right.")
