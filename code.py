import collections

# Read ciphertext
with open('ciphertext.txt', 'r') as file:
    cipher_text = file.read()

def frequency_analysis(cipher_text):
    frequency = collections.defaultdict(int)

    for char in cipher_text:
        frequency[char] += 1

    return frequency

# Compute frequency analysis
frequency = frequency_analysis(cipher_text)

# Display frequency analysis
for char, freq in sorted(frequency.items(), key=lambda x: x[1], reverse=True):
    print(char, int(freq))
