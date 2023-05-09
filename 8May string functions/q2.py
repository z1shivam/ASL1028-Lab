import string

punctuations = string.punctuation
given_str = "Hello, world! This is a sentence"

without_punctuations = given_str.translate(str.maketrans(",",punctuations))
print(without_punctuations)