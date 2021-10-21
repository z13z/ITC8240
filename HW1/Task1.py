def encrypt_cezar_letter(letter, shift):
    letter_index = (ord(letter) - ord('A') + shift) % 26
    return chr(letter_index + ord('A'))


def encrypt_cezar(message, shift):
    return ''.join([encrypt_cezar_letter(message_char, shift) for message_char in message])


def encrypt_shuffle(text, indexes):
    text: str
    if len(text) % len(indexes) != 0:
        print("length of message must be divided by shuffle array length without reminder")
        exit(1)
    cur_text = list(text)
    original = list(cur_text)
    for i in range(len(text)):
        cur_text[i] = original[indexes[i % len(indexes)] + int(i / len(indexes)) * len(indexes) - 1]
    return ''.join(cur_text)


S1 = encrypt_cezar('BLOCKCHAIN', 9)

P1 = encrypt_shuffle(S1, [5, 1, 3, 2, 4])

S2 = encrypt_cezar(P1, 19)

P2 = encrypt_shuffle(S2, [3, 1, 4, 2, 5])

print("Ciphertext is %s" % P2)
