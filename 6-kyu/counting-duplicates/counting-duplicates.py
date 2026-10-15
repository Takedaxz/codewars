def duplicate_count(text):
    # Your code goes here
    count={}
    for char in text.lower():
        count[char]=count.get(char,0)+1
    print(count)
    out=[]
    for i,n in count.items():
        if n>1:
            out.append(i)
    
    return len(out)
     