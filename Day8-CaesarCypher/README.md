**NOTES**

<u>Caser Cypher</u>
\
This lesson taught me about Lists, how to create them and reference 
values in them. 

I did well creating the functions that processed Encoding/Decoding,
but the Instructor showed a much cleaner way to manage the code. 
That code is currently in main.py, and my code is below:

    def encrypt(plain_Text, shift_amount):
       cypher_Text = ""
       for letter in plain_Text:
         plain_Index = alphabet.index(letter)
         cypher_Index = plain_Index + shift_amount
         if cypher_Index >= 26:
           cypher_Index -= 26
         cypher_Letter = alphabet[cypher_Index]
         cypher_Text += cypher_Letter
       print(f"The encoded message is {cypher_Text}")
    
    def decrypt(cypher_Text, shift_amount):
        #Dont need to worry about end of range: 
        #negative position is the same and starting from end
       plain_Text = ""
       for letter in cypher_Text:
         cypher_Index = alphabet.index(letter)     
         plain_Index = cypher_Index - shift_amount
         plain_Letter = alphabet[plain_Index]
         plain_Text += plain_Letter
       print(f"the decoded message is {plain_Text}")
    
     if direction == "encode":
       encrypt(text, shift)
     else:
       decrypt(text, shift)