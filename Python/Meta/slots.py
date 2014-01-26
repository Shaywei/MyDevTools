'''
Illustrates the effectiveness of __slots__ on new_style objects in terms of memroy usage
As you can see, all 4 runs are pretty much time identical, but memory of the new style with __slots__ usage 
is about 1/4 of the rest!!

Line #    Mem usage    Increment   Line Contents
================================================
    22     11.4 MiB      0.0 MiB   @profile
    23                             def Factory(class_name, num_of_isntances_to_c
reate):
    24     11.4 MiB      0.0 MiB        collection = []
    25     99.0 MiB     87.5 MiB        for i in range (num_of_isntances_to_crea
te):
    26     99.0 MiB      0.0 MiB                exec('collection.append(%s(i))'
% (class_name))


73.8345536755

Filename: slots.py

Line #    Mem usage    Increment   Line Contents
================================================
    22     36.4 MiB      0.0 MiB   @profile
    23                             def Factory(class_name, num_of_isntances_to_c
reate):
    24     36.4 MiB      0.0 MiB        collection = []
    25    383.8 MiB    347.5 MiB        for i in range (num_of_isntances_to_crea
te):
    26    383.8 MiB      0.0 MiB                exec('collection.append(%s(i))'
% (class_name))


74.0802571638

Filename: slots.py

Line #    Mem usage    Increment   Line Contents
================================================
    22     45.4 MiB      0.0 MiB   @profile
    23                             def Factory(class_name, num_of_isntances_to_c
reate):
    24     45.4 MiB      0.0 MiB        collection = []
    25    390.2 MiB    344.8 MiB        for i in range (num_of_isntances_to_crea
te):
    26    390.2 MiB      0.0 MiB                exec('collection.append(%s(i))'
% (class_name))


74.5324830523

Filename: slots.py

Line #    Mem usage    Increment   Line Contents
================================================
    22     45.6 MiB      0.0 MiB   @profile
    23                             def Factory(class_name, num_of_isntances_to_c
reate):
    24     45.6 MiB      0.0 MiB        collection = []
    25    390.0 MiB    344.3 MiB        for i in range (num_of_isntances_to_crea
te):
    26    390.0 MiB      0.0 MiB                exec('collection.append(%s(i))'
% (class_name))

74.2571026362

'''

import timeit
from memory_profiler import profile

class FooSlotsNewStyle(object):
	__slots__ = ['x']
	def __init__(self, n):
		self.x = n

class FooNewStyle(object):
	def __init__(self, n):
		self.x = n

class FooSlotsOldStyle():
	__slots__ = ['x']
	def __init__(self, n):
		self.x = n

class FooOldStyle():
	def __init__(self, n):
		self.x = n

@profile
def Factory(class_name, num_of_isntances_to_create):
	collection = []
	for i in range (num_of_isntances_to_create):
		exec('collection.append(%s(i))' % (class_name))

def main():
	print(timeit.timeit('Factory(\'FooSlotsNewStyle\', 1000000)', setup="from __main__ import Factory", number=1))
	print(timeit.timeit('Factory(\'FooNewStyle\', 1000000)', setup="from __main__ import Factory", number=1))
	print(timeit.timeit('Factory(\'FooSlotsOldStyle\', 1000000)', setup="from __main__ import Factory", number=1))
	print(timeit.timeit('Factory(\'FooOldStyle\', 1000000)', setup="from __main__ import Factory", number=1))

if __name__ == '__main__':
	main()


