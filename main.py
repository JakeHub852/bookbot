from stats import word_count, char_counts, sort_chars # Import helper functions from stats.py
import sys # Needed so we can use sys.argv to read comamand-line arguments

def get_book_text(filepath):
    # Opens a text file and reads its full contents into a string
    with open(filepath) as f: 
        file_contents = f.read() # Read the entire file into memory
        return file_contents # Return the texts as a string



def main():

    # sys.argv is a list of command-line arguments
    # Example: if we run "python3 main.py books/frankenstein.txt"
    # sys.argv[0] will be "main.py"
    # sys.argv[1] will be "books/frankenstein.txt"

    # We expect exactly one extra argument: the path the book 
    # So sys.argv should have a length of 2 (program name + file path)   
    if len(sys.argv) != 2:
        # If the user did not give exactly one argument, tell them how to use the program
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) # Exit the program with an error code(1 means "error")

    # Use sys.argv for bookpath
    book_path = sys.argv[1]


    # Read the book's contents from the file
    text = get_book_text(book_path)  
    
    # Count the total number of words in the text
    total_words = word_count(text) 
    
    # Count how many times each character appears in the text
    char_count_map = char_counts(text)

    # Sort the characters by frequency (most common first)
    sorted_char_list = sort_chars(char_count_map)   


    # Display formatted output
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("---------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")

    # Loop through each dictionary in the sorted character list
    # Print only alphabetical characters (ignore spaces, punctuation, numbers, etc.) 
    for char_dict in sorted_char_list:
        char = char_dict["char"] # The character itself
        count = char_dict["num"] # The number of times it appears
        if char.isalpha():
            print(f"{char}: {count}")
    
    # End of program output
    print("============= END ===============")

# Run the program
main()



