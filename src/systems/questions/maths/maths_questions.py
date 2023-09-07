import random
from operator import add, sub, mul, truediv


def create_maths_question():
    operators = [add, sub, mul, truediv]
    op = random.choice(operators)
    if op == add or op == sub:
        num_1 = random.randint(1, 500)
        num_2 = random.randint(1, 500)
    elif op == mul or op == truediv:
        num_1 = random.randint(2, 12)
        num_2 = random.randint(2, 12)
    max_num = max([num_1, num_2])
    min_num = min([num_1, num_2])
    if op == truediv and max_num % min_num != 0:
        op = mul


    i = operators.index(op)
    symbols = ['+', '-', 'x', '/']
    text = f"What is {max_num} {symbols[i]} {min_num}?"
    answer = op(max_num, min_num)

    return {
        'text': text,
        'answer': answer 
    }




def create_rounding_question():
    num = random.randint(1, 100)/10
    text = f'What is {num} rounded to the nearest integer?'
    answer = round(num)

    return {
        'text': text,
        'answer': answer 
    }

def choose_maths_question():
    questions_list = [
        create_maths_question,
        create_rounding_question
    ]

    chosen_question = random.choice(questions_list)

    return chosen_question()


