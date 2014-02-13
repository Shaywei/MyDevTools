# SRM 608

# Div2 I
class OneDimensionalRobotEasy(object):
    def finalPosition(self, commands, A, B):
        pos = 0
        for command in commands:
            if command == 'R' and pos < B:
                pos += 1
            elif command == 'L' and pos > -A:
                pos -= 1
        return pos

# Div2 II
class MysticAndCandiesEasy(object):
    def minBoxes(self, C, X, high):
        sorted_descending = sorted(high)
        ans = n = len(high)
        s = C
        for i in xrange(n):
            if s - sorted_descending[i] >= X:
                s -= sorted_descending[i]
                ans -= 1
        return ans