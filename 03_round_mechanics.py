import random


def check_rounds():
        while True:
            response = input("How many rounds: ")
            print()

            round_error =  "Please type either <enter> " \
                           "or an integer that is more than 0\n"
            
            # if infinite mode not chosen, check response
            # Is an integer that is more than 0
            if response != "":
                try:
                    response = int(response)

                
                    if response <1:
                        print(round_error)
                        continue

                except ValueError:
                    print(round_error)
                    continue

            return response


def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
         print("Please answer yes / no")


def instructions():
    print("**** How to Play ****")
    print()
    print("*** Instructions ** *")


    print()
    print ("**To begin with the computer will ask you to choose a number of rounds OR press < enter > for infinite mode ** ")
    print()
    print("**Next you will guess a number, once selecting what numbers you will be guessing between(high and low number) ** ")
    print()
    print("**If your number is too high the computer will tell you to go lower, and visa versa, until you guess the correct number ** ")
    print()
    return ""


# Main routine goes here...
Played_before = yes_no("Have you played this game before?")


if Played_before == "no":
    instructions()

print("Program continues")
# Main routine goes here...

rounds_played = 0
choose_instruction = "Guess a number: "
# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Rounds heading
    print ()
    if rounds == "":
        heading = "Continuous Mode: " \
                  "Round{}".format(rounds_played)
        print(heading)
        choose = input("{} or 'xxx' to end: ".format(choose_instruction))
        if choose == "xxx":
            break
    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)
        print(heading)
        choose = input(choose_instruction)
        if rounds_played == rounds - 1:
            end_game = "yes"


    # rest of loop / game
    print("You chose {}".format(choose))

    rounds_played += 1

print("Thank you for playing")