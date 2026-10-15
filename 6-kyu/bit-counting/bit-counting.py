def count_bits(n):
    count=0
    while n>0:
        remain=n%2
        n=n//2
        if remain%2==1:
            count+=1 
        
    return count
        