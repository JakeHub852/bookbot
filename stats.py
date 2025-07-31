def get_num_words(contents):
    words = contents.split()
    num_words = len(words)
    return num_words

def get_num_chars(contents):
    num_of_chars = {}


    for char in contents:
        lowercase_char = char.lower()
        if lowercase_char in num_of_chars:
            num_of_chars[lowercase_char] += 1
        else:   
            num_of_chars[lowercase_char] = 1

    return num_of_chars

def sorted_chars(num_of_chars):
    char_list = []

    for char in num_of_chars:
        char_list.append({"char": char, "num": num_of_chars[char]})

    def sort_on(item):
        return item["num"]

    char_list.sort(key=sort_on, reverse=True)

    return char_list