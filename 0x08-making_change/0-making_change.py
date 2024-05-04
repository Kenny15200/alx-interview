#!/usr/bin/python3
"""
Module for making change.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): A list of coin denominations.
        total (int): The total amount to make change for.

    Returns:
        int: The fewest number of coins needed to meet the total.
             Returns -1 if the total cannot be met by any combination of coins.
    """
    if total <= 0:
        return 0

    # Create a list to store the fewest number of coins needed for each total from 0 to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin denomination
    for coin in coins:
        # Update dp[j] if it can be reached with fewer coins using the current coin
        for j in range(coin, total + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be met by any combination of coins
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]


if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))

