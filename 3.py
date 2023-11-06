def anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    print("Преобразуем первую строку:", str1)
    print("Преобразуем вторую строку:", str2)

    set1 = set(str1)
    set2 = set(str2)

    print("Множество символов первой строки:", set1)
    print("Множество символов второй строки:", set2)

    if set1 == set2:
        return True
    else:
        return False


string1 = input("Введите первую строку: ")
string2 = input("Введите вторую строку: ")


if anagram(string1, string2):
    print("Эти строки являются анаграммами.")
else:
    print("Эти строки не являются анаграммами.")

# примеры для ввода
# "listen" и "silent"
# "debit card" и "bad credit"
# "astronomer" и "moon starer"
# "eleven plus two" и "twelve plus one"
# "funeral" и "real fun"