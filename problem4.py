"""
Problem 4: File Word Counter
Process text files and perform various analyses.
"""
import string 
def create_sample_file(filename="sample.txt"): 
    """
    Create a sample text file for testing.

    Args:
        filename (str): Name of the file to create
    """
    content = """Python is a powerful programming language.
It is widely used in web development, data science, and automation.
Python's simple syntax makes it great for beginners.
Many companies use Python for their projects."""

    with open(filename, 'w') as f:
        f.write(content)
    print(f"Created {filename}")


def count_words(filename): 
    with open(filename, 'r') as f:
        text = f.read()
    words = text.split()
    return len(words)
    """
    Count total words in the file.

    Args:
        filename (str): Name of the file to analyze

    Returns:
        int: Total number of words
    """
    # TODO: Open file and count words
    # Hint: Use split() to separate words
    pass


def count_lines(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return len(lines)
    """
    Count total lines in the file.

    Args:
        filename (str): Name of the file to analyze

    Returns:
        int: Total number of lines
    """
    # TODO: Open file and count lines
    pass


def count_characters(filename, include_spaces=True):
    with open(filename, 'r') as f:
        text = f.read()
    if not include_spaces:
        text = text.replace(" ", "")
    return len(text)
    """
    Count characters in the file.

    Args:
        filename (str): Name of the file to analyze
        include_spaces (bool): Whether to include spaces in count

    Returns:
        int: Total number of characters
    """
    # TODO: Open file and count characters
    # If include_spaces is False, don't count spaces
    pass


def find_longest_word(filename):
    with open(filename, 'r') as f:
        text = f.read()
    # Supprime la ponctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    if not words:
        return None
    return max(words, key=len)
    """
    Find and return the longest word in the file.

    Args:
        filename (str): Name of the file to analyze

    Returns:
        str: The longest word found
    """
    # TODO: Find the longest word
    # Hint: You might need to remove punctuation
    pass


def word_frequency(filename):
    frequency = {}
    with open(filename, 'r') as f:
        text = f.read().lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency
    """
    Return a dictionary of word frequencies.
    Convert words to lowercase and remove punctuation.

    Args:
        filename (str): Name of the file to analyze

    Returns:
        dict: Dictionary with words as keys and frequencies as values
    """
    

    # TODO: Open file
    # TODO: Read all words
    # TODO: Convert to lowercase
    # TODO: Remove punctuation (use string.punctuation)
    # TODO: Count frequency of each word

    return frequency


def analyze_file(filename):
    """
    Perform complete analysis of the file.

    Args:
        filename (str): Name of the file to analyze
    """
    print(f"\nAnalyzing: {filename}")
    print("-" * 40)

    try:
        # Display all analyses
        print(f"Lines: {count_lines(filename)}")
        print(f"Words: {count_words(filename)}")
        print(f"Characters (with spaces): {count_characters(filename, True)}")
        print(f"Characters (without spaces): {count_characters(filename, False)}")
        print(f"Longest word: {find_longest_word(filename)}")

        # Display top 5 most common words
        print("\nTop 5 most common words:")
        freq = word_frequency(filename)

        # Sort by frequency and get top 5
        top_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]
        for word, count in top_words:
            print(f"  '{word}': {count} times")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Main function to run the file analyzer."""
    # Create sample file
    create_sample_file()

    # Analyze the sample file
    analyze_file("sample.txt")

    # Allow user to analyze their own file
    print("\n" + "=" * 40)
    user_file = input("Enter a filename to analyze (or press Enter to skip): ").strip()
    if user_file:
        analyze_file(user_file)


if __name__ == "__main__":
    main()