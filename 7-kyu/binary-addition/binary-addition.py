def add_binary(a, b):
    sum=a+b
    result=""
​
    while sum>0:
        remain=sum%2
        result=str(remain)+result
        sum=sum//2
​
    return result