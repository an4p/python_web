def is_concatinate(word, dictionary):
    if (word == ""):
        return True

    for i in range(1,len(word)+1):
        temp=word[0:i]
        if temp in dictionary:
            print(temp)
            print(word[i:])
            if is_concatinate(word[i:],dictionary):
                return True
    return False

print(is_concatinate("aabbb", ["aab", "aa", "bb", "cdf"]))



