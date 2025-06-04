
def get_num_words(text): # function to count the number of words in a given text
    words = text.split() # split the text into words using whitespace as the delimiter
    return len(words) # return the number of words by counting the length of the list of words


def get_num_characters(text): # function to count the number of characters in a given text
    char_count = {} #initialize an empty dictionary to hold character counts
    for char in text.lower(): # convert text to lowercase for case-insensitive counting
        if char in char_count: # check if the character is already in the dictionary
            char_count[char] += 1 # increment the count if it is
        else: # if the character is not in the dictionary, add it with a count of 1
            char_count[char] = 1 # add the character to the dictionary with a count of 1
    return char_count # return the dictionary containing character counts

def get_sorted_char_list(char_count):
    char_list = [{"char": char, "num": count} for char, count in char_count.items() if char.isalpha()]
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list