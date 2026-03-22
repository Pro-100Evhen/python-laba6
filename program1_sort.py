import re


UKRAINIAN_ALPHABET = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
LATIN_ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def get_word_category(word):
    """Повертає пріоритет слова для сортування."""
    clean_word = re.sub(r"^[^\w]+|[^\w]+$", "", word, flags=re.UNICODE)

    if not clean_word:
        return 2

    first_char = clean_word[0].lower()

    if first_char in UKRAINIAN_ALPHABET:
        return 0
    if first_char in LATIN_ALPHABET:
        return 1

    return 2


def sorting_key(word):
    """Ключ сортування: спочатку категорія, потім слово без урахування регістру."""
    cleaned = re.sub(r"^[^\w]+|[^\w]+$", "", word, flags=re.UNICODE).lower()
    return get_word_category(word), cleaned


def main():
    file_name = "input_text.txt"

    with open(file_name, "r", encoding="utf-8") as file:
        text = file.read()

    print("Початковий текст:\n")
    print(text)

    words = text.split()
    sorted_words = sorted(words, key=sorting_key)

    print("\nВідсортовані слова:\n")
    print(sorted_words)


if __name__ == "__main__":
    main()
