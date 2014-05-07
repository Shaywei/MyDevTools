import math_utils
'''
Cracking The Primes

It's Monday! Hope you all had a good weekend and are set to solve this week's problems.

One of the biggest areas in encryption is prime number generation. Eventually our computing power will grow to the point where RSA encryption will either need to be 1 million bits or a new key sharing standard will need to take over. In today's world a standard RSA key is 2048 bits. The key length is determined by the multiplication of 2 prime numbers, thus making it very hard to factor.

For today's challenge I have multiplied two small prime numbers together. Your objective is to find the two factors used. The 48 bit key can be bruteforced in a reasonable amount of time whereas the 146 bit key may take some more time and smarter engineering. As always feel free to post any code used in cracking the numbers.

Key (48 bit): 153728883468487

Key (146 bit): 50134918426382971596395239206900954838888151
'''

print math_utils.factor_to_primes(153728883468487) # output: Counter({10850761: 1, 14167567: 1})
# print math_utils.factor_to_primes(50134918426382971596395239206900954838888151) Not good enough for such a huge prime