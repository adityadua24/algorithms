import time

def efficient(array):
    if len(array) == 1:
        return array[0]

    max1 = array[0]
    max2 = 1

    array.pop(0)

    for i in array:
        if i >= max1:
            max2 = max1
            max1 = i
        if i < max1 and i > max2:
            max2 = i
    return max1*max2

def inefficient(array):
    result = 0
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j and array[i] * array[j] > result:
                result = array[i] * array[j]
    return result

if __name__ == "__main__":
    from sys import argv
    array = list(map(int, argv[1].split(",")))
    for f in [efficient, inefficient]:
        print("Using %s algorithm" % f.__name__)
        start_time = time.time()
        prod = f(array)
        end_time = time.time()
        exec_time = end_time - start_time
        print(prod)
        print("Execution time: %s" % exec_time)

