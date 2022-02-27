# **<u>Error Handling and Exceptions</u>**

this lesson focuses on how to test for and catch error exceptions
in our code. Let's say our code runs and produces and error. What can be done
about this is to write a Try:, Except: block of code to tell python
the code to try and run and if an error occurs, we can specify what the code
ought to do when that error is processed, instead of outright crashing
and terminating the program. The code below is our Phonetic Alphabet made
previously, edited to show this method. What if a User enters Numbers or 
a value that is not in the Dictionary? Or a value outside of scope/range?

    word = input("Enter a word: ").upper()
    output_list = [phonetic_dict[letter] for letter in word]
    print(output_list)

The above code will have an error that we can account for:

    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError: #User entered a Number or Symbol
        print("Only use letters please.")
    else:
        print(output_list)

We can make this line of code into a function to allow it to keep running should the 
error proc. When errors are found, the program can respond but will
ultimately end unless told to restart the program.

<h2> JSON Information </h2>
JavaScript Object Notation
An increasingly popular data format that makes referencing data within and
sending the data across the internet much easier. JSON works similarly 
to Nested Directories in Python with Key:Value pairs.JSON is built in to Python.

- json.dump(new_data, log, indent=4) - To Write JSON data to a file. Needs to "w" tag
- data = json.load(log) # - .load is to Read from a JSON file. Need to add the "r" tag
- To Upload (add) data to a JSON file. Need to add "r" tag to read the data, then the "w" tag to write the data:
 
    
    with open("data.json", "r") as log:
        data = json.load(log) - 
        data.update(new_data)
    
    with open("data.json", "w") as log:
        json.dump(data, log, indent=4)

Look at code from today to study JSON and Try/Except/Else/Finally block

*Learned some new things today that made me feel like I wasn't doing enough
of this day by myself but remembered I didn't know any of it and was able to do 
a lot that I did know by myself. I only used the video to help solidify our confirm 
my code, so I feel like I'm learning have been enjoying this.*

