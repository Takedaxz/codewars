def substring_test(s1, s2):
    s1=s1.lower()
    s2=s2.lower()
    
    for i in range(len(s1)-1):
        pair=s1[i:i+2]
        
        if pair in s2:
            return True
    return False
        