def reverse_every_second_word(text):
    words = text.split()  
    for i in range(1, len(words), 2):  
        words[i] = words[i][::-1]
    return ' '.join(words) 

def shift_letter(letter, shift_amount):
    if 'a' <= letter <= 'z':  
        return chr((ord(letter) - ord('a') + shift_amount) % 26 + ord('a'))
    elif 'A' <= letter <= 'Z': 
        return chr((ord(letter) - ord('A') + shift_amount) % 26 + ord('A'))
    else:
        return letter  

def encrypt(text, shift_amount):
    reversed_text = reverse_every_second_word(text)  
    encrypted_text = ''.join(shift_letter(char, shift_amount) for char in reversed_text)
    return encrypted_text

# Example usage
if __name__ == "__main__":
    original_text = "Hello World This is an Example"
    shift_amount = 3
    encrypted_text = encrypt(original_text, shift_amount)
    print("Original Text:", original_text)
    print("Encrypted Text:", encrypted_text)
