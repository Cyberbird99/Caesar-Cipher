import string

def shift_alphabet(key, reverse=False):
    """Generates a shifted alphabet based on the key."""
    shift = key % 26
    if reverse:
        # For decryption, shift in the opposite direction
        shifted = string.ascii_lowercase[-shift:] + string.ascii_lowercase[:-shift]
    else:
        # For encryption, shift forward
        shifted = string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]
    return shifted

def caesar_encrypt(message, key):
    if not isinstance(message, str) or not isinstance(key, int):
        raise ValueError("Message must be a string and key must be an integer.")
    
    shifted = shift_alphabet(key)
    cipher = str.maketrans(string.ascii_lowercase + string.ascii_uppercase,
                           shifted + shifted.upper())
    return message.translate(cipher)

def caesar_decrypt(encrypted_message, key):
    if not isinstance(encrypted_message, str) or not isinstance(key, int):
        raise ValueError("Message must be a string and key must be an integer.")
    
    shifted = shift_alphabet(key, reverse=True)
    cipher = str.maketrans(string.ascii_lowercase + string.ascii_uppercase,
                           shifted + shifted.upper())
    return encrypted_message.translate(cipher)

# Test the functions
if __name__ == "__main__":
    message = "How are you today?"
    key = 3

    encrypted_message = caesar_encrypt(message, key)
    print(f"Encrypted message is: {encrypted_message}")

    decrypted_message = caesar_decrypt(encrypted_message, key)
    print(f"Decrypted message is: {decrypted_message}")
