
import math
from math import exp
from math import sqrt
import numpy as np


def EuropeanPutOption(s, sigma, t, r, n, k):

    #s: the initial price of the underlying asset
    #sigma: the volatility of the underlying asset
    #t: the time to maturity
    #r: the risk-free rate
    #n: the number of periods
    #k: the strike price

    # Calculate delta t
    dt = t / n

    # Calculate the growth factor u
    u = exp(sigma * sqrt(dt))

    # Calculate the decay factor d
    d = 1 / u

    # Calculate the risk-neutral probability
    q = (exp(r * dt) - d) / (u - d)

    # Compute the stock tree
    stk_val = np.zeros((n + 1, n + 1))

    stk_val[0, 0] = s
    for i in range(1, n + 1):
        stk_val[i, 0] = stk_val[i - 1, 0] * u
        for j in range(1, i + 1):
            stk_val[i, j] = stk_val[i - 1, j - 1] * d

    # print(stk_val)

    # Compute the European derivative tree
    opt_val = np.zeros((n + 1, n + 1))

    for index in range(n + 1):
        opt_val[n, index] = max(0, (k - stk_val[n, index]))

    # Backward calculation within derivative tree
    for col in range(n - 1, -1, -1):
        for row in range(col + 1):
            opt_val[col, row] = (q * opt_val[col + 1, row] + (1 - q) * opt_val[col + 1, row + 1]) / exp(r * dt)

    # print(opt_val)

    return opt_val[0, 0]


def AmericanPutOption(s, sigma, t, r, n, k):
    # Calculate delta t
    dt = t / n

    # Calculate the growth factor u
    u = exp(sigma * sqrt(dt))

    # Calculate the decay factor d
    d = 1 / u

    # Calculate the risk-neutral probability
    q = (exp(r * dt) - d) / (u - d)

    # Compute the stock tree
    stk_val = np.zeros((n + 1, n + 1))

    stk_val[0, 0] = s
    for i in range(1, n + 1):
        stk_val[i, 0] = stk_val[i - 1, 0] * u
        for j in range(1, i + 1):
            stk_val[i, j] = stk_val[i - 1, j - 1] * d

    # print(stk_val)

    # Compute the European derivative tree
    opt_val = np.zeros((n + 1, n + 1))

    for index in range(n + 1):
        opt_val[n, index] = max(0, (k - stk_val[n, index]))

    # Backward calculation within derivative tree
    for col in range(n - 1, -1, -1):
        for row in range(col + 1):
            earlyExercise = k - stk_val[col, row]
            keepToTheEnd = (q * opt_val[col + 1, row] + (1 - q) * opt_val[col + 1, row + 1]) / exp(r * dt)
            opt_val[col, row] = max(earlyExercise, keepToTheEnd)
            # print opt_val[row, col]

    #print(opt_val)

    return opt_val[0, 0]


if __name__ == "__main__":
    '''

    print "European put option"
    for n in range (300, 310):
        print
        value = EuropeanPutOption(60.0, 0.15, 0.5, 0.05, n, 62.0)
        print "Option price using ", n, " periods: ", value

    for n in range (30, 40):
        print
        value = EuropeanPutOption(60.0, 0.15, 0.5, 0.05, n, 62.0)
        print "Option price using ", n, " periods: ", value

    print

    print "American put option"
    for n in range (300, 310):
        print
        value = AmericanPutOption(60.0, 0.15, 0.5, 0.05, n, 62.0)
        print "Option price using ", n, " periods: ", value

    for n in range (30, 40):
        print
        value = AmericanPutOption(60.0, 0.15, 0.5, 0.05, n, 62.0)
        print "Option price using ", n, " periods: ", value

    print

    '''

    # Changing volatility
    s = 60.0
    sigma = 0.25
    t = 0.5
    r = 0.05
    n = 300
    k = 62.0

    print "European put option with ", n, " periods:"
    print EuropeanPutOption(s, sigma, t, r, n, k)

    '''
    print "American put option with ", n, " periods:"
    print AmericanPutOption(s, sigma, t, r, n, k)
    '''
