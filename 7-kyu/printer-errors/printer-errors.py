def printer_error(s):
    # your code
    len_s=len(s)
    error=0
    for char in s:
        if char<"a" or char>"m":
            error+=1
            
    return f"{error}/{len_s}"