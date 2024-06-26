#program to encrpt and decrpyt a text using caesar cipher algorithm
#allowing user to input a message and shift value for encrption and decryption
#written by BLESSING IFEOLUWA OMOGBEHIN
def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                offset = ord('a')
            elif char.isupper():
                offset = ord('A')
            else:
                continue
            shifted = (ord(char) - offset + shift * mode) % 26 + offset
            result += chr(shifted)
        else:
            result += char
    return result
#encryption process declaration
def encryption(text, shift):
    return caesar_cipher(text, shift, 1)
#decryption process declaration
def decryption(text, shift):
    return caesar_cipher(text, shift, -1)

def main():
    while True:
        choice = input("Enter 'encrypt' for encryption, 'decrypt' for decryption, 'E' to exit: ").lower()
        if choice == 'encrypt':
            text = input("Enter the text to encrypt: ") #user to input a message
            shift = int(input("Enter the shift value: ")) #user to input a shift value to encrypt message
            encrypted_text = encryption(text, shift)
            print("Encrypted text:", encrypted_text)
        elif choice == 'decrypt':
            text = input("Enter the text to decrypt: ") #user to input the message to decrypt
            shift = int(input("Enter the shift value: ")) #user to input the shift value to decrypt message
            decrypted_text = decryption(text, shift)
            print("Decrypted text:", decrypted_text)
        elif choice == 'E':
            print("Exiting...")
            break
        else:
            print("You have selected a wrong option. Please enter 'Encrypt', 'decrypt', or 'E'.")

if __name__ == "__main__":
    main()

"""e"""
