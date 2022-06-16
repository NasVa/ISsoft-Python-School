alphabet_dict = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••', 'e': '•', 'f': '••—•', 'g': '——•',
                'h': '••••', 'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••', 'm': '——', 'n': '—•',
               'o': '———', 'p': '•——•', 'q': '——•—', 'r': '•—•', 's': '•••', 't': '—', 'u': '••—',
              'v': '•••—', 'w': '•——', 'x': '—••—', 'y': '—•——', 'z': '——••',
              '0' : '—————', '1' : '•————', '2' : '••———', '3' : '•••——', '4' : '••••—',
              '5' : '•••••', '6' : '—••••', '7' : '——•••', '8' : '———••', '9' : '————•', ' ' : ' ', '\n' : '\n'}

def translate_text(text):
    is_dec = '•' in text or '—' in text
    words_separates = [" " * 3, " "]
    letters_separate = " "
    dictionary = {value: key for key, value in alphabet_dict.items()} if is_dec else alphabet_dict
    if not is_dec:
        words_separates.reverse()
        text = text.lower()
    words = text.split(words_separates[0])
    new_text = ""
    for word in words:
        new_word = ""
        letters = list(word.split(letters_separate) if is_dec else word)
        for letter in letters: 
            if not letter:
                continue
            new_word += dictionary[letter]
            if not is_dec:
                new_word += letters_separate
        new_text += new_word + letters_separate * (1 if is_dec else 2)
    if is_dec and new_text[0].isalpha():
        new_text = new_text[0].upper() + str((new_text)[1:])
    return new_text

def read_file(path):
    text = ""
    try:
        with open(path, 'r') as file:
            for line in file:
                text += line
    except IOError:
        print(IOError)
    return text

def write_file(path, text):
    try:
        if '•' in text or '—' in text:
            with open(path.split('.')[:-1][-1] + '.cod.' + path.split('.')[-1:][-1], 'w') as file:
                file.write(text)
        else:
            with open(path.split('.')[:-2][-1] + '.' + path.split('.')[-1:][-1], 'w') as file:
                file.write(text)
    except IOError:
        print(IOError)

file_path = input("Введите путь к файлу: ")
input_text = read_file(file_path)
output_text = translate_text(input_text)
write_file(file_path, output_text)

