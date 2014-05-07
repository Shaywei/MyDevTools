class Trie(object):
    __slots__ = ['c', 'EOW', 'nexts']

    @staticmethod
    def make_trie(words):
        t = Trie('')
        for word in words:
            t.insert_word(word)

    def __init__(self, _c, _EOW=False, _nexts=dict()):
        self.nexts = _nexts
        self.c =  _c
        self.EOW = _EOW

    def insert_word(self, word):
        print 'c:', self.c, 'EOW:', self.EOW, 'word:', word

        if len(word) == 0:
            self.EOW = True
        else:
            c = word[0]
            if self.nexts.get(c) is not None:
                EOW = True if len(word) == 1 else False
                self.nexts[c] = Trie(c, EOW)
            self.nexts[c].insert_word[word[1:]]

    def __getitem__(self, key):
        pass

    def __setitem__(self, key):
        pass

    def search(self, item):
        pass

    def items(self):
        pass

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        pass

    def __repr__(self):
        return "Trie(c=%r, EOW=%r, nexts=%r)" % (self.c, self.EOW, self.nexts)
