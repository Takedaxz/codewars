def find_outlier(integers):
    first_three=integers[:3]
    odd_count=0
    
    for i in first_three:
        if i%2==1:
            odd_count+=1
            
    for i in integers:
        if odd_count>=2 and i%2==0:
            return i
        elif odd_count<2 and i%2==1:
            return i
        