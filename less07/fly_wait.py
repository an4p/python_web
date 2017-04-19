# files shared from my missed lesson
# flyweight
class Character_flyweight:
    def __init__(self, character):
        self.character = character

class Factory:
    def __init__(self):
        self.map = {}
    def instance_character(self, char):
        if self.map.get(char) != None:
            return self.map.get(char)
        else:
            c = Character_flyweight(char)
            self.map[char] = c
            return c

factory = Factory()

def convert_word_to_list(word):
    lis = []
    for char in word:
        lis.append(factory.instance_character(char))
    return lis


lis_word = convert_word_to_list("abbaa")
print (lis_word)

