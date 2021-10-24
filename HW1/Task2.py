def encrypt_cezar_letter(letter, shift):
    letter_index = (ord(letter) - ord('A') + shift) % 26
    return chr(letter_index + ord('A'))


def encrypt_vigenere(message, key):
    key: str
    result_letters = []
    for i, char in enumerate(message):
        shift_by = ord(key[i % len(key)]) - ord('A')
        result_letters.append(encrypt_cezar_letter(char, shift_by))
    ciphertext = ''.join(result_letters)
    return ciphertext


def get_letters_count_dict(text):
    counts_map = {}
    for char in text:
        prev_count = counts_map.get(char)
        if prev_count is None:
            prev_count = 0
        counts_map[char] = prev_count + 1
    return counts_map


def get_index_of_coincidence(text):
    counts_map = get_letters_count_dict(text)
    result = 0
    for val in counts_map.values():
        result += val * (val - 1)
    result /= len(text) * (len(text) - 1)
    return result


plaintext = 'FRIENDSMAKETHEWORSTENEMIES'

ciphertext = encrypt_vigenere(plaintext, 'LIST')

ciphertext_index_of_coincidence = get_index_of_coincidence(ciphertext)
plaintext_index_of_coincidence = get_index_of_coincidence(plaintext)

print("Ciphertext is: " + ciphertext)
print("Index of coincidence of the plaintext is: %f" % plaintext_index_of_coincidence)
print("Index of coincidence of the ciphertext is: %f" % ciphertext_index_of_coincidence)
