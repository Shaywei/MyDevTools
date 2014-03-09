import marisa_trie

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

ENGLISH_WORDS = load_dic('brit-a-z.txt')

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
    return breakdowns

def _break_sentence(sentence, breakdown_so_far = []):
    global breakdowns
    if sentence == '':
        breakdowns.append(' '.join(breakdown_so_far))
        return

    for prefix in find_all_word_prefix(sentence):
        _break_sentence(sentence[len(prefix):], breakdown_so_far + [prefix])

if __name__ == '__main__':
    break_sentence('basedfearssdfsdf')