import collections

def load_ciphertext(file_path):
    with open('ciphertext.txt', 'r') as file:
        ciphertext = file.read().replace('\n', '')
    return ciphertext

def load_dictionary(file_path):
    with open('dictionary.txt', 'r') as file:
        dictionary = set(file.read().split())
    return dictionary

def compute_frequency_order(ciphertext):
    letter_count = collections.Counter(ciphertext)
    frequency_order = ''.join(letter for letter, _ in letter_count.most_common())
    return frequency_order

def decrypt_ciphertext(ciphertext, key):
    decrypted_message = ""
    for char in ciphertext:
        if char.isalpha():
            decrypted_char = key[ord(char.upper()) - ord('A')]
            decrypted_message += decrypted_char.lower() if char.islower() else decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

def count_dictionary_words(message, dictionary):
    words = message.split()
    word_count = sum(1 for word in words if word.lower() in dictionary)
    return word_count

def guess_key(ciphertext, dictionary):
    standard_frequency_order = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    frequency_order = compute_frequency_order(ciphertext)

    best_key = standard_frequency_order
    best_word_count = 0

    for i in range(len(standard_frequency_order)):
        potential_key = standard_frequency_order[i:] + standard_frequency_order[:i]
        decrypted_message = decrypt_ciphertext(ciphertext, potential_key)
        word_count = count_dictionary_words(decrypted_message, dictionary)

        if word_count > best_word_count:
            best_word_count = word_count
            best_key = potential_key

    # Permute the guessed key until further permutations no longer improve word count
    while True:
        key_permutations = [best_key[i:] + best_key[:i] for i in range(len(best_key))]
        updated = False

        for permuted_key in key_permutations:
            decrypted_message = decrypt_ciphertext(ciphertext, permuted_key)
            word_count = count_dictionary_words(decrypted_message, dictionary)

            if word_count > best_word_count:
                best_word_count = word_count
                best_key = permuted_key
                updated = True

        if not updated:
            break

    return best_key, decrypt_ciphertext(ciphertext, best_key)

def main():
    ciphertext_file = 'ciphertext.txt'
    dictionary_file = 'dictionary.txt'

    # Load ciphertext and dictionary
    ciphertext = load_ciphertext(ciphertext_file)
    dictionary = load_dictionary(dictionary_file)

    # Compute frequency analysis
    frequency_order = compute_frequency_order(ciphertext)
    print("Frequency Analysis:", frequency_order)

    # Guess the key of the cipher
    guessed_key, decrypted_message = guess_key(ciphertext, dictionary)
    print("Guessed Key:", guessed_key)
    print("Decrypted Message:", decrypted_message)

if __name__ == '__main__':
    main()
