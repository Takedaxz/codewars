def narcissistic( value ):
    x=1
    check=0
    for i in range (len(str(value))):
        check+=int(str(value)[i])**len(str(value))
        x+=1
        print(check)
    if check==value:
        return True
    return False # Code away