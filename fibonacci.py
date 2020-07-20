import time

def fib1(n):
    if n <= 1:
        return n
    else:
        return fib1(n-1) + fib1(n-2)

def fib2(n):
    x = []
    x.append(0)
    x.append(1)
    for i in range(2, n+1):
        x.append(x[i-1] + x[i-2])

    return x[n]

if __name__ == "__main__":
    from sys import argv
    n = int(argv[1])
    print("Using in-efficient algorithm")
    for f in [fib1, fib2]:
        print("Using %s" % f.__name__)
        start_time = time.time()
        num = f(n)
        end_time = time.time()
        exec_time = end_time - start_time
        print(num)
        print("Execution time: %f" % exec_time)

