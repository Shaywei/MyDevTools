'''
Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy, it deosn't mttaer in waht oredr the ltteers in a wrod are, the olny iprmoatnt tihng is taht the frist and lsat ltteers be at the rghit pclae. The rset can be a toatl mses and you can sitll raed it wouthit porbelm. Tihs is bcuseae the huamn mnid deos not raed ervey lteter by istlef, but the wrod as a wlohe

input: String arr[words in a dictionary] 

output: all sets of words that are 'equivalent'

sample input: ['word', 'string', 'field', 'flied', 'fried', 'array', 'fired']
'''

'''
Idea:

Let's use a hashtable:
    Keys = a touple containing the first and last characters of that word
    Values = a touple: a set of inner characters and a list of words.

'''

from collections import Counter
def print_equivalent(words):
    ht = dict()

    for word in words:
        word = word.strip('\'s')

        key = (word[0], word[-1])

        inner_letters = Counter(word[1:-1])

        if key not in ht.keys():
            ht[key] = [(inner_letters, set([word]))]

        else:
            matched = False
            for entry in ht[key]:
                if entry[0] == inner_letters:
                    entry[1].add(word)
                    matched = True

            if not matched:
                new_entry = (inner_letters, set([word]))
                ht[key].append(new_entry)

    for key in ht.keys():
        for entry in ht[key]:
            if len(entry[1]) > 1:
                print (' '.join(entry[1]))

if __name__ == '__main__':
    import file_utils, os
    #print_equivalent([word for word in file_utils.read_file(os.path.join(os.environ['PYTHONPATH'], 'dic.txt')).splitlines() if len(word) > 2])
    print_equivalent(['word', 'fired', 'fried', 'flied', 'field', 'felid'])

