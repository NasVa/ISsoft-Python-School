# Способ 1
def reverse_words(str):
    result = ""
    word = ""
    for i in range(0, len(str)):
        if str[i] == " " or i == len(str)-1:
            if i == len(str)-1:
                word += str[i]
            for j in range (len(word)-1, -1, -1):
                result += word[j]
            if i != len(str)-1 : result += " "
            word = ""
        else:
            word += str[i]
    return result

#Способ 2
def reverse_words2(str):
    words = str.split(" ")
    result_list = []
    s = ""
    for word in words:
        word_letters = list(word)
        word_letters.reverse()
        reversed_word = "".join(word_letters)
        result_list.append(reversed_word)
    return " ".join(result_list)

str = input("Введите строку: ")
print(reverse_words(str))
print(reverse_words2(str))
