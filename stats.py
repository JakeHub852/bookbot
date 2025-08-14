def word_count(text): 
    # Counts the number of words in a given string
    words = text.split() # Split on whitespace into a list of words 
    return len(words) # Return total number of words

def char_counts(text):
    # Convert the entire string to lowercase so counts are case-insensitive
    lowercase = text.lower()
   
    # Initialize an empty dictionary to store character counts
    char_count_map = {} 

    # Loop through each character in the lowercase string
    for char in lowercase: 
        if char in char_count_map:
            # Increment the count if the character is already in the dictionary
            char_count_map[char] += 1 
        else: 
            # Add the character to the dictionary with an initial count of 1
            char_count_map[char] = 1 
    
    return char_count_map             

def sort_chars(char_count_map):

    # Create an empty list to store characters and their counts
    sorted_chars = []

    # Loop through each character in the dictionary
    # char_count_map[char] gives the number of times that character appears
    for char in char_count_map:
        # Add a dictionary with the character and its count to the list
        sorted_chars.append({"char": char, "num": char_count_map[char]})

    # Define a helper function to tell python how to sort
    # It returns the "num" value from each dictionary (the count)
    def sort_on(item):
        return item["num"]

    # Sort the list of dictionaries in place
    # reverse=True means largest count first (descending order)
    # key=sort_on tells Python to sort using the counts, not the characters
    sorted_chars.sort(reverse=True, key=sort_on)

    # Give back the sorted list
    return sorted_chars