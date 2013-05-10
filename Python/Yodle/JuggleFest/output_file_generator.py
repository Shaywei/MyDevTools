__author__ = 'Shay Weiss'

def generate_output(matches, jugglers):
    jugglers_dict = {juggler.name:juggler for juggler in jugglers}
    output = ""
    for circuit, matching_jugglers in matches.items():
        output_line_as_list = []
        output_line_as_list.append(circuit) # circuit's name
        for juggler_name in matching_jugglers:
            output_line_as_list.append(jugglers_dict[juggler_name].representation_for_output)
        output += ' '.join(output_line_as_list).replace(' ,', ',')[:-1] + '\n'
    return output

def calc_representation_for_output_for_each_juggler(circuits, jugglers):
    for juggler in jugglers:
        juggler.calculate_representation_for_output({circuit.name : circuit for circuit in circuits})

def generate_output_file(path_to_file, matches, circuits, jugglers):
    calc_representation_for_output_for_each_juggler(circuits, jugglers)

    output = generate_output(matches, jugglers)

    with open(path_to_file, 'w') as output_file:
        output_file.write(output)

def calc_sum_of_jugglers_names_for_circuit_output_line(line):
    sum = 0
    line_as_list = line.strip().split()
    for elem in line_as_list:
        if elem[0] == 'J':
            sum += int(elem[1:])
    return sum
