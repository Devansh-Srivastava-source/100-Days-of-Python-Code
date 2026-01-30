alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text,shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter != " ":
            shifted_index = (alphabet.index(letter) + shift_amount)%26
            # Here %26 is done to get values between 1 and 26
            cipher_text += alphabet[shifted_index]
        else:
            cipher_text += " "
    print(f"Encrypted message: {cipher_text}")

def decrypt(encrypted_text, shift_amount):
    back_text = ""
    for letter in encrypted_text:
        if letter != " ":
            shifted_index = (alphabet.index(letter) - shift_amount)%26
            back_text += alphabet[shifted_index]
        else:
            back_text += letter
    print("Decrypted text: "+back_text)

if direction == "encode":
    encrypt(text,shift)
elif direction == "decode":
    decrypt(text,shift)
else:
    print("invalid choice")