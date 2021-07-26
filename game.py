import random


def generate_number():
    ran_values = random.sample(range(10), 4)
    ran_value = ""
    for i in ran_values:
        ran_value += str(i)

    return ran_value


def state_count(word, letter):
    count = 0
    for char in word:
        if letter == char:
            count += 1
    return count


def gameplay():
    value = generate_number()
    guessed_num = ""
    result = ""
    dead_count = 0
    wounded_count = 0

    while guessed_num != value:

        guessed_num = input("What is your guessed number: ")

        if guessed_num.strip().isdigit():

            if len(guessed_num) > len(value):
                print(f"\n{guessed_num} is more than (4) digits, please input a 4-digits number\n")

            elif len(set(guessed_num)) < len(value):
                print(f"\n{guessed_num} has duplicate values, please input a no duplicate value number\n")

            else:
                for i in range(len(guessed_num)):
                    if guessed_num[i] in value:
                        if i == value.index(guessed_num[i]):
                            result += 'd'
                        else:
                            result += 'w'
                    else:
                        continue

                dead_count = state_count(result, 'd')
                wounded_count = state_count(result, 'w')
                print(f'{guessed_num} : {dead_count} dead, {wounded_count} wounded')
                print("")
                # print(value)
                result = ""
        else:
            print(f"\n{guessed_num} is not a number, please input a 4-digits number\n")

    print("Congrats! you guessed the number right.")
