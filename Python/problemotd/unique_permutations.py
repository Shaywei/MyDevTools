'''
Unique Permutations

Today's problem comes from @mofodox.

Given the string "Hello world hello" how many unique (case sensitive) permutations can you find?

If you have a problem you'd like to see featured on here head over to http://www.problemotd.com/suggest/ and suggest it now!
'''
import itertools
def unique_perms(s="Hello world hello"):
    unique_pms = set(list(itertools.permutations(s.split())))
    for perm in unique_pms:
        print perm
    return len

unique_perms()