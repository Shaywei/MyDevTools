from collections import deque
import os

def tail(f, n=10):
    d = deque(maxlen=n)

    if not os.path.exists(f):
        raise ValueError('File not found')
    with open (f, 'r') as _file:
        for line in _file:
            d.append(line)
    return ''.join(d)

def tail2(f, n=10):
    number_of_newlines_found = 0

    if not os.path.exists(f):
        raise ValueError('File not found')

    with open (f, 'r') as _file:
        _file.seek(-1, 2) # Go to the last byte
        while _file.tell() != 0:
            if _file.read(1) == '\n':
                number_of_newlines_found += 1
                if number_of_newlines_found == n-1:
                    return _file.read()
            _file.seek(-2, 1)
        return _file.read()

if __name__ == '__main__':
    #print (tail('./tail.py'))
    #print ('******')
    #print(tail('./tail.py', n=3))
    print tail2('./tail.py', n=10)