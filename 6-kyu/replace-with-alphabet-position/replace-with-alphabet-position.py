def alphabet_position(text):
    alp={}
    start=ord("a")
    for i in range(1,27):
        alp[chr(start)]=i
        start+=1
    out=[]
    for char in text.lower():
        if char in alp:
            out.append(str(alp[char]))
    
    return " ".join(out)