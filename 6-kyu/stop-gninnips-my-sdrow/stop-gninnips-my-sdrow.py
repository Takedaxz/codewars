def spin_words(sentence):
    # Your code goes here
    words=sentence.split()
    out=[]
    for word in words:
        if len(word)>=5:
            word=word[::-1]
            out.append(word)
        else:
            out.append(word)
    return " ".join(out)