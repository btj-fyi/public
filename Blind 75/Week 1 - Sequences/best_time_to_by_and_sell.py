"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

prices: list = [7, 6, 4, 3, 1]
# the index of this list represents the price of the stock on the ith day

# chose one i to buy, then choose a different i of a greater value
# which in just i_buy < i_sell


def buy_and_sell(prices: list) -> int:
    past_prices: list = []
    profit: int = 0
    for day, price in enumerate(prices):
        past_prices.append(price)
        if day > 0:
            min_past_price = min(past_prices)
            if min_past_price < price:
                new_profit = price - min_past_price
                if new_profit > profit:
                    profit = new_profit
    return profit


# lowest price in all the days before

# we want to find the two numbers with the greatest delta where i_buy < i_sell

print(buy_and_sell(prices))


# REVIEW
# this problem took me 19 minutes w/o any additional resources
# this was more difficult and I am unsure about the solution - feels messy but it does work
# and it is not hammering the problem with multiple loops

# SOLUTION
# I think I got vaguely close to the right answer but ignoring the first value was an oversight


def Solution(prices):
    profit = 0  # i had this right
    buy = prices[0]  # set this to our first possible price to get things started
    for sell in prices:
        if sell > buy:
            profit = max(profit, sell - buy)
        else:
            buy = sell
    return profit


# its getting late I think I was just overthinking it
