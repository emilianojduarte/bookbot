def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    cant = count_words(text)
    caracteres = count_chars(text)
    get_report(book_path, cant, caracteres)
    return

def read_book(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    chars = {}
    for char in text:
        if char.lower() in chars:
            chars[char.lower()] += 1
        else:
            if char.lower() >= 'a' and char.lower() <= 'z':
                chars[char.lower()] = 1
    return chars

def get_report(book_path, cant, caracteres):
    print(f"--- Begin report of {book_path} ---")
    print(f"{cant} words found in the document\n")
    sorted_caracteres = dict(sorted(caracteres.items()))
    for car in sorted_caracteres:
        print(f"The '{car}' character was found {sorted_caracteres[car]} times")
    print("--- End report ---")

main()