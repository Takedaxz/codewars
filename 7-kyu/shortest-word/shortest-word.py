def find_short(s):
    words=s.split()
    print(words)
    min_word=len(words[0])
    for word in words:
        min_word=min(min_word,len(word))
    return min_word