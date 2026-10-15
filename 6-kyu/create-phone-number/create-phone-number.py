def create_phone_number(n):
    g1 = "".join(map(str, n[0:3]))
    g2 = "".join(map(str, n[3:6]))
    g3 = "".join(map(str, n[6:10]))
​
    return f"({g1}) {g2}-{g3}"