def sort_array(source_array):
    odd_arr=[]
    for x in source_array:
        if x%2==1:
            odd_arr.append(x)
    
    odd_arr.sort()
    i=0
    for x in range(len(source_array)):
        if source_array[x]%2==1:
            source_array[x]=odd_arr[i]
            i+=1
    
    return source_array