capitals_dict =  {
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne',
}

import random

states = list(capitals_dict.keys())
while True:
    state = random.choice(states)
    capital = capitals_dict[state]
    capital_guess = input('What is the capital of ' + state + '? ')

    if capital_guess == 'quit':
        break
    elif capital_guess == capital:
        print('Correct! Nice Job.')
    else:
        print('Incorrect. The capital of ' + state + ' is ' + capital + '.')

print('All Done')