__author__ = 'Shay Weiss'

import circuit, juggler

def parse_name_and_ranks(list):
    try:
        name = list[1]
        hep_ranks = []
        for i in (2,3,4):
            hep_ranks.append(int((list[i][2:])))
        return name, hep_ranks
    except Exception as e:
        print "exception: " + str(e) + "while trying to parse name and ranks from list: " + str(list)

def parse_circuit(line_as_list):
    name, hep_ranks = parse_name_and_ranks(line_as_list)
    return circuit.Circuit(name, hep_ranks)

def parse_juggler(line_as_list):
    name, hep_ranks = parse_name_and_ranks(line_as_list)
    circuit_preferences = line_as_list[-1].split(',')
    return juggler.Juggler(name, hep_ranks, circuit_preferences)

def parse_input_file(path_to_file):
    circuits = []
    jugglers = []

    with open(path_to_file, 'r') as input_file:
        for i, line in enumerate(input_file):
            try:
                line_as_list = line.strip().split()
                if len(line_as_list) == 0: continue
                elif line_as_list[0] == 'C': circuits.append(parse_circuit(line_as_list))
                elif line_as_list[0] == 'J': jugglers.append(parse_juggler(line_as_list))
                else: raise Exception("Unrecognized line type, not a Circuit/Juggler")
            except Exception as e:
                print "exception: '" + str(e) + "' in line ", i, ":\n " + line

    # Some input validation
    assert len(jugglers) % len(circuits) == 0
    for juggler in jugglers:
        assert len(set(juggler.circuit_preferences)) == len(circuits)

    return circuits, jugglers

