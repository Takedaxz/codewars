def solution(number):
    out=0
    for i in range(number):
        if i%3==0 or i%5==0:
            out+=i
    return out
  