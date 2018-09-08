# Riddler - Sep 7, 2018
# https://fivethirtyeight.com/features/id-like-to-use-my-riddler-lifeline/

# 100 unique cards in a set
# cards are sold in packs of 10 for $1, no dupes in each pack
# you get $10 a week
# how long until you get all 100 cards?

import random
import statistics

def buy_pack(card_list):
    # select 10 random cards without duplication
    pack_cards = random.sample([x for x in range(1, 101)], k = 10)

    # print(f"Bought: {pack_cards}")

    # change purchased card numbers to 0
    for card in pack_cards:
        if card in card_list:
            card_list[card - 1] = 0

def collect_cards():
    # initialize 100 unique cards
    cards_left = [x for x in range(1, 101)]
    num_packs = 0

    # loop until 0 cards are left
    while sum(cards_left) > 0:
        buy_pack(cards_left)
        num_packs += 1

    return num_packs

# loop over 10,000 card runs
num_simulations = 10000

card_runs = []

for i in range(num_simulations):
    card_runs.append(collect_cards())

mean_packs = statistics.mean(card_runs)
sd_packs = statistics.stdev(card_runs)

print(f"After {num_simulations} simulations, all 100 cards were collected in {mean_packs} +/- {sd_packs} packs.")

num_weeks = mean_packs/10

print(f"That's {num_weeks} weeks!")
