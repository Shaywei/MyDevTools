__author__ = 'Shay Weiss'

class Circuit:
    def __init__(self, name, hep_ranks):
        self.name = name
        self.hep_ranks = hep_ranks

    def calc_match_with_juggler(self, juggler):
        return sum(p*q for p,q in zip(self.hep_ranks, juggler.hep_ranks))

    def to_dict(self):
        return {self.name : self}