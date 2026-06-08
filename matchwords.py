def match_words(words):
    ctr = 0 
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)

    print("List of character with the first and last characters the same", lst)
    return ctr
count = match_words(["abc", "cfc", "xyz", "aba", "1221"])
print("The number of word with the first and last character the same is:", count)