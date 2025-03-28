#Total Words
def count_words(file_contents):
    words = file_contents.split()
    return len(words)

#Character Counts
def count_characters(file_contents):
    character_dict  = {}
    lowercase_file = file_contents.lower()
    from collections import Counter
    characters = Counter(lowercase_file)
    return characters

#Sort Dictionaries
def sort_on(count_characters):
    character_dict = dict(characters)
    return character_dict