def duplicate_encode(word):
    #your code here
    count={}
    for char in word.lower():
        count[char]=count.get(char,0)+1
        
    out=""
    for i in word.lower():
        if count[i]==1:
            out+="("
        else:
            out+=")"
            
    return out