def read_file(path):
    text = ""
    with open(path, 'r') as file:
        for line in file:
            text += line
    return text

def find_word(text):
    src_words = text.split(" ")
    words = []
    for word in src_words:
        if word.isalpha():
            words.append(word.lower())
        else:
            new_word = ""
            for i in word:
                if i.isalpha(): new_word += i
            if new_word: words.append(new_word.lower())
    sorted_list = sorted(words, key=lambda x: words.count(x))
    return sorted_list[-1]

path = input("Enter the file path: ")
text = read_file(path)
print(f"The most frequently used word: {find_word(text)}")

