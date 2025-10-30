def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()



def word_count():
    text = get_book_text("books/frankenstein.txt")
    words = len(text.split())
    return words

def main():
    num_words = word_count()
    binbong = f"Found {num_words} total words"
    print(binbong)

if __name__ == "__main__":
    main()
