word = input("Enter a word. \nIt will be checked if it is a palindrome.\n")
word = word.lower()

def palindrome(word):
    for i in range(len(word)//2):
        if (len(word) < 2) or word[i] != word[-i-1]:
            return False
        else:
            continue
    return True

print(palindrome(word))