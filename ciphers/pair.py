import random
from datetime import *
import time

def standard_seed():
    todays_date = str(date.today())
    li = list(todays_date.split("-"))
    test_list = [int(i) for i in li]

    dt = datetime(test_list[0], test_list[1], test_list[2])
    timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
    standard = random.seed(timestamp)
    standard = timestamp + (random.randint(10, 10000000000) * random.random())

    return standard

random.seed(standard_seed());

letters = list("""abcdefghijklmnopqrstuvwxyz !.,/@#$%^&*()_+=-?0123456789:;"'[]{}""");
chars = list(range(13314 ,17283));
random.shuffle(chars);

def makeCombo(seed):
    if isinstance(seed, int) or isinstance(seed, float):
        seed = int(seed);
    else:
        seed = int(standard_seed());

    combos = [];
    index = 0;
    random.seed(seed);
    chrs = [x for x in chars]
    random.shuffle(chrs);
    for i in range(len(letters)):
        for j in range(len(letters)):
            combos.append([f"{letters[i]}{letters[j]}", chr(chrs[index])]);
            index += 1;
    return combos;


def cipher(message: str, input=None):
    if not input:
        input = standard_seed();
    key = int(input);

    if isinstance(key, str):
        new = 0;
        for letter in key:
            new += chr(letter);
        key = new;

    combos = makeCombo(key);

    if (len(message)/2) % 2 != 0:
        message += " ";
    newMessage = [];
    j = 0
    for i in range(int(len(message)/2)):
        newMessage.append(f"{message[j]}{message[j+1]}");
        j += 2;

    result = "";

    for i in range(len(newMessage)):
        for j in range(len(combos)):
            if combos[j][0] == newMessage[i]:
                result += str(combos[j][1]);
                break;

    return result;


def decipher(message: str, input=None):
    if not input:
        input = standard_seed();
    key = int(input);

    if isinstance(key, str):    
        new = 0;
        for letter in key:
            new += chr(letter);
        key = new;

    combos = makeCombo(key);
    result = message;
    deciphered = ""

    for i in range(len(result)):
        for j in range(len(combos)):
            if result[i] == combos[j][1]:
                deciphered += combos[j][0];

    return deciphered;


