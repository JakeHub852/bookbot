import sys
from stats import get_num_words, get_num_chars, sorted_chars

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
  
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    sorted_list = sorted_chars(num_chars)

 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()