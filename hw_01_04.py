def word_input():
    word_list = []
    print("Type 'exit' to stop words entering")
    while True:
        user_input = input()
        if user_input.lower() == 'exit':
            break
        else:
            word_list.append(user_input)
    return word_list

def is_concatenation(word_list, concat_word):
    long_frase = ""
    for word in word_list:
        if concat_word == long_frase:
            return True
        else:
            long_frase += word
    print(long_frase)
    return False

if __name__ == "__main__":
    words = word_input()
    user_word = input("Enter word to check concatenation:\n")
    print(is_concatenation(words, user_word))


