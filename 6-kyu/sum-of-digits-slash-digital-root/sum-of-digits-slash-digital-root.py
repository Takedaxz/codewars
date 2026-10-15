def digital_root(n):
    def sum(n):
        out=0
        while n>0:
            out+=n%10
            n=n//10
        return out
    while n>=10:
        n=sum(n)
    
    return n
        