from stats import get_num_words

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()



def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    binbong = f"Found {num_words} total words"
    print(binbong)

if __name__ == "__main__":
    main()
