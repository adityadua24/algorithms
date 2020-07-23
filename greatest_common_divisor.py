import time

def inefficient(n1, n2):
    best = 0
    limit = n1 if n1 < n2 else n2
    for i in range(limit, 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            return i

    return 0

def efficient(n1, n2):
    a = n1 if n1 > n2 else n2
    b = n2 if n2 < n1 else n1
    def compute(x, y):
        if  y == 0:
            return x
        else:
            return compute(y, x % y)

    return compute(a, b)


if __name__ == "__main__":
    from sys import argv
    n1 = int(argv[1])
    n2 = int(argv[2])
    for f in [inefficient, efficient]:
        print("Using %s algorithm..." % f.__name__)
        start_time = time.time()
        num = f(n1, n2)
        end_time = time.time()
        exec_time = end_time - start_time
        print(num)
        print("Execution time: %f" % exec_time)
