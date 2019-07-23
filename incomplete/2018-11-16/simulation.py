# SIMULATION FILE
# https://fivethirtyeight.com/features/the-riddler-just-had-to-go-and-reinvent-beer-pong/

import time
import random
random.seed(12345)


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

    # setup
    MAX_CUPS = 100
    NUM_SIMULATIONS = 10000
    rounds_played = []
    balls_thrown = []

    # setup data file with column names
    with open('data.csv', 'w') as f:
        f.write('NUM_CUPS,NUM_SIMULATIONS,NUM_ROUNDS,NUM_BALLS,TIME_TAKEN\n')

    # simulate game for different numbers of cups and balls
    for i in range(1, MAX_CUPS + 1):

        start = time.time()
        num_cups = i

        for j in range(NUM_SIMULATIONS):
            num_rounds = 0
            num_balls = 0

            # initialize cup dictionary
            cups = {x:[] for x in range(num_cups)}

            # loop over throwing and pruning phases until all cups are filled
            while list(filter(lambda x: not x, cups.values())):
                cups, num_thrown = throw_phase(cups, num_cups)
                cups = prune(cups)
                num_rounds += 1
                num_balls += num_thrown

            rounds_played.append(num_rounds)
            balls_thrown.append(num_balls)

        stop = time.time()
        dur = stop - start

        # print results
        print(f'With {num_cups} cups and across {NUM_SIMULATIONS} simulations:')
        print(f'Mean rounds played:', sum(rounds_played) / NUM_SIMULATIONS)
        print(f'Mean balls thrown:', sum(balls_thrown) / NUM_SIMULATIONS)
        print(f'Time taken:', dur, 'seconds')
        print('')

        # write results to file
        with open('data.csv', 'a') as f:
            f.write(f'{num_cups},')
            f.write(f'{NUM_SIMULATIONS},')
            f.write(f'{sum(rounds_played) / NUM_SIMULATIONS},')
            f.write(f'{sum(balls_thrown) / NUM_SIMULATIONS},')
            f.write(f'{dur}\n')

        # reset counters
        rounds_played = []
        balls_thrown = []


if __name__ == '__main__':
    main()
