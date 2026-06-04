# This will contain code to remove all the punctuations before the tokenization.
# For this I am using the string module.
# I am taking the input from terminal only and terminal does not take the multi line input so paste the example text in one line only.
import string
import sys

print("Enter/Paste your text. Press Ctrl+D (Mac/Linux) or Ctrl+Z -> Enter (Windows) to save:")
user_input = sys.stdin.read()

clean_text = user_input.translate(str.maketrans(string.punctuation, " " * len(string.punctuation)))
tokens = clean_text.split() # This will split whole text into separate words and arrange in list.

print(tokens)
print(f"The total number of tokens are {len(tokens)}")