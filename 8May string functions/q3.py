given_str = "this is a sentence with duplicate words.this is a sentence without duplicate words."
words_list = given_str.split()
unique_words = list(set(words_list))

unique_str = ''.join(unique_words)
print(unique_str)