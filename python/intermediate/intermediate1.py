#Write a function that will take in the a word and add a space to the string if its length is odd, and if it is even return it. (pass the word hi or odd into the function written) 
def add_space(word):
    if len(word) % 2 == 0:
        return word
    else:
        return word + " "

# Example usage
word1 = "hi"
word2 = "odd"
print(add_space(word1)) # Output: "hi "
print(add_space(word2)) # Output: "odd"
