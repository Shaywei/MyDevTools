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

import linked_lists
ll_factory = linked_lists.LinkedList.from_list

''' 2.1 Write a code to remove duplicates from an unsorted linked list'''

def remove_duplicates_buffer(ll):
    buff = []
    for item in ll:
        if item not in buff:
            buff.append(item)

    return linked_lists.LinkedList.from_list(buff)

''' 2.2 Algorithm to find k to the last element of a linked list '''

'''
[1,2,3,4,5,6]
1 = last
2 = 1 before last
..
len(ll) = 1st

I assume k is between 1 and len(ll)

Naive option O(n):
    first go over the list to find it's length, denote as l.
    Then make another pass and return the link at place l-k
'''

def find_kth_to_the_last_2_passes(ll, k):  
    p = ll
    length = 1
    while p.next_l:
        length += 1
        p = p.next_l
    
    # now p is length(ll)
    
    while length - k != 0:
        ll = ll.next_l
        length -=1
    
    return ll.item


def find_kth_to_the_last_1_pass(ll, k):  
    p = ll
    p2 = ll
    
    for i in range(k-1):
        p2 = p2.next_l
    
    while p2.next_l is not None:
        p2 = p2.next_l
        p = p.next_l
        
    return p.item

''' Algorithem that takes as an input a node in a linked list and deletes it '''

'''
O(1) space and time ^_^
list = [1]->[2]->[3]->[4]->[5]
input_node = [3]

# Assumption - can't be the last node!
# [3]->[4]->[5] (found next node)
# [4]->[4]->[5] (copied next node's data)
# [4]->[5]      (unlinked next node)
'''

def delete_node(node):
    next_node = node.next_l 
    node.item = next_node.item # will crash if node is the next node!
    node.next_l = next_node.next_l 

''' Algorithem that checkes if a linked list is a palindrom'''
'''
[1] -> [2] -> [1]
[1] -> [2] -> [2] -> [1]

[1]

Option 1 - copy all items of ll to a buffer (array), then check (one pass over list, one pass over buffer, O(n) space, calculate length.

Option 2 - Pass over ll to check length, pass again and copy half of it into a buffer. Then travel to the second half of the list and check against reversed buffer. O(n/2) space

Option 3 - O(1) space - pass to check length, then pass for each of n/2 elements to check if palindrom.

'''

def check_length(ll):
    length = 1
    while ll.next_l:
        length += 1
        ll = ll.next_l
    return length
    
def copy_to_buff(ll, how_many):
    buff = []
    for i in range(how_many):
        buff.append(ll.item)
        ll = ll.next_l
    return buff
    
def is_palindrom(ll):
    length = check_length(ll)
    if length == 1:
        return True
    buff = copy_to_buff(ll, length/2)
    buff.reverse()

    i = length/2  if length%2 == 0 else length/2 + 1
    second_half_of_ll = ll
    while i != 0:
        second_half_of_ll = second_half_of_ll.next_l
        i -= 1

    for item in buff:
        if item != second_half_of_ll.item:
            return False
        second_half_of_ll = second_half_of_ll.next_l
    return True

def count_twos(num):
    count = 0
    for i in range(2, num + 1):
        for c in str(i):
            if c == '2':
                count += 1
    return count

def shay_num(n): # number of twos in 0 .. 9(n_times)
    if n==1:
        return 1
    return (9 * shay_num(n-1) + pow(10, n-1))
    
def count_twos_using_shay_num(num, res_acc=0):
    print 'num, res_acc = ', num, res_acc
    if num < 10:
        res = res_acc if num < 2 else res_acc + 1
        print res
        return res
    
    msd = int(str(num)[0])
    sn = shay_num(len(str(num)) - 1)

    
    print 'msd', msd
    print 'sn', sn
    #print pow(10, len(str(num))-1)*2
    if msd == 1:
        print 'msd == 1', int(str(num)[1:]), res_acc + sn
        return count_twos_using_shay_num(int(str(num)[1:]), res_acc + sn)
    elif msd == 2:
        res = count_twos_using_shay_num(num - pow(10, len(str(num))-1)*2, res_acc) + count_twos_using_shay_num(pow(10, len(str(num))-1)*2 - 1, res_acc + num - pow(10, len(str(num))-1)*2 + 1) 
        print res
        return res
    else:
        return count_twos_using_shay_num(num - pow(10, len(str(num-1))), res_acc + sn)

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

    assert(ll_factory([1,2,3,4,5]) == remove_duplicates_buffer(ll_factory([1,1,1,2,2,3,3,4,5])))
    #assert(ll_factory([1,2,3,4,5]) == remove_duplicates_no_buffer(ll_factory([1,1,1,2,2,3,3,4,5])))


    assert(5 == find_kth_to_the_last_2_passes(ll_factory([1,2,3,4,5]), 1))
    assert(4 == find_kth_to_the_last_2_passes(ll_factory([1,2,3,4,5]), 2))
    assert(3 == find_kth_to_the_last_2_passes(ll_factory([1,2,3,4,5]), 3))
    assert(2 == find_kth_to_the_last_2_passes(ll_factory([1,2,3,4,5]), 4))
    assert(1 == find_kth_to_the_last_2_passes(ll_factory([1,2,3,4,5]), 5))

    assert(5 == find_kth_to_the_last_1_pass(ll_factory([1,2,3,4,5]), 1))
    assert(4 == find_kth_to_the_last_1_pass(ll_factory([1,2,3,4,5]), 2))
    assert(3 == find_kth_to_the_last_1_pass(ll_factory([1,2,3,4,5]), 3))
    assert(2 == find_kth_to_the_last_1_pass(ll_factory([1,2,3,4,5]), 4))
    assert(1 == find_kth_to_the_last_1_pass(ll_factory([1,2,3,4,5]), 5))

    assert(True == is_palindrom(ll_factory([1])))
    assert(True == is_palindrom(ll_factory([1,2,1])))
    assert(True == is_palindrom(ll_factory([1,2,2,1])))
    assert(False == is_palindrom(ll_factory([1,2,3])))
    assert(False == is_palindrom(ll_factory([1,2,3,1])))

    for i in range(1,6):
        if i != 5:
           ll = ll_factory(range(1,6))
           expected = ll_factory([j for j in range(1,6) if j != i])
           node = ll
           while i != 1:
               node = node.next_l
               i -= 1
           actual = delete_node(node)
           assert(expected == ll)

    assert(755 == count_twos(2125))

    #assert(755 == count_twos_using_shay_num(2125))
