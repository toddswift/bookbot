import sys
from stats import get_num_words # function to count the number of words in a given text
from stats import get_num_characters # function to count the number of characters in a given text
from stats import get_sorted_char_list # function to get a sorted list of characters and their counts

def get_book_text(filepath): # function to read the content of a book from a file
    try: # open the file at the specified filepath
        with open(filepath, 'r', encoding='utf-8') as file: # read the file with UTF-8 encoding
            return file.read() # return the content of the file as a string
    except FileNotFoundError: # handle the case where the file does not exist
        return "Error: File not found." # return an error message if the file is not found
    except Exception as e: # handle any other exceptions that may occur
        return f"Error reading file: {str(e)}" # return a generic error message with the exception details

 
def main(): # main function to execute the script

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("debugging............")
    print(sys.argv[1])
    book_path = sys.argv[1] # get the book path from command line arguments
    #book_path = "books/frankenstein.txt" # specify the path to the book file
    book_content = get_book_text(book_path) # read the content of the book file
    #print(book_content)
    #print (count_words(book_content), "words found in the document")
    #print(f"{get_num_words(book_content)} words found in the document") # count the number of words in the book content
    
    char_count = get_num_characters(book_content)  # count the number of characters in the book content
    #print(f"{get_num_words(book_content)} words found in the document") # print the number of words found in the document
    #print("\nCharacter counts:") # print a header for character counts
    #print(char_count) # print the character counts in the book content

    word_count = get_num_words(book_content)
    char_count = get_num_characters(book_content)
    sorted_char_list = get_sorted_char_list(char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_char_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    
if __name__ == "__main__": # check if the script is being run directly
    main() # if so, call the main function to execute the script

