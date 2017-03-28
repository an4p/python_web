def word_count(input_text, some_word):
    counter = 0
    words = input_text.split()

    for word in words:
        word = word.strip('.').strip(",")
        if word.lower() == some_word.lower():
            counter += 1
    return counter

if __name__ == "__main__":
    user_text = input("Enter some text... \n")
    user_word = input("Enter the word you want to count... \n")
    counts = word_count(user_text, user_word)
    print('Your word is met {} times'.format(counts))

