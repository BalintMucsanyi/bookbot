def main():
    pass

def return_book(path_to_book):
    with open(path_to_book) as f:
        file_contents = f.read()
        #print(file_contents)
    return file_contents

def count_words(book_as_string):
    words = book_as_string.split()
    word_counter = 0
    for word in words:
        word_counter += 1
    return word_counter

main()
string = return_book("books/frankenstein.txt")
number_of_words = count_words(string)
print(number_of_words)