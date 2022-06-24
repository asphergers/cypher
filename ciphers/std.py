import random
from datetime import date, datetime, timezone;
import time

acceptable_chars = list(range(32, 127)) + list(range(293, 347)) + list(range(913, 952));

characters_in_order = [chr(x) for x in acceptable_chars];

key = list();

def standard_seed():
    todays_date = str(date.today());
    li = list(todays_date.split("-"));
    test_list = [int(i) for i in li];

    dt = datetime(test_list[0], test_list[1], test_list[2]);

    timestamp = dt.replace(tzinfo=timezone.utc).timestamp();
    random.seed(timestamp);
    standard = timestamp + (random.randint(10, 1000000000) * random.random());
    
    return standard;

def cipher(message: int, input=None):
    if not input:
        input = standard_seed();
    seed = input;

    if isinstance(seed, str):
        new = int();
        for letter in input:
            new += chr(letter);
        seed = new;
    seed = int(seed);
    
    random.seed(seed);
    shuffled_list = [chr(x) for x in acceptable_chars];
    random.shuffle(shuffled_list);

    result = str();
    for letter in message:
        result += shuffled_list[characters_in_order.index(letter)];

    return result;

def decipher(message: str, input=None):
    if not input:
        input = standard_seed();
    seed = input;

    if isinstance(seed, str):
        new = str();
        for letter in seed:
            new += chr(letter);
        seed = new;
    seed = int(seed);

    random.seed(seed);
    shuffled_list = [chr(x) for x in acceptable_chars];
    random.shuffle(shuffled_list);

    result = str();
    for letter in message:
        result += characters_in_order[shuffled_list.index(letter)];

    return result;
