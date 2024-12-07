import string

def caesar_encrypt(message, key):
    shift = key % 26
    # Shift the alphabet and ensure the lengths are the same
    cipher = str.maketrans(string.ascii_lowercase, 
                           string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    encrypted_message = message.lower().translate(cipher)
    return encrypted_message

def caesar_decrypt(encrypted_message, key):
    shift = key % 26
    # Reverse the shift for decryption
    cipher = str.maketrans(string.ascii_lowercase, 
                           string.ascii_lowercase[-shift:] + string.ascii_lowercase[:-shift])
    message = encrypted_message.translate(cipher)
    return message

# Test the functions
message = "How are you today?"
key = 3

encrypted_message = caesar_encrypt(message, key)
print(f"Encrypted message is: {encrypted_message}")

decrypted_message = caesar_decrypt(encrypted_message, key)
print(f"Decrypted message is: {decrypted_message}")
