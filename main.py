# code the gamblers fallacy using a monte carlo simulation to show that the probability of a coin flip is 50/50 regardless of previous flips

import random
import matplotlib.pyplot as plt


def flip():
    return random.randint(0, 1)


def main():
    # initialize variables
    heads = 0
    tails = 0
    flips = 0
    flips_list = []
    heads_list = []
    tails_list = []

    # ask user for number of flips
    num_flips = int(input("How many times would you like to flip the coin? "))

    # flip coin num_flips times
    while flips < num_flips:
        if flip() == 0:
            heads += 1
        else:
            tails += 1
        flips += 1
        flips_list.append(flips)
        heads_list.append(heads)
        tails_list.append(tails)

    # plot results
    plt.plot(flips_list, heads_list, label="Heads")
    plt.plot(flips_list, tails_list, label="Tails")
    plt.xlabel("Number of Flips")
    plt.ylabel("Number of Heads/Tails")
    plt.title("Coin Flip Results")
    plt.legend()
    plt.show()


main()

# ask the user if they would like to flip again
while True:
    again = input("Would you like to flip again? (y/n) ")
    if again == "y":
        main()
    elif again == "n":
        print("Goodbye!")
        break
