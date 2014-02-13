# SRM 607

# Div2 I
class BoundingBox(object):
    def smallestArea(self, Xs, Ys):
        return (max(Xs) - min(Xs)) * (max(Ys) - min(Ys))

# Div2 II
class PalindromicSubstringsDiv2(object):
    def count(self, S1, S2):
        ans = 0
        S = ''.join(S1) + ''.join(S2)
        substrings = self._all_substrings(S)
        for s in substrings:
            if self._is_palindrome(s):
                ans += self._count_occurrences_with_overlap(S, s)
        return ans

    def _is_palindrome(self,s):
        return s == s[::-1]

    def _all_substrings(self, S):
        substrings = set()
        for i in xrange(len(S)):
            for j in xrange(i+1, len(S)+1):
                substrings.add(S[i:j])
        l = list(substrings)
        #print l
        return substrings

    def _count_occurrences_with_overlap(self, string, sub):
        count = start = 0
        while True:
            start = string.find(sub, start) + 1
            if start > 0:
                count+=1
            else:
                return count
