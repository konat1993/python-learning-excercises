# Task 8: Count the number of occurrences of each word in the sentence.
import string

# sentence = input("Write a sentence: ").replace(",", "").replace(".", "")
sentence = input("Write a sentence: ").translate(str.maketrans("", "", ",."))

words = sentence.split(" ")

words_dict = {}

for word in words:
    if words_dict.get(word) == None:
        words_dict[word] = 1

    else:
        words_dict[word] = words_dict[word] + 1


for word, count in words_dict.items():
    print(word, ": ", count)
