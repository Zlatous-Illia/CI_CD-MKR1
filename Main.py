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
    sentences = re.split(r'[\.\?!]+', text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

    # Розділяємо кожне речення на слова
    final_sentences = []
    for sentence in sentences:
        final_sentences.append(sentence)

    return words, final_sentences


def count_words_and_sentences(words: List[str], sentences: List[str]) -> Tuple[int, int]:
    """Функція для підрахунку кількості слів та речень"""
    return len(words), len(sentences)


def save_result(filename: str, word_count: int, sentence_count: int):
    """Метод для збереження результату у файл"""
    with open(filename, 'w') as file:
        file.write(f"Кількість слів у файлі: {word_count}\n")
        file.write(f"Кількість речень у файлі: {sentence_count}\n")


def main():
    filename = "text.txt"  # Шлях до файлу
    result_filename = "result.txt"  # Ім'я файлу для збереження результатівy
    text = read_file(filename)
    words, sentences = split_text(text)
    word_count, sentence_count = count_words_and_sentences(words, sentences)
    print("Кількість слів у файлі:", word_count)
    print("Кількість речень у файлі:", sentence_count)
    save_result(result_filename, word_count, sentence_count)

if __name__ == "__main__":
    main()
