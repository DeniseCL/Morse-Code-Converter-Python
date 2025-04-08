from morse_dict import morse_dict

print("=== Text to Morse Code Converter ===")
print("Type 'exit' to exit.\n")

while True:
    text = input("Enter the text to convert to Morse code: ").upper()

    if text.lower() == 'exit':
        print("Shutting down the converter. See you later!")
        break

    morse_converted = ''
    for character in text:
        if character in morse_dict:
            morse_converted += morse_dict[character] + ' '
        else:
            morse_converted += '[?]'

    print(f"Text in Morse Code: {morse_converted} \n")
