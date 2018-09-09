# Riddler - Sep 7, 2018
# https://fivethirtyeight.com/features/id-like-to-use-my-riddler-lifeline/

# 100 unique cards in a set
# cards are sold in packs of 10 for $1, no dupes in each pack
# you get $10 a week
# how long until you get all 100 cards?

import random
import time

def buy_pack(num_cards, card_set):
    # select 10 random cards without duplication
    pack_cards = random.sample([x for x in range(1, num_cards + 1)], k = 10)

    # remove cards in pack from set once collected
    for card in pack_cards:
        if card in card_set:
            card_set.remove(card)

def collect_cards(num_cards):
    # initialize 100 unique cards using a set
    cards_left = set([x for x in range(1, num_cards + 1)])

    # loop until 0 cards are left
    num_packs = 0

    while cards_left:
        buy_pack(num_cards, cards_left)
        num_packs += 1

    return num_packs

# loop over n card runs
num_simulations = 10000
num_cards = 100

# pre-allocate list
card_runs = [None] * num_simulations

for i in range(num_simulations):
   card_runs[i] = collect_cards(num_cards)

# get mean number of packs needed to collect all cards
mean_packs = sum(card_runs) / num_simulations

num_weeks = mean_packs/10

print(f"After {num_simulations} simulations, all {num_cards} cards were collected in {mean_packs} packs.")
print(f"That's {num_weeks} weeks!")
print(f"Time taken: {time.perf_counter()} s")
