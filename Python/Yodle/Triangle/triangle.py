__author__ = 'Shay Weiss'

def max_path(path_to_file):
    '''
        Note that problem is undefined in case where there are adjacent identical numbers:
        0
        1 1
        3 0 2

        possible output can be either 4 or 3 depending on which 1 was chosen in second row.
    '''

    sum = index = 0
    with open(path_to_file, 'r') as target_file:
        for i, line in enumerate(target_file):
            try:
                line_as_list = [int(num_str) for num_str in line.strip().split()] # Read just 1 line at a time vs. loading all of the file to a list of lists
            except Exception as e:
                print "exception in line ", i, ":\n " + line
                print e

            assert len(line_as_list) == i + 1 # Making sure the triangle is valid

            if i == 0:
                sum = line_as_list[i] # Starting condition
            else:
                candidate1, candidate2 = line_as_list[index:index+2]
                index, sum = (index, sum + candidate1) if candidate1 > candidate2 else (index + 1, sum + candidate2)
        return sum





