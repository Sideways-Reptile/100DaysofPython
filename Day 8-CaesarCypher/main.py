from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
print(logo)


def ceaser(start_text, shift_amount, cypher_Direction):
    output = ""
    if cypher_Direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            letter_Index = alphabet.index(char)
            new_Index = letter_Index + shift_amount
            if new_Index >= 26:
                new_Index %= 26
            output += alphabet[new_Index]
        else:
            output += char
    print(f"The {cypher_Direction}d message is {output}")


# Program starts here:
start_Again = True
while start_Again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(start_text=text, shift_amount=shift, cypher_Direction=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no':\n")
    if restart == "no":
        print("Goodbye.")
        start_Again = False


