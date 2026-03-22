from urllib.parse import unquote
import pyperclip


def decode_url(encoded_url):
    """Декодує URL у читабельний вигляд."""
    return unquote(encoded_url)


def main():
    encoded_url = input("Введіть закодоване посилання: ").strip()

    decoded_url = decode_url(encoded_url)

    print("\nДекодоване посилання:")
    print(decoded_url)

    pyperclip.copy(decoded_url)
    print("\nПосилання скопійовано в буфер обміну.")


if __name__ == "__main__":
    main()