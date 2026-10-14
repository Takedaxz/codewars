def to_jaden_case(string):
    out=string[0].upper()
    for i in range(1,len(string)):
        if string[i-1]==" ":
            out+=string[i].upper()
        else:
            out+=string[i].lower()
    return out