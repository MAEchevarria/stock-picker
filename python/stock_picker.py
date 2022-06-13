def picker(prices):
    price_list = prices
    list_of_days = []
    profits = 0

    for x in range(len(price_list)):
        # needed to add range(start + 1, ) to remain ahead of date of buying
        for y in range(x + 1, len(price_list)):
            temp_profits = 0
            if (price_list[y] - price_list[x]) > temp_profits:
                # compare whether current buy/sell profits greater than previous or default values
                temp_profits = price_list[y] - price_list[x]
                if (temp_profits > profits):
                    # if temporary profit counter is greater than total profits, update profits and list of buy/sell date
                    profits = temp_profits
                    list_of_days = [x, y]

    # return list with buy/sell date, for most profit, by index
    return list_of_days

print(picker([17,3,6,9,15,8,6,1,10]) == [1,4])
print(picker([3,17,6,9,18,15,6,1,10]) == [0,4])
print(picker([1,17,6,9,8,15,6,3,19]) == [0,8])
print(picker([19,17,6,9,8,15,6,3,1]) == [2,5])