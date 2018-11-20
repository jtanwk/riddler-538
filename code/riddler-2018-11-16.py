# https://fivethirtyeight.com/features/the-riddler-just-had-to-go-and-reinvent-beer-pong/

import random


def throw(cups, N):
    '''Appends randomly selected ball number to randomly selected cups.
    Returns resulting cup.'''
    ball_num = random.choice(range(N))
    cup_num = random.choice(range(N))
    cups[cup_num].append(ball_num)
    return cups


def throw_phase(cups, N):
    '''Throws balls at cups repeatedly until every cup has >0 balls.
    Returns cups and the number of balls thrown.'''

    num_thrown = 0

    # Returns true until all cups are filled, then false.
    while list(filter(lambda x: not x, cups.values())):
        cups = throw(cups, N)
        num_thrown += 1

    return cups, num_thrown


def prune(cups):
    '''Removes all balls whose number does not match the cup number.'''

    def check_cup(arg):
        cup_num, ball_nums = arg[0], arg[1]
        return list(filter(lambda x: x == cup_num, ball_nums))

    cups = dict(enumerate(list(map(check_cup, cups.items()))))

    return cups


def main():

    # key parameters
    N = 10
    NUM_SIMULATIONS = 10000
    rounds_played = []
    balls_thrown = []

    for i in range(NUM_SIMULATIONS):
        num_rounds = 0
        num_balls = 0

        # initialize cup dictionary
        cups = {x:[] for x in range(N)}

        # loop over throwing and pruning phases until all cups are filled
        while list(filter(lambda x: not x, cups.values())):
            cups, num_thrown = throw_phase(cups, N)
            cups = prune(cups)
            num_rounds += 1
            num_balls += num_thrown

        rounds_played.append(num_rounds)
        balls_thrown.append(num_balls)

    # print results
    print(f'With {N} cups and across {NUM_SIMULATIONS} simulations...')
    print(f'Mean rounds played:', sum(rounds_played) / NUM_SIMULATIONS)
    print(f'Mean balls thrown:', sum(balls_thrown) / NUM_SIMULATIONS)
    print('')


if __name__ == '__main__':
    main()
