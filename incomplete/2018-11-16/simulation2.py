# SIMULATION FILE
# https://fivethirtyeight.com/features/the-riddler-just-had-to-go-and-reinvent-beer-pong/

import time
import numpy as np
np.random.seed(12345)


def throw(n):
    '''Returns number of throws to fill N cups, as well as number of rounds.
    One round is completed when every cup has at least one ball.
    One game is completed when every numbered cup has a same-number ball in it.
    '''
    cup_set = set()
    round_set = set()
    ball_count = 0
    round_count = 1 # allow for ending the game on an incomplete round

    while len(cup_set) < n:
        ball_count += 1
        ball_num = np.random.randint(n)
        cup_num = np.random.randint(n)

        # "Reset" round once all the cups have at least one ball
        round_set.add(cup_num)
        if len(round_set) == n:
            round_count += 1
            round_set = set()

        if ball_num == cup_num:
            cup_set.add(ball_num)

    return ball_count, round_count


def main():
    '''Main control structure for simulation.'''
    NUM_SIMULATIONS = 10000
    MAX_CUPS = 30

    # setup data file with column names
    with open('data2.csv', 'w') as f:
        f.write('NUM_CUPS,NUM_ROUNDS,NUM_BALLS,TIME_TAKEN\n')

    for i in range(1, MAX_CUPS + 1):

        # Results = mean number of balls thrown to finish game
        start = time.time()
        results = np.array(list(map(lambda x: throw(i), range(NUM_SIMULATIONS))))
        balls = np.mean(results[:, 0])
        rounds = np.mean(results[:, 1])
        duration = time.time() - start

        # print results
        print(f'With {i} cups and across {NUM_SIMULATIONS} simulations:')
        print(f'Mean rounds: {rounds}')
        print(f'Mean balls thrown: {balls}')
        print(f'Time taken: {duration}s')
        print('')

        # write results to file
        with open('data2.csv', 'a') as f:
            f.write(f'{i},{rounds},{balls},{duration}\n')

if __name__ == '__main__':
    main()
