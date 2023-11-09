def in_range(start, end=None, step=1):
    if (end is None) and start > 0:
        index = 0
        while not index == start:
            yield index
            index += step
    else:
        if not end is None:
            index = start
            if step < 0:
                while not index <= end:
                    index += step
                    yield index - step
            elif step > 0:
                while not index >= end:
                    index += step
                    yield index - step


print(list(in_range(10)))


print(list(range(10)))
