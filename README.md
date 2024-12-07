# Caesar-Cipher
This code implements a Caesar cipher, a basic encryption technique that shifts letters in the alphabet by a fixed number of places (the "key"). 

Key Components:

Alphabet Shift Logic:

For encryption, the alphabet is shifted to the right (string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]).
For decryption, the alphabet is shifted to the left (string.ascii_lowercase[-shift:] + string.ascii_lowercase[:-shift]).
The % 26 ensures the key is within the valid range of 0-25 (the number of letters in the alphabet).

Character Mapping:

The str.maketrans method creates a mapping from the original alphabet to the shifted alphabet.

Translation:

The translate method replaces the characters in the input message based on the mapping.

Key Features of the Improved Code:

Handles Uppercase and Lowercase:

Both uppercase and lowercase letters are shifted correctly using string.ascii_uppercase.

Preserves Non-Alphabetic Characters:

Non-alphabetic characters like spaces, punctuation, and numbers are left unchanged.

Helper Function for Reusability:

The shift_alphabet function reduces redundancy and makes the code more modular.

Input Validation:

Ensures that invalid input types are handled gracefully with a descriptive error.

Improved Readability:

The code is well-structured with clear logic, making it easier to understand and maintain.
