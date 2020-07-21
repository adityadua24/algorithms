import time

def inefficient(n):
    if n <= 1:
        return n
    else:
        return inefficient(n-1) + inefficient(n-2)

def efficient(n):
    x = []
    x.append(0)
    x.append(1)
    for i in range(2, n+1):
        x.append(x[i-1] + x[i-2])

    return x[n]

if __name__ == "__main__":
    from sys import argv
    n = int(argv[1])
    for f in [inefficient, efficient]:
        print("Using %s algorithm..." % f.__name__)
        start_time = time.time()
        num = f(n)
        end_time = time.time()
        exec_time = end_time - start_time
        print(num)
        print("Execution time: %f" % exec_time)

