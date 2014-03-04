# Div2 I

'''
Problem Statement
    
Note that the memory limit for all tasks in this SRM is 256 MB.
 The company Manao Inc. cares for its employees and tries to provide them with as much comfort as possible. One of the services Manao Inc. provides is transportation of employees from N distant locations to the office. The locations are numbered from 0 to N-1. You are given a tuple (integer) cnt containing N elements. The i-th (0-based index) element of cnt is the number of employees who live near location i.  The company wants to purchase several shuttles of the same size. These shuttles will then be used for employee transportation. Each of the shuttles will only serve one particular location. Each location will be assigned the smallest number of shuttles sufficient to transport all of the employees living close to it.  The cost of a shuttle consists of the cost baseCost of its frame and some additional cost seatCost per each seat. That is, a shuttle with X seats will cost baseCost + X * seatCost. For its shuttles, Manao Inc. can choose X to be any positive integer. (But remember that all the shuttles must have the same X.) Compute and return the least amount of money the company needs to spend on the shuttles in order to provide transportation for all employees.
Definition
    
Class:
TheShuttles
Method:
getLeastCost
Parameters:
tuple (integer), integer, integer
Returns:
integer
Method signature:
def getLeastCost(self, cnt, baseCost, seatCost):

Limits
    
Time limit (s):
2.000
Memory limit (MB):
256
Constraints
-
cnt will contain between 1 and 50 elements, inclusive.
-
Each element of cnt will be between 1 and 100, inclusive.
-
baseCost will be between 1 and 100, inclusive.
-
seatCost will be between 1 and 100, inclusive.
Examples
0)

    
{9}
30
5
Returns: 75
Manao Inc. provides transportation for its employees from a single location. There are 9 employees living near it. A shuttle with X seats will cost the company 30 + 5X. It is optimal to buy a single shuttle with 9 seats.
1)

    
{9, 4}
30
5
Returns: 150
Manao Inc. provides transportation from two locations. There are 9 employees living near location 0 and 4 employees living near location 1. It is optimal to buy two shuttles with 9 seats each and send a single shuttle to each location. (Note that the shuttles we buy must all be of the same size. It is not allowed to buy one shuttle with 9 and another with 4 seats.)
2)

    
{9, 4}
10
5
Returns: 105
This is the same test as the previous example, but baseCost is lower. It is optimal to buy three shuttles with 5 seats each and send two shuttles to location 0 and one shuttle to location 1.
3)

    
{51, 1, 77, 14, 17, 10, 80}
32
40
Returns: 12096
'''

import sys
class TheShuttles(object):
    def getLeastCost(self, cnt, baseCost, seatCost):
        # Lets calculate how much would it cost to support transportation with shuttles of size 1... max(cnt), and return the lowest sum.
        best_cost = sys.maxsize
        for num_seats in range(1, max(cnt)+1):
            cost_of_shuttle = baseCost + num_seats * seatCost
            cost_using_shuttle = 0
            for num_people in cnt:
                num_of_shuttles_needed = num_people / num_seats if num_people % num_seats == 0 else num_people / num_seats + 1
                cost_using_shuttle += num_of_shuttles_needed * cost_of_shuttle
            best_cost = min(best_cost, cost_using_shuttle)
        return best_cost
