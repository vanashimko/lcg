def minmax(data):
    iterator = iter(data)
    try:
        smallest = biggest = next(iterator)
    except StopIteration:
        raise ValueError('data is an empty sequence')
    for x in iterator:
        if x < smallest:
            smallest = x
        if x > biggest:
            biggest = x
    return smallest, biggest


def uniform_ratio(numbers):
    length = len(numbers)
    if length % 2:
        length = length - 1
    pairs = ((numbers[i], numbers[i+1]) for i in range(0, length, 2))
    K = sum(1 for x1, x2 in pairs if x1**2 + x2**2 < 1)
    return 2*K / len(numbers)


def random_vector(length, lgc_parameters):
    x = lgc_parameters.initial
    for i in range(length):
        x = (x * lgc_parameters.multiplyer) % lgc_parameters.base
        yield x/lgc_parameters.base


def last_element(iterable):
    try:
        result = next(iterable)
    except StopIteration:
        raise ValueError('Empty iterable')
    for result in iterable:
        pass
    return result


def period(generator):
    initial = 1
    length = 10**6

    last = last_element(generator(length, initial))
    start = end = None
    for i, x in enumerate(generator(length, initial)):
        if x == last:
            if not start:
                start = i
            else:
                end = i
                break
    if not (start and end):
        return None
    else:
        return end - start
