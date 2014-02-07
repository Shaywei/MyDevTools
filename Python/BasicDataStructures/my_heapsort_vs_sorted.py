'''
My heapsort is TERRIBLE vs. sorted()... (52.2 secs vs 2.3secs with memory profiler and 7.05 vs 0.134 without...)
T__T

****************************

         100004 function calls in 0.134 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.066    0.066    0.066    0.066 {sorted}
        1    0.057    0.057    0.133    0.133 my_heapsort_vs_sorted.py:188(sort_by)
   100000    0.010    0.000    0.010    0.000 {method 'random' of '_random.Random' objects}
        1    0.001    0.001    0.134    0.134 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


[Finished in 0.3s]

***************************

         11939754 function calls (10411238 primitive calls) in 7.075 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
1500726/99999    3.710    0.000    6.051    0.000 heaps.py:54(_bubbledown)
  3001452    1.743    0.000    1.967    0.000 heaps.py:50(_child)
  3080540    0.408    0.000    0.408    0.000 {operator.lt}
227789/100000    0.291    0.000    0.448    0.000 heaps.py:39(_bubbleup)
  3201453    0.239    0.000    0.239    0.000 {len}
   100000    0.166    0.000    6.252    0.000 heaps.py:25(extract_root)
        1    0.162    0.162    7.003    7.003 heaps.py:4(heapsort)
   227789    0.124    0.000    0.157    0.000 heaps.py:47(_dominates)
   100000    0.096    0.000    0.561    0.000 heaps.py:20(insert)
        1    0.058    0.058    7.069    7.069 my_heapsort_vs_sorted.py:159(sort_by)
   200000    0.045    0.000    0.045    0.000 {method 'pop' of 'list' objects}
   200000    0.019    0.000    0.019    0.000 {method 'append' of 'list' objects}
   100000    0.008    0.000    0.008    0.000 {method 'random' of '_random.Random' objects}
        1    0.006    0.006    7.075    7.075 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 heaps.py:16(__init__)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


[Finished in 7.3s]

************ WITH MEMORY PROFILER *****************

Filename: C:\dev\MyDevTools\Python\BasicDataStructures\my_heapsort_vs_sorted.py

Line #    Mem usage    Increment   Line Contents
================================================
    13     11.7 MiB      0.0 MiB   @profile
    14                             def sort_by(heapsort=True):   
    15     16.2 MiB      4.5 MiB       l = [int(100000*random.random()) for x in xrange(100000)]
    16     16.2 MiB      0.0 MiB       if heapsort:
    17                                   Heap.heapsort(l)
    18                                 else:
    19     15.5 MiB     -0.7 MiB         sorted(l)


         100308 function calls in 2.292 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    2.223    2.223    2.290    2.290 my_heapsort_vs_sorted.py:13(sort_by)
        1    0.053    0.053    0.053    0.053 {sorted}
   100000    0.013    0.000    0.013    0.000 {method 'random' of '_random.Random' objects}
        1    0.001    0.001    2.291    2.291 memory_profiler.py:429(f)
        2    0.000    0.000    0.000    0.000 {nt.stat}
       53    0.000    0.000    0.000    0.000 {method 'match' of '_sre.SRE_Pattern' objects}
       61    0.000    0.000    0.000    0.000 tokenize.py:264(generate_tokens)
        1    0.000    0.000    0.001    0.001 memory_profiler.py:522(show_results)
        1    0.000    0.000    0.000    0.000 tokenize.py:174(tokenize_loop)
        1    0.000    0.000    0.000    0.000 {open}
       11    0.000    0.000    0.000    0.000 {method 'write' of 'file' objects}
        1    0.000    0.000    0.000    0.000 {method 'readlines' of 'file' objects}
       60    0.000    0.000    0.000    0.000 inspect.py:641(tokeneater)
       17    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
        1    0.000    0.000    0.001    0.001 inspect.py:673(getblock)
        1    0.000    0.000    0.000    0.000 linecache.py:68(updatecache)
        1    0.000    0.000    0.000    0.000 linecache.py:33(getlines)
        1    0.000    0.000    2.292    2.292 memory_profiler.py:771(wrapper)
       53    0.000    0.000    0.000    0.000 {method 'span' of '_sre.SRE_Match' objects}
        1    0.000    0.000    0.000    0.000 memory_profiler.py:463(disable_by_count)
        1    0.000    0.000    0.000    0.000 memory_profiler.py:402(__call__)
        1    0.000    0.000    0.001    0.001 tokenize.py:155(tokenize)
        1    0.000    0.000    0.000    0.000 memory_profiler.py:517(disable)
        1    0.000    0.000    0.000    0.000 genericpath.py:15(exists)
        1    0.000    0.000    0.000    0.000 memory_profiler.py:396(__init__)
        1    0.000    0.000    2.292    2.292 <string>:1(<module>)
        2    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        2    0.000    0.000    0.000    0.000 {sys.settrace}
        1    0.000    0.000    0.000    0.000 memory_profiler.py:411(add_function)
        1    0.000    0.000    0.000    0.000 memory_profiler.py:511(enable)
        1    0.000    0.000    0.000    0.000 inspect.py:634(__init__)
       12    0.000    0.000    0.000    0.000 {len}
        1    0.000    0.000    0.000    0.000 memory_profiler.py:456(enable_by_count)
        3    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {range}
        1    0.000    0.000    0.000    0.000 {min}
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {iter}
        1    0.000    0.000    0.000    0.000 memory_profiler.py:425(wrap_function)
        1    0.000    0.000    0.000    0.000 {getattr}
        1    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


[Finished in 2.6s]

**************************
Filename: C:\dev\MyDevTools\Python\BasicDataStructures\my_heapsort_vs_sorted.py

Line #    Mem usage    Increment   Line Contents
================================================
    80     11.7 MiB      0.0 MiB   @profile
    81                             def sort_by(heapsort=True):   
    82     15.7 MiB      4.0 MiB       l = [int(100000*random.random()) for x in xrange(100000)]
    83     15.7 MiB      0.0 MiB       if heapsort:
    84     15.1 MiB     -0.6 MiB         Heap.heapsort(l)
    85                                 else:
    86                                   sorted(l)


         11939021 function calls (10410835 primitive calls) in 51.693 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
1500749/99999   27.636    0.000   42.237    0.000 heaps.py:54(_bubbledown)
  3001498   13.847    0.000   14.146    0.000 heaps.py:50(_child)
        1    3.838    3.838   51.685   51.685 my_heapsort_vs_sorted.py:80(sort_by)
227436/100000    2.063    0.000    2.739    0.000 heaps.py:39(_bubbleup)
   100000    1.051    0.000   43.327    0.000 heaps.py:25(extract_root)
        1    0.964    0.964   47.832   47.832 heaps.py:4(heapsort)
   100000    0.745    0.000    3.507    0.000 heaps.py:20(insert)
   227436    0.639    0.000    0.676    0.000 heaps.py:47(_dominates)
  3080094    0.491    0.000    0.491    0.000 {operator.lt}
  3201511    0.319    0.000    0.319    0.000 {len}
   200000    0.051    0.000    0.051    0.000 {method 'pop' of 'list' objects}
   200003    0.026    0.000    0.026    0.000 {method 'append' of 'list' objects}
   100000    0.015    0.000    0.015    0.000 {method 'random' of '_random.Random' objects}
        1    0.006    0.006   51.691   51.691 memory_profiler.py:429(f)
        2    0.000    0.000    0.000    0.000 {nt.stat}
       11    0.000    0.000    0.000    0.000 {method 'write' of 'file' objects}
       53    0.000    0.000    0.000    0.000 {method 'match' of '_sre.SRE_Pattern' objects}
       61    0.000    0.000    0.000    0.000 tokenize.py:264(generate_tokens)
        1    0.000    0.000    0.002    0.002 memory_profiler.py:522(show_results)
        1    0.000    0.000    0.000    0.000 {method 'readlines' of 'file' objects}
       17    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {open}
        1    0.000    0.000    0.001    0.001 tokenize.py:174(tokenize_loop)
       60    0.000    0.000    0.000    0.000 inspect.py:641(tokeneater)
        1    0.000    0.000    0.001    0.001 inspect.py:673(getblock)
        1    0.000    0.000    0.000    0.000 linecache.py:68(updatecache)
        1    0.000    0.000   51.693   51.693 memory_profiler.py:771(wrapper)
       53    0.000    0.000    0.000    0.000 {method 'span' of '_sre.SRE_Match' objects}
        1    0.000    0.000    0.000    0.000 memory_profiler.py:463(disable_by_count)
        1    0.000    0.000    0.000    0.000 linecache.py:33(getlines)
        1    0.000    0.000    0.000    0.000 memory_profiler.py:402(__call__)
        1    0.000    0.000    0.001    0.001 tokenize.py:155(tokenize)
        1    0.000    0.000    0.000    0.000 heaps.py:16(__init__)
        1    0.000    0.000   51.693   51.693 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 memory_profiler.py:517(disable)
        1    0.000    0.000    0.000    0.000 genericpath.py:15(exists)
        2    0.000    0.000    0.000    0.000 {sys.settrace}
        1    0.000    0.000    0.000    0.000 memory_profiler.py:396(__init__)
        2    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        1    0.000    0.000    0.000    0.000 memory_profiler.py:411(add_function)
        1    0.000    0.000    0.000    0.000 {range}
        1    0.000    0.000    0.000    0.000 memory_profiler.py:511(enable)
        1    0.000    0.000    0.000    0.000 {min}
        1    0.000    0.000    0.000    0.000 inspect.py:634(__init__)
        1    0.000    0.000    0.000    0.000 memory_profiler.py:456(enable_by_count)
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {iter}
        1    0.000    0.000    0.000    0.000 memory_profiler.py:425(wrap_function)
        1    0.000    0.000    0.000    0.000 {getattr}
        1    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


[Finished in 52.2s]
'''
import random
import string
import cProfile


from heaps import Heap

from memory_profiler import profile

def id_generator(size=6, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))        

#@profile
def sort_by(heapsort=True):   
    l = [int(100000*random.random()) for x in xrange(100000)]
    if heapsort:
      Heap.heapsort(l)
    else:
      sorted(l)

def main():
    #cProfile.run('sort_by()', sort='time')
    cProfile.run('sort_by(False)', sort='time')

if __name__ == '__main__':
    main()


