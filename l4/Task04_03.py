def read_file(path):
    text = ""
    with open(path, 'r') as file:
        for line in file:
            text += line
    return text

def get_words(text):
    src_words = text.split(" ")
    words = []
    for word in src_words:
        if word.isalpha() and not words.count(word):
            words.append(word.lower())
        else:
            new_word = ""
            for i in word:
                if i.isalpha(): new_word += i
            if new_word and not words.count(new_word): words.append(new_word.lower())
    return words

path = input("Enter the first file path: ")
path2 = input("Enter the second file path: ")
first_text = read_file(path)
second_text = read_file(path2)
first_list = get_words(first_text)
second_list = get_words(second_text)
print("Words:")
for word in list(set(first_list) & set(second_list)):
    print(word)


