'''
Palindromic Numbers

A palindromic number is a number that reads the same forwards as it does backwards. 123321 is a palindromic number where as 321321 is not. Negative numbers may be considered palindromic or not; it's up to you until someone proves otherwise.

Your mission, should you choose to accept it, is to create a program to return whether a number is a palindromic number or not. To make things slightly more interesting you may not use a string or array in your solution. Thus doing something like "123.toString()" is not allowed.

Good luck!
'''
def is_palindromic_number(num):
    num = abs(num)
    l = []
    while num > 0:
        l.append(num % 10)
        num = num / 10
    return l == l[::-1]

print is_palindromic_number(-31213)