import string


def word_len():
    print("Слов в тексте =", len(list_word.split()))


def longest_word():
    words = list_word.split()
    longest = max(words, key=len)
    print("Самое длинное слово =", longest)


def number_vowels():
    vowels = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я", "a", "e", "i", "o", "u", "y"]
    count = 0
    for word in list_word:
        if word in vowels:
            count += 1
    print("Количество гласных =", count)


def word_meet_up():
    words = list_word.split()
    x = []
    for word in words:
        if word in x:
            break
        x.append(word)
        print(word, words.count(word))


if __name__ == "__main__":
    list_word = input("Введите или скопируйте текст ")
    translator = str.maketrans('', '', string.punctuation)
    list_word = list_word.translate(translator)
    word_len()
    longest_word()
    number_vowels()
    word_meet_up()
