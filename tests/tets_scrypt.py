import pytest
import sys
sys.path.append(".")
from Main import read_file, split_text, count_words_and_sentences, save_result

# Fixture для зчитування вмісту файлу
@pytest.fixture
def test_text():
    filename = "index.txt"
    return read_file(filename)

## Фіксований тест для функції read_file
def test_read_file(test_text):
    expected_text = "Це текст для демонстрації Python-скрипта.\n\nКожне речення закінчується крапкою, знаком питанням або оклику?\nТекст містить кілька речень!"
    assert expected_text in test_text

# Параметризований тест для функції split_text
@pytest.mark.parametrize("test_text, expected_sentences", [
    ("Це текст для демонстрації Python-скрипта.\n\nКожне речення закінчується крапкою, знаком питанням або оклику?\nТекст містить кілька речень!\nТекст може містити розділові знаки: кома, пробіл, двокрапка; крапка з комою.\nКілька речень у тексті!\nОсь останнє речення в тексті.",
     ['Це текст для демонстрації Python-скрипта.', 'Кожне речення закінчується крапкою, знаком питанням або оклику?', 'Текст містить кілька речень!', 'Текст може містити розділові знаки: кома, пробіл, двокрапка; крапка з комою.', 'Кілька речень у тексті!', 'Ось останнє речення в тексті.'])
])
def test_split_text(test_text, expected_sentences):
    sentences = split_text(test_text)[1]  # Отримання речень з результату розділення тексту
    assert sentences == expected_sentences

# Parametrize тест для функції count_words_and_sentences
@pytest.mark.parametrize("words, sentences, expected_word_count, expected_sentence_count", [
    (['This', 'is', 'a', 'sample', 'text', 'It', 'contains', 'multiple', 'sentences', 'And', 'some', 'words'],
     ['This is a sample text', 'It contains multiple sentences', 'And some words'],
     12, 3)
])
def test_count_words_and_sentences(words, sentences, expected_word_count, expected_sentence_count):
    word_count, sentence_count = count_words_and_sentences(words, sentences)
    assert word_count == expected_word_count
    assert sentence_count == expected_sentence_count