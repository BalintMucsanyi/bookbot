def main():
    string = return_book("books/frankenstein.txt")
    number_of_words = count_words(string)
    print(number_of_words)
    dict = count_letters(string)
    report(dict)

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

def count_letters(book_as_string):
    no_capitals = book_as_string.lower()
    letters_dict = {}
    for word in no_capitals:
        for letter in word:
            if letter not in letters_dict:
                letters_dict[letter] = 0
        letters_dict[letter] += 1
    return letters_dict

def sort_dict_alphanumerically(input_dict):
    sorted_dict = {k: input_dict[k] for k in sorted(input_dict.keys())}
    return sorted_dict

def report(input_dict):
    alpha_dict = {key: value for key, value in input_dict.items() if key.isalpha()}

    alpha_list = sorted(alpha_dict.items(), key=lambda pair: pair[1], reverse=True)

    for char, count in alpha_list:
        print(f"The '{char}' character was found {count} times")
    

main()


#sorted_dict = sort_dict_alphanumerically(dict)
#or key in sorted_dict:    
 #   print(f"{key}: {dict[key]}")
