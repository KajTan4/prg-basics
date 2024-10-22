###
# Calculates the sum of the digits in a number
#
import math
def sum_digits(number):
    if number < 0:
        number = abs(number)
    num_str = str(number)
    total = 0
    for chr in num_str:
        total += int(chr)


    return total

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')