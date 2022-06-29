import random
from datetime import date, datetime, timezone;

def standard_seed():
    todays_date = str(date.today())
    li = list(todays_date.split("-"))
    test_list = [int(i) for i in li]

    dt = datetime(test_list[0], test_list[1], test_list[2])
    timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
    standard = random.seed(timestamp)
    standard = timestamp + (random.randint(10, 10000000000) * random.random())

    return standard

random.seed(10);

def cipher(message: str, input=None):
    if (not input) or not isinstance(input, int):
        seed = standard_seed();
    else:
        seed = input
    random.seed(seed)
    counter = 0;
    output = list();
    for letter in message:
        newChar = ord(letter) + random.randint(127, 300);
        output.append(newChar);
        counter += 1;
        random.seed(seed + counter);
    
    final = ''.join([chr(i) for i in output]);
    return final

def decipher(message: str, input=None):
    if (not input) or (not isinstance(input, int)) or (isinstance(input, float)):
        seed = standard_seed();
    else:
        seed = input;
    random.seed(seed);
    counter = 0;
    output = list();
    for letter in message:
        newChar = ord(letter) - random.randint(127, 300);
        output.append(newChar);
        counter += 1;
        random.seed(seed + counter);

    final = ''.join([chr(u) for u in output]);
    return final;

