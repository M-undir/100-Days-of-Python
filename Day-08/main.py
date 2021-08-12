# Prime number checker

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

will_continue = True

while will_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def caesar(text_amount, shift_amount, cipher_direction):
        new_word = ""
        if cipher_direction == 'decode':
            shift_amount *= -1
        for letter in text_amount:
            if letter in alphabet:
                text_index = alphabet.index(letter)
                new_word += alphabet[text_index + shift_amount]
            else:
                new_word += letter
        print(f"Your {cipher_direction}d text is {new_word}")


    shift = shift % 26
    caesar(text, shift, direction)
    stay_or_go = input("Would you like to continue or stop? ").lower()
    if stay_or_go == "stop":
        will_continue = False
