import random
import math
from tkinter import Y

def intcheck(question, low=None, high=None, exit_code = None):

    while True:

        # sets up error messages
        if low is not None and high is not None:
            error = "Please enter an integer between {} and {} (inclusive)".format(low, high)
        elif low is not None and high is None:
            error = "Please enter an integer that is more than or equal to {}".format(low)
        elif low is None and high is not None:
            error = "Please enter an integer that is less than or equal to {}".format(high)
        else:
            error = "Please enter an integer"

        try:
            response = input(question)
            
            # check to see if response is the exit code and return it
            if response == exit_code:
                return response
            
            # change the response into an integer
            else:
                response = int(response)

            # Checks response is not too low, not use of 'is not' keywords
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        # checks input is a integer
        except ValueError:
            print(error)
            continue


def check_rounds():
        while True:
            response = input("How many rounds or <enter> for infinite mode: ")
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
    print("*** Instructions ***")


    print()
    print ("***To begin with the computer will ask you to choose a number of rounds OR press < enter > for infinite mode *** ")
    print()
    print("***Next you will guess a number, once selecting what numbers you will be guessing between(high and low number) *** ")
    print()
    print("***If your number is too high the computer will tell you to go lower, and visa versa, until you guess the correct number *** ")
    print()
    return ""


def choice_checker(question, valid_list, error):


    valid = False
    while not valid:

        # Ask user for choice (and put in lowercase)
        response = input(question).lower()

        # In the list (or the first letter of an item)
        # Full item name is returned
        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # Output error if item not in list 
        print("item is not in list")
        print(error)
        print()

# list of valid responses
yes_no_list = ["yes", "no"]
game_summary = []

# stores number of guesses used for each round
#used to calculate min/max/average stats
all_game_guesses = []

print("****Welcome to the Higher Lower Game****")
print()

played_before = choice_checker("Have you played this game before? Please enter yes or no. ", yes_no_list, "Please enter yes / no")
print()

if played_before == "no":
    instructions()

# checks that response is an integer
low_num = intcheck("Low Number: ")
print("You chose a low number of ", low_num)

rounds_played = 0
rounds_lost = 0
rounds_won = 0
# checks that response is an integer more than the low number
high_num = intcheck("High Number: ", low_num+1)
print("You chose a high number of ", high_num)


# works out max guesses based on user selected range
var_range = high_num - low_num + 1
max_raw = math.log2(var_range)  # finds maximum # of guesses using
max_upped = math.ceil(max_raw)  # rounds up ( ceil -> ceiling)
max_guesses = max_upped + 1
print("Max Guesses: {}".format(max_guesses))

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()
if rounds == "":
    mode = "infinite"
    rounds = 5
else:
    mode = "regular"



end_game = "no"
while end_game == "no":

    # Rounds heading     
    print ()
    if mode == "infinite":
        heading = "Continuous Mode: " \
                  "Round{}".format(rounds_played)
        print(heading)
        rounds += 1

    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)
        print(heading)


    guess = ""

    secret = random.randint(low_num, high_num)
    numbers_guessed = []
    # rounds heading 


    print("spoiler alert", secret)
    print()

    rounds_lost = rounds_played - rounds_won

    # guessing loop starts here
    while guess != secret and len(numbers_guessed) != max_guesses:

        guess_instruction = "Guess a number between {} and {}: ".format(low_num, high_num)

        # checks that the response is either the exit code
        # or a number between low_num and high_num
        guess = intcheck(guess_instruction, low_num, high_num, "xxx")
        if guess =="xxx":
            end_game = "yes"
            break
        
        if guess in numbers_guessed:
            print("you already guessed this")
            continue

        if guess not in numbers_guessed:
           numbers_guessed.append(guess)

        if guess == secret:
            print("You got it!")
            rounds_won +=1


        if guess == "xxx":
            end_game = "yes"
            break

        if guess < secret: 
            print("Hint: Higher, Guesses left {}".format(
                max_guesses - len(numbers_guessed)))
        elif guess > secret:
            print("Hint: Lower, Guesses left {}".format(
                max_guesses - len(numbers_guessed)))

        # check if they have lost
        if len(numbers_guessed) == max_guesses:
            print("Sorry you have run out of guesses")
        

    if len(numbers_guessed) > 0:

        all_game_guesses.append(len(numbers_guessed))

    if end_game == "yes":
        break
    
    rounds_played += 1

    if rounds_played == rounds:
        break


#finding smallest number

s_num = min(all_game_guesses)
s_num_max = max(all_game_guesses)
average = sum(all_game_guesses) / len(all_game_guesses)


print()
print("         !!game statistics!!          ")
print()
print("all guesses taken per round", all_game_guesses)
print("The smallest number of gueeses in any given round was: ", s_num)
print("The largest number of gueeses in any given round was: ", s_num_max)
print("Average number of guesses per round: {:.2f}".format(average))


if rounds_played == 0:
    print("You chickened out")
else:
    percent_win = rounds_won / rounds_played * 100
    percent_lose = rounds_lost / rounds_played * 100


print("******** Game Summary ********")
for item in game_summary:
    print(item)

# displays game stats with % valuse to the nearest whole number
print("******* Game statistics ********")
print("Win: {}, ({:.0f}%) \nLoss: {}, ({:.0f}%)".format(rounds_won, percent_win, rounds_lost,percent_lose))
                                         

print()
print("Thank you for playing")
