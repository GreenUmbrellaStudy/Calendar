# <GreenUmbrellaStudy>, code=utf-8

# The objective is to write a program that calculates which day of the week it will be in N days.
# First, we need know which day it is today and what is N.

DayT = input('Input what day it is today, considering {Sunday = 0, ... Saturday = 6}\n')
N = input('What day do you want to know (input N)\n')
DayNext = (int(DayT) + int(N)) % 7
print('In N days, it will be', DayNext)

# Resume: for all integers n, d with d > 0, we can find integers q and r,
# called a quotient q and a remainder, such that n = dq + r and 0 <= r < d.
# And moreover, n div d = n // d = q, and n mod d = n % d = r.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
