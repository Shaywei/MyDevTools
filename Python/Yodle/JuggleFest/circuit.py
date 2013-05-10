__author__ = 'Shay Weiss'
import operator

class Circuit:
    def __init__(self, name, hep_ranks):
        self.name = name
        self.hep_ranks = hep_ranks

    def calc_match_with_juggler(self, juggler):
        return sum(p*q for p,q in zip(self.hep_ranks, juggler.hep_ranks))

    def to_dict(self):
        return {self.name : self}

    def calc_preference_list(self, jugglers):
        # create a dictionary juggler_name:juggler_match
        jugglers_match_dic = {}

        for j in jugglers:
            jugglers_match_dic[j.name] = self.calc_match_with_juggler(j)

        # The following is a list of pairs where the first elem is name, second element is match sorted by match, ascending.
        sorted_jugglers_match_dic = sorted(jugglers_match_dic.iteritems(), key=operator.itemgetter(1))

        result = [elem[0] for elem in sorted_jugglers_match_dic]
        result.reverse()
        return result
