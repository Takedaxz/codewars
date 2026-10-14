def xo(s):
    check={"x":0,"o":0}
    for char in s.lower():
        if char in check:
            check[char]+=1
    
    return check["x"]==check["o"]