# Path: stockprice.py

# Write a program that finds the best days to buy and sell stocks to maximize profit, given an array of stock prices. Return the maximum profit that can be made. If no profit can be made, return -1.

# Example:

#Input:[100,180,260,310,40,535,695]

#Output:Buy on day 5 at price 40 Sell on day 7 at price 695 Max profit: 655

def stockprice(arr):

    # Write your code here

    max_profit = 0

    for i in range(len(arr)):

        for j in range(i+1, len(arr)):

            if arr[j] - arr[i] > max_profit:

                max_profit = arr[j] - arr[i]

    if max_profit == 0:

        return -1

    return max_profit
