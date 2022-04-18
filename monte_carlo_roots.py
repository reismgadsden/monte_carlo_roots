"""
Attempts to find a root of polynomial using Monte Carlo approach.
This program breaks when the rate of change is negative,
it will find where x is undefined in these cases.

author: Reis Gadsden
version: 17/4/22
github: https://github.com/reismgadsden/monte_carlo_roots

class: CS-5531 @ Appalachian State University
instructor: Dr. Mohammad Mohebbi
"""

import random
import math
import sys

a = 0
b = 0
k = 0
p = 0


def main() -> None:
    global a, b, k, p
    print("Function: Ax^k + Bx^p + tan(Ax^k + Bx^p)")
    while True:
        a = input("Please enter a value for A: ")
        b = input("Please enter a value for B: ")
        k = input("Please enter a value for k: ")
        p = input("Please enter a value for p: ")
        n = input("Please enter the number of iterations you would like to attempt a guess: ")
        actual = input("Please enter the actual roots of your function "
                       "(if there are multiple, enter a list of as many roots as you would like): ").strip()

        try:
            a = float(a.strip())
            b = float(b.strip())
            k = float(k.strip())
            p = float(p.strip())
            n = int(n.strip())
            break
        except ValueError as v:
            print("One or more value was improperly formatted")
            continue
    print("Ok!")
    f = open("Results.txt", 'a')
    output = "a = " + str(a) + ", b = " + str(b) + ", k = " + str(k) + \
             ", p = " + str(p) + " number of iterations: " + str(n) + \
             ", actual value of x: " + str(actual) + "\n"
    best_guess, guess_trace = guess_root(n)
    output += guess_trace
    output += "Approximation of x: " + str(best_guess) + '\n'
    f.write(output + "\n")
    f.close()


def guess_root(n) -> float:
    x = 0

    # limit x1 and x2 to positive roots
    # some equations do not have values for negative numbers
    x1 = 0
    x2 = 1000
    t = 0
    output = ""

    while t < n:
        print("Iteration #", t)
        x = random.uniform(x1, x2)

        if x * 2 == float('inf') or math.cos(a * (x ** k) + b * (x ** p)) == 0:
            continue

        output += "iteration #" + str(t) + ": x1 = " + str(x1) + ", x2 = " + str(x2) +\
                  ", x = " + str(x) + "\n"
        result = polynomial(x)

        if result < 0:
            x1 = x
        elif result > 0:
            x2 = x
        else:
            break
        t += 1
    return x, output


def polynomial(x) -> float:
    return a * (x ** k) + b * (x ** p) + math.tan(a * (x ** k) + b * (x ** p))


if __name__ == "__main__":
    main()
