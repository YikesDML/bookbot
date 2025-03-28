def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

from stats import count_words
from stats import count_characters
from stats import sort_on

#bookbot CH2 L5 Created and moved this to stats.py and replaced with line above
#def count_words(file_contents):
    #words = file_contents.split()
    #return len(words)

def main():
    contents = get_book_text("books/frankenstein.txt")
    word_count = count_words(contents)
    char_count = count_characters(contents)
    print(f"{word_count} words found in the document")
    import json
    print(json.dumps(char_count))
    print(sort_on)
    

#bookbot CH2 L3
#def main():
    #contents = get_book_text("books/frankenstein.txt")
    #print(contents)

main()