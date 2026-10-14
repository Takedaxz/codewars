def sequence_sum(begin_number, end_number, step):
    if step == 0:
        return begin_number
​
    n = (end_number - begin_number) // step + 1
​
    if n <= 0:
        return 0
​
    last = begin_number + (n - 1) * step
    return n * (begin_number + last) // 2