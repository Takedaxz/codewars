def find_it(seq):
    temp = {}
​
    for num in seq:
        temp[num] = temp.get(num, 0) + 1
​
    for number, count in temp.items():
        if count % 2 == 1:
            return number
​
    return 0