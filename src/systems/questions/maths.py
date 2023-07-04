import random
from operator import add, sub, mul, truediv


def create_maths_question():
    num_1 = random.randint(1, 12)
    num_2 = random.randint(1, 12)
    max_num = max([num_1, num_2])
    min_num = min([num_1, num_2])
    ops = [add, sub, mul, truediv] if max_num % min_num == 0 else [add, sub, mul]
    op = random.choice(ops)

    index = ops.index(op)
    symbols = ['+', '-', 'x', '/']
    text = f"What is {max_num} {symbols[index]} {min_num}?"
    answer = op(max_num, min_num)

    return {
        'text': text,
        'answer': answer
    }

def create_fraction_question():
    pass


def create_rounding_question():
    num = random.randint(1, 100)/10
    text = f'What is {num} rounded to the nearest integer?'
    answer = round(num)

    return {
        'text': text,
        'answer': answer
    }

def choose_maths_question():
    pass
