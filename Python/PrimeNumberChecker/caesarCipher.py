alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    new_text = ""
    if direction == "encode":
        
        for char in range(len(text)):
            index = alphabet.index(text[char]) + shift

            while index > 25:
                index = index - 26

            else:
                new_text = new_text + alphabet[index]

        return new_text
    
    elif direction == "decode":
        for char in range(len(text)):
            
            index = alphabet.index(text[char]) - shift
            while index < -25:
                index = index + 26

            new_text = new_text + alphabet[index]

        return new_text

    return new_text

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, type 'quit' to end the game\n")
    
    if direction == "quit":
        print("Thank you")
        break

    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesarText = caesar(text, shift, direction)
        print(caesarText)


