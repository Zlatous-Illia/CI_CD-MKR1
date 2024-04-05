import re
from typing import List, Tuple


def read_file(filename: str) -> str:
    """Метод для зчитування вмісту файлу і повернення у форматі тексту"""
    with open(filename, 'r') as file:
        return file.read()


def split_text(text: str) -> Tuple[List[str], List[str]]:
    """Метод для розділу тексту на слова та речення"""
    words = re.findall(r'\b\w+\b', text)

    # Розділяємо текст на речення за всіма можливими символами, які можуть завершувати речення
    sentences = re.split(r'(?<=[.!?])\s*', text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

    # Розділяємо кожне речення на слова
    final_sentences = []
    for sentence in sentences:
        final_sentences.append(sentence)

    return words, final_sentences


def main():
    filename = "text.txt"  # Шлях до файлу
    text = read_file(filename)
    words, sentences = split_text(text)

if __name__ == "__main__":
    main()
