import random
import time
import sys

def print_slow(str):
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()  
        time.sleep(0.05)  

def dice_roll():
    return random.randint(1, 6)

with open("bank.txt", "r") as balance_file:
    bank = int(balance_file.read())

playing = True

while playing == True:
    if bank == 0:
        print_slow("Your balance is zero. Please deposit funds.\n")
        break

    balance_print = ("You have", "  ", str(bank), " VND \n")
    print_slow(balance_print)
    print_slow("[1] High \n[2] Low \n[3] Exit\n")

    try:
        a = int(input())
    except ValueError:
        print_slow("Invalid input.\n")
        continue

    if a == 1 or a == 2:
        print_slow("Enter your bet: ")
        try:
            bet = int(input())
        except ValueError:
            print_slow("Invalid input. Please enter a number.\n")
            continue

        if bet > bank:
            print_slow("Insufficient balance.\n")
            continue
        if bet <= 0 or bet % 1000 != 0:
            print_slow("Invalid bet amount.\n")
            continue

        print_slow("Rolling the dice...\n")
        time.sleep(2)
        dice_1 = dice_roll()
        dice_2 = dice_roll()  
        dice_3 = dice_roll()
        total = dice_1 + dice_2 + dice_3

        print_slow("Dice 1: " + str(dice_1) + "\n")
        print_slow("Dice 2: " + str(dice_2) + "\n")  
        print_slow("Dice 3: " + str(dice_3) + "\n")
        print_slow("Total is: " + str(total) + "\n")

        if total > 10 and total < 18:
            if a == 1:
                print_slow("You win!\n")
                bank += bet
            else:
                print_slow("You lose!\n")
                bank -= bet

        elif total < 11 and total > 3:
            if a == 2:
                print_slow("You win!\n")
                bank += bet
            else:
                print_slow("You lose!\n")
                bank -= bet

    with open("bank.txt", "w") as balance_file:
        balance_file.write(str(bank))

    if a == 3:
        print("Exiting game.")
        playing = False
