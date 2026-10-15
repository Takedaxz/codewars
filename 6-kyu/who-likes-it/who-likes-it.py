def likes(names):
    # your code here
    len_names=len(names)
    if len_names<=0:
        return "no one likes this"
    elif len_names==1:
        return f"{names[0]} likes this"
    elif len_names==2:
        return f"{names[0]} and {names[1]} like this"
    elif len_names==3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len_names-2} others like this"
    pass