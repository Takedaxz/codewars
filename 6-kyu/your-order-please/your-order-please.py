def order(sentence):
    words=sentence.split()
    out=[]
    for i in range(1, len(words) + 1):
        for word in words:
            if str(i) in word:
                out.append(word)
                break
​
    return " ".join(out)
        
        