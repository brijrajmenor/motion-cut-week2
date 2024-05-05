def count_words(text):
    # Split the text into words using whitespace as delimiter
    words = text.split()

    # Return the count of words
    return len(words)


def main():
    print("Welcome to Word Counter!")
    print("Please enter a sentence or paragraph:")

    # Prompt the user for input
    user_input = input()

    # Check if input is empty
    if not user_input.strip():
        print("Error: Input is empty. Please enter some text.")
        return

    # Call the function to count words
    word_count = count_words(user_input)

    # Display the word count
    print("Word count:", word_count)


if __name__ == "__main__":
    main()
