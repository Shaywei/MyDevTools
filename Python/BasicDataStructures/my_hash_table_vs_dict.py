'''

My ht is about 20% slower (12.117 vs. 10.757 seconds) and consumes about 20% more memory (154MiB vs 130)

Line #    Mem usage    Increment   Line Contents
================================================
    12     14.7 MiB      0.0 MiB   @profile
    13                             def Factory(class_to_test, num_of_entries_to_create):
    14     14.7 MiB      0.0 MiB       instance = class_to_test()
    15
    16    130.2 MiB    115.5 MiB       for i in range (num_of_entries_to_create):
    17    130.2 MiB      0.0 MiB           exec('instance[i]=id_generator()')


         2800220 function calls in 10.757 CPU seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    6.223    6.223   11.099   11.099 my_hash_table_vs_dict.py:12(Factory)
   700000    1.785    0.000    3.348    0.000 my_hash_table_vs_dict.py:10(<genexpr>)
   600000    1.478    0.000    1.562    0.000 random.py:259(choice)
   100000    0.811    0.000    4.159    0.000 {method 'join' of 'str' objects}
   100000    0.316    0.000    4.525    0.000 my_hash_table_vs_dict.py:9(id_generator)
   100002    0.052    0.000    0.052    0.000 {range}
   600000    0.047    0.000    0.047    0.000 {method 'random' of '_random.Random' objects}
   600012    0.037    0.000    0.037    0.000 {len}
        1    0.003    0.003   11.103   11.103 memory_profiler.py:421(f)
       10    0.002    0.000    0.002    0.000 {method 'write' of 'file' objects}
        1    0.000    0.000    0.000    0.000 memory_profiler.py:455(disable_by_count)
        2    0.000    0.000    0.000    0.000 {nt.stat}
        1    0.000    0.000    0.000    0.000 {open}
        1    0.000    0.000    0.003    0.003 memory_profiler.py:522(show_results)
       39    0.000    0.000    0.000    0.000 tokenize.py:264(generate_tokens)
       32    0.000    0.000    0.000    0.000 {built-in method match}
        1    0.000    0.000    0.000    0.000 tokenize.py:174(tokenize_loop)
        1    0.000    0.000    0.000    0.000 memory_profiler.py:517(disable)
        1    0.000    0.000   11.106   11.106 memory_profiler.py:771(wrapper)
        1    0.000    0.000    0.000    0.000 inspect.py:671(getblock)
        1    0.000    0.000    0.000    0.000 {method 'readlines' of 'file' objects}
       16    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
       38    0.000    0.000    0.000    0.000 inspect.py:639(tokeneater)
        1    0.000    0.000    0.000    0.000 linecache.py:68(updatecache)
        1    0.000    0.000    0.000    0.000 tokenize.py:155(tokenize)
        1    0.000    0.000    0.000    0.000 inspect.py:632(__init__)
       32    0.000    0.000    0.000    0.000 {built-in method span}
        1    0.000    0.000    0.000    0.000 genericpath.py:15(exists)
        1    0.000    0.000    0.000    0.000 memory_profiler.py:394(__call__)
        1    0.000    0.000    0.000    0.000 linecache.py:33(getlines)
        1    0.000    0.000    0.000    0.000 memory_profiler.py:510(enable)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        2    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        2    0.000    0.000    0.000    0.000 {sys.settrace}
        1    0.000    0.000    0.000    0.000 memory_profiler.py:388(__init__)
        1    0.000    0.000    0.000    0.000 {min}
        1    0.000    0.000    0.000    0.000 memory_profiler.py:403(add_function)
        1    0.000    0.000    0.000    0.000 memory_profiler.py:448(enable_by_count)
        2    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {iter}
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 memory_profiler.py:417(wrap_function)
        1    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {sys.gettrace}
        1    0.000    0.000    0.000    0.000 {getattr}
        1    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}


Filename: my_hash_table_vs_dict.py

Line #    Mem usage    Increment   Line Contents
================================================
    12     58.6 MiB      0.0 MiB   @profile
    13                             def Factory(class_to_test, num_of_entries_to_create):
    14     58.6 MiB      0.0 MiB       instance = class_to_test()
    15
    16    154.3 MiB     95.6 MiB       for i in range (num_of_entries_to_create):
    17    154.3 MiB      0.0 MiB           exec('instance[i]=id_generator()')


         3300215 function calls in 12.117 CPU seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    6.295    6.295   12.645   12.645 my_hash_table_vs_dict.py:12(Factory)
   700000    1.796    0.000    3.363    0.000 my_hash_table_vs_dict.py:10(<genexpr>)
   600000    1.479    0.000    1.568    0.000 random.py:259(choice)
   100000    0.820    0.000    4.184    0.000 {method 'join' of 'str' objects}
   100000    0.585    0.000    0.962    0.000 hash_tables.py:43(insert)
   100000    0.321    0.000    4.556    0.000 my_hash_table_vs_dict.py:9(id_generator)
   100000    0.300    0.000    1.262    0.000 hash_tables.py:68(__setitem__)
   100000    0.191    0.000    0.203    0.000 hash_tables.py:40(i)
    99936    0.175    0.000    0.175    0.000 hash_tables.py:8(insert)
   100002    0.053    0.000    0.053    0.000 {range}
   600000    0.049    0.000    0.049    0.000 {method 'random' of '_random.Random' objects}
   600012    0.039    0.000    0.039    0.000 {len}
   100000    0.011    0.000    0.011    0.000 {hash}
       10    0.002    0.000    0.002    0.000 {method 'write' of 'file' objects}
        1    0.000    0.000    0.000    0.000 {nt.stat}
       64    0.000    0.000    0.000    0.000 hash_tables.py:6(__init__)
       39    0.000    0.000    0.000    0.000 tokenize.py:264(generate_tokens)
       32    0.000    0.000    0.000    0.000 {built-in method match}
        1    0.000    0.000    0.003    0.003 memory_profiler.py:522(show_results)
        1    0.000    0.000   12.645   12.645 memory_profiler.py:421(f)
        1    0.000    0.000    0.000    0.000 tokenize.py:174(tokenize_loop)
       16    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
       38    0.000    0.000    0.000    0.000 inspect.py:639(tokeneater)
        1    0.000    0.000    0.000    0.000 hash_tables.py:29(__init__)
        1    0.000    0.000   12.648   12.648 memory_profiler.py:771(wrapper)
        1    0.000    0.000    0.000    0.000 inspect.py:671(getblock)
        1    0.000    0.000    0.000    0.000 memory_profiler.py:455(disable_by_count)
        1    0.000    0.000    0.000    0.000 memory_profiler.py:394(__call__)
        1    0.000    0.000    0.000    0.000 memory_profiler.py:388(__init__)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 tokenize.py:155(tokenize)
        1    0.000    0.000    0.000    0.000 memory_profiler.py:510(enable)
        1    0.000    0.000    0.000    0.000 memory_profiler.py:517(disable)
        1    0.000    0.000    0.000    0.000 genericpath.py:15(exists)
       32    0.000    0.000    0.000    0.000 {built-in method span}
        1    0.000    0.000    0.000    0.000 memory_profiler.py:403(add_function)
        1    0.000    0.000    0.000    0.000 memory_profiler.py:448(enable_by_count)
        1    0.000    0.000    0.000    0.000 inspect.py:632(__init__)
        1    0.000    0.000    0.000    0.000 linecache.py:33(getlines)
        1    0.000    0.000    0.000    0.000 {min}
        1    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 memory_profiler.py:417(wrap_function)
        2    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {getattr}
        1    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {iter}
        2    0.000    0.000    0.000    0.000 {sys.settrace}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {sys.gettrace}
'''
import random
import string
import cProfile

from hash_tables import HashTable

from memory_profiler import profile

def id_generator(size=6, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))        

@profile
def Factory(class_to_test, num_of_entries_to_create):   
    instance = class_to_test()

    for i in range (num_of_entries_to_create):
        exec('instance[i]=id_generator()')

def main():
    cProfile.run('Factory(dict, 1000000)', sort='time')
    cProfile.run('Factory(HashTable, 1000000)', sort='time')

if __name__ == '__main__':
    main()


