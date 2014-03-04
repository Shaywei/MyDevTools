# Div2 I
'''
Problem Statement
    
Dachshund is a popular dog breed. In this problem, a miniature dachshund is defined as a dachshund whose weight is not more than 5,000 grams.  Lun the miniature dachshund loves mikan (satsuma oranges). She has just bought some mikan. You are given a tuple (integer) mikan. It gives the weight of all mikan she bought. For each valid i, mikan[i] is the weight of the i-th mikan in grams.  You are also given an integer weight. Currently, Lun weighs weight grams. When she eats i-th mikan, her weight increases by mikan[i] grams. If she eats multiple mikan, her weight increases by their total weight. She cannot eat just a part of a mikan. In other words, if she chooses to eat a mikan, she eats it completely.  She wants to remain being a miniature dachshund. That is, she wants her weight not to exceed 5,000 grams. Under this condition, calculate and return the maximum number of mikan Lun can eat.
Definition
    
Class:
MiniatureDachshund
Method:
maxMikan
Parameters:
tuple (integer), integer
Returns:
integer
Method signature:
def maxMikan(self, mikan, weight):

Limits
    
Time limit (s):
2.000
Memory limit (MB):
64
Constraints
-
mikan will contain between 1 and 50 elements, inclusive.
-
Each element of mikan will be between 50 and 200, inclusive.
-
weight will be between 3,000 and 5,000, inclusive.
Examples
0)

    
{100, 100, 100, 100, 100}
4750
Returns: 2
Here, Lun weighs 4,750 grams and has bought 5 mikan, each of which weighs 100 grams. When she eats 2 of these, her weight will be 4,950 grams. She should not eat more.
1)

    
{100, 100, 100, 100, 50}
4750
Returns: 3
This time, one of the mikan is smaller. She can eat it with 2 of the 100-gram mikan. Note that her weight is allowed to be exactly 5,000 grams.
2)

    
{120, 90, 130, 100, 110, 80}
3000
Returns: 6
When she is light enough, she can eat all of the mikan she has bought.
3)

    
{50}
5000
Returns: 0
When her weight is already 5,000 grams, she should not eat anything.
4)

    
{200, 50, 200, 50, 200, 50, 200, 50}
4800
Returns: 4
'''
class MiniatureDachshund:
    def maxMikan(self, mikan, weight):
        mikan = sorted(mikan)
        ans = 0
        for i in range(len(mikan)):
            weight += mikan[i]
            if weight > 5000:
                return ans
            ans += 1
        return ans




# Div2 II

'''

Problem Statement
    
This problem statement contains superscipts that may not display properly outside the applet.
 You are given four integers A, B, C and D. Return "divisible" (quotes for clarity) if AB is divisible by CD. Return "not divisible" otherwise.
Definition
    
Class:
BigFatInteger2
Method:
isDivisible
Parameters:
integer, integer, integer, integer
Returns:
string
Method signature:
def isDivisible(self, A, B, C, D):

Limits
    
Time limit (s):
2.000
Memory limit (MB):
64
Notes
-
The return value is case-sensitive.
-
Positive integer y divides a positive integer x if and only if there is a positive integer z such that y*z=x. In particular, for each positive integer x, both 1 and x divide x.
Constraints
-
A, B, C and D will each be between 1 and 1,000,000,000 (109), inclusive.
Examples
0)

    
6
1
2
1
Returns: "divisible"
Here, AB = 61 = 6 and CD = 21 = 2. 6 is divisible by 2.
1)

    
2
1
6
1
Returns: "not divisible"
2 is not divisible by 6.
2)

    
1000000000
1000000000
1000000000
200000000
Returns: "divisible"
Now the numbers are huge, but we can see that AB is divisible by CD from the fact that A=C and B>D.
3)

    
8
100
4
200
Returns: "not divisible"
We can rewrite 8100 as (23)100 = 2300. Similarly, 4200 = (22)200 = 2400. Thus, 8100 is not divisible by 4200.
4)

    
999999937
1000000000
999999929
1
Returns: "not divisible"
Here A and C are distinct prime numbers, which means AB cannot have C as its divisor.
5)

    
2
2
4
1
Returns: "divisible"

'''

from collections import Counter

def factor_to_primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n /= d
        d += 1
    if n > 1:
       primfac.append(n)
    return Counter(primfac)

class BigFatInteger2:
    def isDivisible(self, A, B, C, D):
        A_factorization = factor_to_primes(A)
        C_factorization = factor_to_primes(C)

        for key in A_factorization:
            A_factorization[key] *= B

        for key in C_factorization:
            C_factorization[key] *= D

        for key in C_factorization.keys():
            if key not in A_factorization.keys() or C_factorization[key] > A_factorization[key]:
                return 'not divisible'
        return 'divisible'
