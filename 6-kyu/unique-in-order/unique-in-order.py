def unique_in_order(sequence):
    out=[]
    if len(sequence)==0:
        return []
    out.append(sequence[0])
    x=0
    for i in sequence[1:]:
        if i==out[x]:
            pass
        else:
            out.append(i)
            x+=1
    return out