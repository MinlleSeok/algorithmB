# maxprofit.py
import time
import random

def max_profit(prices):
    n = len(prices)
    max_profit = 0

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit

def max_profit2(prices):
    n = len(prices)
    max_profit = 0
    min_price = prices[0]
    for i in range(1,n):
        profit = prices[i] - min_price
        print("ㄹㄹ",profit)
        if profit > max_profit:
            max_profit = profit
        if prices[i] < min_price:
            min_price = prices[i]
    return max_profit

def test(n):
    a = []
    for i in range(0, n):
        a.append(random.randint(5000, 20000))
    start = time.time()
    mps = max_profit(a)
    end = time.time()
    time_slow = end - start

    start = time.time()
    mpf = max_profit2(a)
    end = time.time()
    time_fast = end - start

    print(n, mps, mpf)

    m = 0

    if time_fast > 0:
        m = time_slow / time_fast

    print("%d %.5f %.5f %.2f" % (n, time_slow, time_fast, m))

    
stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit(stock))
print(max_profit2(stock))
test(100)
test(10000)
