#!/usr/bin/env python
import click

# build a function that returns the minimum number of coins as the value only using quarters and dimes


def greedy_coin(change):
    """Return a dictionary with the coin type as the key and the number of coins as the value"""

    print(f"Your change for {change}: ")
    coins = [0.25, 0.10]  # Only quarters and dimes
    coin_lookup = {0.25: "quarter", 0.10: "dime"}
    coin_dict = {}
    for coin in coins:
        coin_dict[coin] = 0
    for coin in coins:
        while change >= coin:
            change -= coin
            coin_dict[coin] += 1
    for coin in coin_dict:
        if coin_dict[coin] > 0:
            print(f"{coin_dict[coin]} {coin_lookup[coin]}")
    return coin_dict


# build a greedy algorithm to find the minimum number of coins but only use pennies, nickels, and dimes
def greedy_coin2(change):
    """Return a dictionary with the coin type as the key and the number of coins as the value"""

    print(f"Your change for {change}: ")
    coins = [0.10, 0.05, 0.01]  # Only dimes, nickels, and pennies
    coin_lookup = {0.10: "dime", 0.05: "nickel", 0.01: "penny"}
    coin_dict = {}
    for coin in coins:
        coin_dict[coin] = 0
    for coin in coins:
        while change >= coin:
            change -= coin
            coin_dict[coin] += 1
    for coin in coin_dict:
        if coin_dict[coin] > 0:
            print(f"{coin_dict[coin]} {coin_lookup[coin]}")
    return coin_dict


# build a click group
@click.group()
def main():
    """Return the minimum number of coins for a given change

    Example: ./greedy_coin.py
    """
    pass


# build a click command that returns only quarters and dimes
@main.command("qd")
@click.argument("change", type=float)
def qd(change):
    """Return the minimum number of quarters and dimes for a given change"""
    greedy_coin(change)


# build a click command that returns only pennies, nickels, and dimes
@main.command("pnd")
@click.argument("change", type=float)
def pnd(change):
    """Return the minimum number of pennies, nickels, and dimes for a given change"""
    greedy_coin2(change)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
