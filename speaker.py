# a -> @
# A -> 4
# B, b -> 8
# E, e -> 3
# I, i -> !
# L, l -> 1
# O, o -> 0
# S, s -> 5
leet = {"a": "@",
    "A": "4",
    "B": "8",
    "b": "8",
    "E": "3",
    "e": "3",
    "I": "!",
    "i": "!",
    "L": "1",
    "l": "i",
    "O": "0",
    "o": "0",
    "S": "5",
    "s": "5"
}     
def convert(text: str) -> str:
    new_text = ""
    for index in text:
        if index == "A":
            new_text += leet["A"]
        elif index == "a":
            new_text += leet["a"]
        elif index == "E" or index == "e":
            new_text += leet["E"]
        elif index == "I" or index == "i":
            new_text += leet["I"]
        elif index == "L" or index == "l":
            new_text += leet["L"]
        elif index == "O" or index == "o":
            new_text += leet["O"]
        elif index == "S" or index == "s":
            new_text += leet["S"]     
        else:
            new_text += index
    return new_text 

a = "EIsa"
print(convert(a))
            