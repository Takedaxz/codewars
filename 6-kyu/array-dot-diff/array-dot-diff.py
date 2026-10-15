def array_diff(a, b):
    out=[]
    if len(b)<=0:
        return a
    for i in a:
        if i not in b:
            out.append(i)
    return out