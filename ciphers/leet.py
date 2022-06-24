leet_dict = {"A": "Д", "B": "ß", "C": "<", "D": "Ð",
        "E": "3", "F": "∫", "G": "9", "H": "н", "I": "!",
        "J": "√", "K": "𝒦", "L": "1", "M": "м", "N": "π",
        "O": "Ø", "P": "P", "Q": "9", "R": "®", "S": "$",
        "T": "7", "U": "μ", "V": "V", "W": "Ш", "X": "Ж",
        "Y": "¥", "Z": "5"}

leet_dict_decode = dict([(y, x) for (x, y) in leet_dict.items()]);

def cipher(message: str, input=None):
    new = str();
    for letter in message.upper():
        if letter in leet_dict:
            new += leet_dict[letter]
        else:
            new += letter;
    return new;

def decipher(message: str, input=None):
    new = str();
    for letter in message.upper():
        if letter in leet_dict_decode:
            new += leet_dict_decode[letter];
        else:
            new += letter;
    return new;
