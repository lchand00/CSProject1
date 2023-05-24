import collections

# Read ciphertext
with open('ciphertext.txt', 'r') as file:
    cipher_text = file.read()

def frequency_analysis(cipher_text):
    frequency = collections.defaultdict(int)

    for char in cipher_text:
        if char.isalpha():
            frequency[char] += 1

    return frequency

# Compute frequency analysis
char_frequency = frequency_analysis(cipher_text)

# Display frequency analysis
#for char, freq in sorted(char_frequency.items(), key=lambda x: x[1], reverse=True):
#    print(char, int(freq))
def sort_by_frequency(item):
    return item[1]

sorted_items = sorted(char_frequency.items(), key=sort_by_frequency, reverse=True)
for char, freq in sorted_items:
    print(char, int(freq))

def decrypt_ciphertext(cipher_text, key):
    decrypted_text = ""

    for char in cipher_text:
        if char.isalpha() and char in key:
            decrypted_text += key[char]
        else:
            decrypted_text += char

    return decrypted_text
#ETAOINSHRDLCUMWFGYPBVKJXQZ
key = {
    'S':'E', 'G':'T','K':'A','U':'O','C':'I','E':'N','Q':'S','H':'R','B':'H','Z':'D','A':'L','I':'C','N':'U','L':'M','X':'W','P':'F','R':'G','O':'Y','W':'P','V':'B','F':'V','M':'K','D':'J','T':'X','J':'Q'
}

decrypted_text = decrypt_ciphertext(cipher_text, key)
print(decrypted_text)
