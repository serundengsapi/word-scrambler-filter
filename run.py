import random
import pyfiglet

# Expanded character substitutions
substitutions = {
    'a': ['4', '@', 'a', '/\\'],
    'e': ['3', '€', 'e'],
    'i': ['1', '!', '|', 'i'],
    'o': ['0', 'o', '°'],
    'u': ['v', 'u', 'µ'],
    's': ['5', '$', 's', '§'],
    'b': ['8', 'b', 'ß'],
    'l': ['1', 'l', '|'],
    't': ['7', 't', '+'],
    'r': ['r', '2'],
    'n': ['n', 'И'],
    'k': ['k', '|<', '|{'],
    'c': ['c', '(', '<'],
    'd': ['d', 'cl'],
}

# Function to replace characters in the word with substitutions
def substitute_chars(word):
    return ''.join(random.choice(substitutions.get(c, [c])) for c in word)

# Function to insert random spaces between letters
def randomize_spaces(word):
    spaced_word = ''.join(c + (' ' if random.random() > 0.7 else '') for c in word)
    return spaced_word.strip()

# Function to generate variations
def generate_variations(word, num_variations=5):
    variations = []
    for _ in range(num_variations):
        substituted_word = substitute_chars(word)
        spaced_word = randomize_spaces(substituted_word)
        variations.append(spaced_word)
    return variations

# Main function to get input from the user and generate variations
def main():
    # Display ASCII text using the Ogre font
    ascii_art = pyfiglet.figlet_format("ryujinx", font="ogre")
    print(ascii_art)
    
    # Display Instagram handle
    print("Word Scrambler Guard - Instagram : @abdan.vbs\n")

    # Get user input
    user_word = input("Enter the word you want to generate variations for: ")
    num_variations = int(input("How many variations do you want to generate? "))
    
    # Generate variations
    variations = generate_variations(user_word, num_variations)
    
    # Print the variations
    print("\nGenerated Variations:")
    for variation in variations:
        print(variation)

# Run the tool
if __name__ == "__main__":
    main()
