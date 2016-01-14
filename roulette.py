#!/usr/bin/env python3.3

import random
import math
import time


money = 200  # Starting money
percent = 0.00000001  # Percentage of money to bet
delay = 0  # Delay between each pass

staticbet = True  # Bet a static amount each pass
static = 0.05

debug = False  # Print whenever a bet is placed


totalbets = 0
totalpasses = 0


def bet(amount):
    global money
    if amount > money:
        raise RuntimeError("Cant afford bet!")
    if random.random() > 0.5:
        money += amount
        if debug:
            print("Bet won. Earned $%s" % amount)
        return True
    else:
        money -= amount
        if debug:
            print("Bet lost. Lost $%s" % amount)
        return False


print("Starting run with $%d..." % money)
if staticbet:
    print("Bets are static. Betting $%d each pass." % static)
else:
    print("Bets are variable. Betting %s of money each pass." % percent)

if debug:
    if delay > 0:
        print("Debug logging is on. Setting a delay is recommended")
    else:
        print("Debug logging is on.")
else:
    print("Debug logging is off.")

while True:
    before = money
    bets = 1
    try:
        if staticbet:
            tobet = math.ceil(money * percent)
        else:
            tobet = staticbet
        while True:
            if debug:
                print("Betting $%s total money: $%d" % (tobet, money))
            win = bet(tobet)
            if win:
                break
            else:
                bets += 1
                tobet *= 2
        totalbets += bets
        totalpasses += 1
        if debug:
            print("Pass complete. Bets placed: %d Current money: $%d" % (bets, money))
        time.sleep(delay)
    except RuntimeError as e:
        totalbets += bets
        totalpasses += 1
        if debug:
            print(e)
        print("Managed to earn 4%d before exceeding bet limit" % before)
        print("Total bets: %d Total passes: %d" % (totalbets, totalpasses))

        if money <= 0:
            print("Ran out of money.")
            break
        else:
            print("Starting another try with $%d" % money)
            print()
