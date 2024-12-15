import os

import docx
from text import text_print


def input_param():
    doc_file = []
    files = input(r"Введите путь к файлам: ")
    text_old = input("Введите слово которое нужно заменить: ")
    text_new = input("Введите слово которое нужно подставить: ")
    try:
        for f in os.scandir(files):
            if f.is_file() and f.path.split('.')[-1].lower() == "docx":
                doc_file.append(f.path)
    except FileNotFoundError:
        print(f"Системе не удается найти указанный путь: {files}")
    return doc_file, text_old, text_new


def create_files():
    doc_files = input_param()
    for doc in doc_files[0]:
        document = docx.Document(doc)
        for paragraph in document.paragraphs:
            paragraph.text = paragraph.text.replace(doc_files[1], doc_files[2])
        document.save(doc)
        print(f"Файл изменен успешно - {doc}")


if __name__ == "__main__":
    text_print()
    while True:
        create_files()