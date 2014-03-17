import string

def is_palindrome(s, ignore_case=True, ignore_spaces=True):
    if ignore_case:
        s = s.lower()

    if ignore_spaces:
        s = s.replace(' ', '')

    return s == s[::-1]

def all_substrings(S):
    substrings = set()
    for i in xrange(len(S)):
        for j in xrange(i+1, len(S)+1):
            substrings.add(S[i:j])
    l = list(substrings)
    #print l
    return substrings

def count_occurrences_with_overlap(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

def prefix_replace_pattern_postfix(s, prefix=None, pattern=None, replacement=None, postfix=None):
        if isinstance(pattern, str) and isinstance(replacement, str):
            s = re.sub(pattern, replacement, s)
        s = s if prefix is None else (prefix + s)
        s = s if postfix is None else (s + postfix)
        return s

def parse_properties_from_multiline_string(s):
    propeties = dict()
    for line in s.splitlines():
        key, val = line.strip().split('=', 2)
        propeties[key] = val
    return propeties

def find_subsequance(subseq, s):
    import re
    return True if re.search('.*'.join(subseq), s) else False

def find_subsequance_efficient(subseq, s):
    i = j = 0
    while i < len(subseq):
        if j == len(s):
            return False
        if subseq[i] == s[j]:
            i += 1
            print ('found ', s[j], 'at: ', j)
        j += 1
    return True

def camelcase(s, exceptions=[]):
    return ' '.join([word[0].upper()+word[1:] if (i == 0 or word not in exceptions) else word for i, word in enumerate(s.split(' '))])

def turn_to_valid_filename(s, accept_as_valid=''):
    valid_chars = "-_. %s%s" % (string.ascii_letters, string.digits) + accept_as_valid
    return ''.join(c for c in s if c in valid_chars)