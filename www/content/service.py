import random


NUMBERS = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
}

WORDS = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
}


def _pick_random_number(maximum=max(NUMBERS.keys())):
    return random.randint(1, maximum)


def generate_words(first_digit=_pick_random_number(),
                   second_digit=_pick_random_number()):
    return (NUMBERS[first_digit], NUMBERS[second_digit])


def _generate_sum(word_1, word_2):
    return WORDS[word_1]+WORDS[word_2]


def generate_answer(question):
    'quick and dirty way to get the numbers out'
    words = question.rstrip('?').split(' ')
    words = (words[2], words[4])
    return(_generate_sum(*words))
