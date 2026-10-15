def solution(text, ending):
    # your code here...
    print(len(ending))
    if ending in text[-len(ending):]:
        return True
    return False