from art import tprint, lprint


def text_print():
    lprint(length=90, height=1, char="*")
    print("Разработчик: https://github.com/jforsety")
    lprint(length=90, height=1, char="*")
    tprint("Change files", space=2)
    print("Программа позволяет изменять слова в docx файлах")
    lprint(length=90, height=1, char="*")