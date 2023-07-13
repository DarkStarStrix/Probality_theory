# use naive bayes to predict the probability of someone flipping a coin again based on the previous flips (heads or tails)

import random

import matplotlib.pyplot as plt

from main import flip

flip()  # 0 = heads, 1 = tails


# use oop programming to create a coin class that can be used to flip a coin use bayes theorem to predict the probability of a coin flip based on previous flips
# use naive bayes to predict the probability of someone flipping a coin again based on the previous flips (heads or tails)

def flip():
    return random.randint(0, 1)


def bayes_theorem(num_flips):
    # initialize variables
    heads = 0
    tails = 0
    flips = 0
    flips_list = []
    heads_list = []
    tails_list = []

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


class Coin:
    def __init__(self):
        self.heads = 0
        self.tails = 0
        self.flips = 0
        self.flips_list = []
        self.heads_list = []
        self.tails_list = []

    def flip_coin(self, num_flips):
        while self.flips < num_flips:
            if flip() == 0:
                self.heads += 1
            else:
                self.tails += 1
            self.flips += 1
            self.flips_list.append(self.flips)
            self.heads_list.append(self.heads)
            self.tails_list.append(self.tails)

    def plot_results(self):
        plt.plot(self.flips_list, self.heads_list, label="Heads")
        plt.plot(self.flips_list, self.tails_list, label="Tails")
        plt.xlabel("Number of Flips")
        plt.ylabel("Number of Heads/Tails")
        plt.title("Coin Flip Results")
        plt.legend()
        plt.show()


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

    # ask the user if they would like to flip again
    while True:
        again = input("Would you like to flip again? (y/n) ")
        if again == "y":
            main()
        elif again == "n":
            print("Goodbye!")
            break
