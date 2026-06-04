# This code contain code to tokenize the input string given by user.
# I am taking the input from terminal only and terminal does not take the multi line input so paste the example text in one line only.
import sys

print("Enter/Paste your text. Press Ctrl+D (Mac/Linux) or Ctrl+Z -> Enter (Windows) to save:")
user_input = sys.stdin.read()

tokens = user_input.split() # the split function will split the input string through whitespace, but will keep attach the punctuation marks in it.
print(tokens)
print(f"The total number of tokens are {len(tokens)}")

# to remove the punctuations before the tokenization we have to use string module and punctuation function.