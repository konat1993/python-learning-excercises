# Task 9: Write a function that takes a text and returns every second character from the text.

def get_every_second_char(text: str) -> str:
    print("Every second char from: ", text)
    return str(text)[::2]


print(get_every_second_char("G|e|t| |m|e| |e|v|e|r|y| |s|e|c|o|n|d| |c|h|a|r"))
