from random import choice

print('Values: paper - p, rock - r, scissors - s')

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'

OPTIONS = [ROCK, SCISSORS, PAPER]
MAPPING = {
    ROCK: SCISSORS,
    SCISSORS: PAPER,
    PAPER: ROCK
}


def get_winner(user_val: str, generated_val: str):
    if user_val == generated_val:
        print('DRAW')
    elif MAPPING[user_val] == generated_val:
        print('YOU WIN')
    else:
        print('COMPUTER WIN')


def validate_input(user_val: str) -> bool:
    return user_val in OPTIONS


while True:
    user_val = input(f'Type one of the values(first letter): {", ".join(OPTIONS)}\n')

    if not validate_input(user_val):
        print('Wrong value. Try again')
        continue

    generated_val = choice(OPTIONS)
    print(f'Computers value is: { generated_val }')

    get_winner(user_val, generated_val)
