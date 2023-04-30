from time import perf_counter
import sys

sys.setrecursionlimit(1500)



def slow_fib(n):
    if n <= 2:
        return 1
    else:
        return slow_fib(n-1) + slow_fib(n-2)

def fib(n, dict = {}):
    if n in dict:
        return dict[n]
    elif n <= 2:
        return 1
    else:
        dict[n] = fib(n-1, dict) + fib(n-2, dict)
        return dict[n]

start = perf_counter()    
print(fib(1499))
end = perf_counter()
time = end-start
print("it took ", time, "seconds")

start = perf_counter()    
print(slow_fib(35))
end = perf_counter()
time = end-start
print("it took ", time, "seconds")
