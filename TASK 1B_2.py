def flames_game(name1, name2):
    # Remove common letters from both names
    name1_set = set(name1.lower())
    name2_set = set(name2.lower())
    common_letters = name1_set.intersection(name2_set)
    name1_filtered = ''.join(char for char in name1.lower() if char not in common_letters)
    name2_filtered = ''.join(char for char in name2.lower() if char not in common_letters)

    # Calculate the total length of remaining letters
    total_length = len(name1_filtered) + len(name2_filtered)

    # Define the FLAMES sequence
    flames_sequence = ['Friends', 'Love', 'Affection', 'Marriage', 'Enemies', 'Sibling']

    # Simulate the game
    while len(flames_sequence) > 1:
        index_to_remove = total_length % len(flames_sequence) - 1
        flames_sequence.pop(index_to_remove)

    return flames_sequence[0]

# Example usage
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")
result = flames_game(name1, name2)
print(f"The relationship between {name1} and {name2} is: {result}")
