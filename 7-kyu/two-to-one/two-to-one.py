def longest(a1, a2):
    out=set()
    sum=sorted(a1+a2)
    for i in range(len(sum)):
        out.add(sum[i])
        
        
    return "".join(sorted(out))
    # your code