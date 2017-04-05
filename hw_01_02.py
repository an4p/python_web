def words_count(input_text):
    count_dict = {}
    tmp_list = input_text.lower().split()
    words = []
    for word in tmp_list:
        word = word.strip(".").strip(",")
        words.append(word.strip(".").strip(",").strip("-").strip("*").strip("!"))
    for word in words:
        if word not in count_dict:
            count_dict[word] = 1
        else:
            count_dict[word] += 1
    return(count_dict)

if __name__ == "__main__":
    text = input("Enter some text...\n")
    text_dict = words_count(text)
    for key, value in text_dict.items():
        print("{word} : {count}".format(word=key, count=value))
