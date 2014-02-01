''' Solutions to problem in Cracking the Coding Interview'''

'''
COMMON ERRORS:

    s = s.replace(...) !!!! (s.replace does not actually replaces s...)

'''
'''Arrays and Strings'''


'''
    1.1 - Implement an algorithm to determine if a string has all unique characters. What if you can not use additional data structures?

    questions for clarity:
    Do I know what is the set of strings allowed (a-zA-Z0-9 etc)?
    What is the meaning in no data structures allowed? Am I still allowed to use additional memory? for example, the string with all allowed characters?
    Simple solution - define set_string to be the string with all the allowed character, for example: "abc..zA...Z0..9". for each character in input string.
                      check if the set string contains the character. If yes - remove it and if not it is not unique
'''

from itertools import chain

def find_if_unique(s):
    set_string = ""
    
    for i in chain(range(ord('a'),ord('z')+1), range(ord('A'), ord('Z')+1), range(ord('0'), ord('9')+1)):
        set_string += (chr(i))   
        
    
    for c in s:
        if c not in set_string:
            return False
        
        set_string = set_string.replace(c, "", 1)

    return True

''' 
    1.2 - reverse c-style string
'''

def reverse_cstyle_string(s):
    s += '\0' # make it cstyle!
    slist = list(s)

    l_index = 0
    r_index = len(s) - 2
    
    while (l_index < r_index):
        tmp_c = s[l_index]
        slist[l_index] = slist[r_index]
        slist[r_index] = tmp_c
        l_index += 1
        r_index -= 1
    
    return ''.join(slist)

'''
    1.3 - Design an algorithm and write code to remove the duplicate characters in a string without using any additional buffer. NOTE: One or two additional variables are fine. An extra copy of the array is not.
    
    FOLLOW UP
    Write the test cases for this method
'''    

def remove_duplicate_characters(s):
    slist = list(s)
    charachters_seen_so_far = []
    for i in range(len(s)):
        if s[i] not in charachters_seen_so_far:
            charachters_seen_so_far.append(s[i])
        else:
            slist[i] = ''
    return ''.join(slist)
        
'''
    1.4 - Write a method to decide if two strings are anagrams or not.        
    clartiry question - can I assume that strings are anagrams only if they are literarly a permutation (that is, spaces and case matter)
'''
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    for c in s1:
        s2 = s2.replace(c, '', 1)
    
    return s2 == ''

if __name__ == '__main__':
    assert(True == find_if_unique('abcdef'))
    assert(False == find_if_unique('fabcdef'))
    assert(True == find_if_unique(''))

    assert('\0' == reverse_cstyle_string(''))
    assert('a' + '\0' == reverse_cstyle_string('a'))
    assert('ba' + '\0' == reverse_cstyle_string('ab'))
    assert('cba' + '\0' == reverse_cstyle_string('abc'))
    assert('dcba' + '\0' == reverse_cstyle_string('abcd'))

    assert('' == remove_duplicate_characters(''))
    assert('a' == remove_duplicate_characters('aaa'))
    assert('abc' == remove_duplicate_characters('abc'))
    assert('abc' == remove_duplicate_characters('abca'))

    assert(True == is_anagram('', ''))
    assert(True == is_anagram("arrigo boito", "tobia gorrio"))
    assert(True == is_anagram('abc', 'cab'))
    assert(False == is_anagram('abc', 'cad'))