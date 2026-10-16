def is_valid_walk(walk):
    #determine if walk is valid
    if len(walk)!=10:
        return False
    count={}
    for i in walk:
        count[i]=count.get(i,0)+1
        
    if count.get('n',0)==count.get('s',0) and count.get('w',0)==count.get('e',0):
        return True
    
    return False
        