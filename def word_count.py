def word_count(input_text):
    """
    Count the number of words in the given text.

    Parameters:
    input_text (str): The input text for word counting.

    Returns:
    int: The number of words in the input text.
    """
    words = input_text.split()
    return len(words)

def main():
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Please enter a sentence or paragraph: ")

    try:
        # Word counting logic
        count = word_count(user_input)

        # Output display
        print(f"\nWord Count: {count}")
    
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    # User-friendly interface
    print("Welcome to the Word Counter Program!")
    main()