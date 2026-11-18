def stat(strg):
    if not strg:
        return ""
​
    s = strg.split(", ")
    res = []
​
    for i in s:
        h, m, sec = map(int, i.split("|"))
        res.append(h * 3600 + m * 60 + sec)
​
    res.sort()
    n = len(res)
​
    min_res = res[0]
    max_res = res[-1]
    avg_res = sum(res) // n
​
    med_res = (
        res[n // 2]
        if n % 2 == 1
        else (res[n // 2 - 1] + res[n // 2]) // 2
    )
​
    def sec_to_hr(sec):
        hr = sec // 3600
        minute = (sec % 3600) // 60
        second = sec % 60
​
        return f"{hr:02d}|{minute:02d}|{second:02d}"
​
    return (
        f"Range: {sec_to_hr(max_res - min_res)} "
        f"Average: {sec_to_hr(avg_res)} "
        f"Median: {sec_to_hr(med_res)}"
    )