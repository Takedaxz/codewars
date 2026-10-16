def persistence(n):
    # your code
    if len(str(n))==1:
        return 0
    def mult(n):
        out=1
        for num in str(n):
            out*=int(num)
        print(out)
        return out
    res=0
    while n>=10:
        res+=1
        n=mult(n)
        
    return res
        