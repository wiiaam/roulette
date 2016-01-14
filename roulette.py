#!/usr/bin/env python3.3

import random
import math
import time


money = 1000000  # Starting money
percent = 0.00000001  # Percentage of money to bet
delay = 0  # Delay between each pass

staticbet = True
static = 1

totalbets = 0
totalpasses = 0

debug = False


def bet(amount):
    global money
    if amount > money:
        raise RuntimeError("Ran out of money")
    if random.random() > 0.5:
        money += amount
        if debug:
            print("Bet won. Earned %s" % amount)
        return True
    else:
        money -= amount
        if debug:
            print("Bet lost. Lost %s" % amount)
        return False


while True:
    before = money
    try:
        bets = 1
        if staticbet:
            tobet = math.ceil(money * percent)
        else:
            tobet = staticbet
        while True:
            if debug:
                print("Betting %s total money: %d" % (tobet, money))
            win = bet(tobet)
            if win:
                break
            else:
                bets += 1
                tobet *= 2
        totalbets += bets
        totalpasses += 1
        if debug:
            print("Pass complete. Total bets placed: %d Current money: %.02d" % (bets, money))
        time.sleep(delay)
    except RuntimeError as e:
        print(e)
        print()
        print("Managed to earn %d" % before)
        print("Total bets: %d Total passes: %d" % (totalbets, totalpasses))
        break
