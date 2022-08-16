def getMaxColors(prices, money):
    test_max = 0
    max = 0
    test_price = 0
    count = 0
    i = count
    flag = False
    while(i < len(prices)):
        flag = True
        if (prices[i] + test_price <= money):
            test_price = test_price + prices[i]
            test_max = test_max + 1
        elif (prices[i] + test_price > money):
            count = count + 1
            i = count
            test_max = 0
            test_price = 0
            flag = False
        if flag:
            i = i + 1
        if test_max > max:
            max = test_max
    return max


test_prices = [2,3,6,1,1,4,1]
test_money = 7
result = getMaxColors(test_prices, test_money)
print("result: " + str(result))