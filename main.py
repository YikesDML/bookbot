def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def main():
    contents = get_book_text("books/frankenstein.txt")
    word_count = count_words(contents)
    print(f"{word_count} words found in the document")

#bookbot CH2 L3
#def main():
    #contents = get_book_text("books/frankenstein.txt")
    #print(contents)

main()
