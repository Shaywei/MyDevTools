

__author__ = 'ShayWeiss'

def dictionary_list_file_parser(path_to_file, int_keys, float_keys):
    '''Takes a file where each line is of the form:
    
        key1:value1,key2:value2,....,keyN:valueN

        and returns a list of dictionaries parsed from each line.

        if a key maches an element in 'int_keys' it is cast into int
        if a key maches an element in 'float_keys' it is cast into float

        the value for every other key is considered string.
    '''
    def parse_line_to_dict(string):
        entry = {}
        try:
            key_items = line.split(',')
            for item in key_items:
                (key, value) = item.split(':', 1)
                if key in int_keys:
                    entry[key] = int(value)
                elif key in float_keys:
                    entry[key] = float(value)
                else:
                    entry[key] = value

            return entry
        except Exception as e:
            print "exception in line " + str(i) + "\n: " + line
            print e     

    result = []
    with open(path_to_file, 'r') as target_file:
        for i, line in enumerate(target_file):
            line = line.strip()
            result.append(parse_line_to_dict(line))
    return result
