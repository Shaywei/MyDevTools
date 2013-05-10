__author__ = 'Shay Weiss'
class Juggler:
    def __init__(self, name, hep_ranks, circuit_preferences):
        # DRY - consider inheriting from Circuit or have a base class "juggling" interface
        self.name = name
        self.hep_ranks = hep_ranks
        self.circuit_preferences = circuit_preferences
        self.representation_for_output = None

    def calculate_representation_for_output(self, circuits):
        ''' assumes circuits contain those in self.circuit_preferences
            circuits input var is a dict of the from circuit_name : circuit '''
        circuit_match_dict ={}
        for circuit in self.circuit_preferences:
            circuit_match_dict[circuit] = circuits[circuit].calc_match_with_juggler(self)
        self.representation_for_output = ' '.join([self.name] + [circuit_name + ':' + str(circuit_match_dict[circuit_name]) for circuit_name in self.circuit_preferences]) + ','