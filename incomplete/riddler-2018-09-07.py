# Riddler - Sep 7, 2018
# https://fivethirtyeight.com/features/id-like-to-use-my-riddler-lifeline/

import numpy.random
import time

# main parameters
num_simulations = 10000
card_runs = [None] * num_simulations    # stores num_packs for each run
total_cards = 100                       # number of cards to collect

for i in range(num_simulations):
    cards_collected = set()     # stores cards in current run
    num_packs = 0

    while len(cards_collected) < total_cards:
        pack_cards = numpy.random.randint(1, 101, size = 10)
        cards_collected.update(pack_cards)

        num_packs += 1

    card_runs[i] = num_packs

# get mean number of packs needed to collect all cards
mean_packs = sum(card_runs) / num_simulations
num_weeks = mean_packs/10

print(f"After {num_simulations} simulations, all {total_cards} cards were collected in {mean_packs} packs.")
print(f"That's {num_weeks} weeks!")
print(f"Time taken: {time.perf_counter()} s")
