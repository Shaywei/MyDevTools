import marisa_trie

ENGLISH_WORDS = load_dic('brit-a-z.txt')

def load_dic(dic_file):
    l = []
    with open(dic_file) as f:
        for word in f:
            try:
                l.append(unicode(word.strip()))
            except:
                pass
    trie = marisa_trie.Trie(l)
    return trie

def is_word(word):
    return unicode(word) in ENGLISH_WORDS

def all_words_with_prefix(prefix):
    return [word.encode('ascii', 'ignore') for word in ENGLISH_WORDS.keys(unicode(prefix))]

def find_all_word_prefix(msg, words=ENGLISH_WORDS):
    ans = []
    for i in  xrange(len(msg)):
        prefix_i = unicode(msg[:i+1])
        if prefix_i in words:
            ans.append(msg[:i+1])
        elif words.keys(prefix_i) == []:
            return ans
    return ans

def break_sentence(sentence):
    global breakdowns
    breakdowns = []
    _break_sentence(sentence.lower())
    return [' '.join(bd[:-1]) for bd in breakdowns]

def _break_sentence(sentence, breakdown_so_far = []):
    global breakdowns
    if sentence == '':
        breakdown_so_far.append('GOOD!')
        return breakdown_so_far
    prefixes = find_all_word_prefix(sentence)

    if prefixes == []:
        breakdown_so_far.append('BAD!')
        return breakdown_so_far

    for prefix in prefixes:
        breakdowns.append(_break_sentence(sentence[len(prefix):], breakdown_so_far + [prefix]))

    breakdowns = [bd for bd in breakdowns if bd is not None]
    breakdowns = [bd for bd in breakdowns if bd[-1] != 'BAD!']
    return breakdowns