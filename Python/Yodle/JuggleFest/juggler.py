__author__ = 'Shay Weiss'
class Juggler:
    def __init__(self, name, hep_ranks, circuit_preferences):
        # DRY - consider inheriting from Circuit or have a base class "juggling" interface
        self.name = name
        self.hep_ranks = hep_ranks
        self.circuit_preferences = circuit_preferences
        self.circuit_match_dict = {}

    def calculate_match_to_circuits(self, circuits):
        ''' assumes circuits are the same set as those in circuit_preferences
            circuits input var is a dict of the from circuit_name : circuit '''
        for circuit in self.circuit_preferences:
            self.circuit_match_dict[circuit] = circuits[circuit].calc_match_with_juggler(self)