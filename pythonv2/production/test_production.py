from production.production import my_function, my_function2, my_function3, my_function4, my_function5
from memory_profiler import memory_usage

#10, 20, 50, 100, 200, 500
#recuerda usar pytest memory
def test_my_function(benchmark):
    n = 1024
    result = benchmark(my_function, n)
    mem_usage = memory_usage((my_function, (n,)), interval=0.1, timeout=None)
    print(f"Uso de memoria para my_function con n={n}: {max(mem_usage)} MB")

def test_my_function2(benchmark):
    n = 1024
    result = benchmark(my_function2, n)
    mem_usage = memory_usage((my_function2, (n,)), interval=0.1, timeout=None)
    print(f"Uso de memoria para my_function2 con n={n}: {max(mem_usage)} MB")

def test_my_function3(benchmark):
    n = 1024
    result = benchmark(my_function3, n)
    mem_usage = memory_usage((my_function3, (n,)), interval=0.1, timeout=None)
    print(f"Uso de memoria para my_function3 con n={n}: {max(mem_usage)} MB")

def test_my_function4(benchmark):
    n = 1024
    result = benchmark(my_function4, n)
    mem_usage = memory_usage((my_function4, (n,)), interval=0.1, timeout=None)
    print(f"Uso de memoria para my_function4 con n={n}: {max(mem_usage)} MB")

def test_my_function5(benchmark):
    n = 1024
    result = benchmark(my_function5, n)
    mem_usage = memory_usage((my_function5, (n,)), interval=0.1, timeout=None)
    print(f"Uso de memoria para my_function5 con n={n}: {max(mem_usage)} MB")