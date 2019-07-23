# Riddler - Aug 24, 2018
# https://fivethirtyeight.com/features/how-many-hoops-will-kids-jump-through-to-play-rock-paper-scissors/

# notes
# 1. board state can be fully represented by 2 numbers: L and R
# 2. calculate next position of L and R, and a rock-paper-scissors winner
# 3, depending on who wins, output new L and R positions
# 4. loop over steps 1-3 until win condition is satisfied
# win condition triggered when L/R are 1 step away from end points and win RPS

# # TODO: correct how win conditions are processed

# setup
import random
import time

num_hoops = 8.0
num_simulations = 1000
results = []

for i in range(num_simulations):

    left_pos = 0.0
    right_pos = num_hoops - 1.0
    num_seconds = 0.0

    while True:

        # advance players
        center = (right_pos + left_pos) / 2
        print("-----")
        print(f"(0) {left_pos}, {right_pos}")

        if center.is_integer():           # L and R landed on same square
            num_seconds += center - left_pos + 1
            left_pos = center
            right_pos = center
            print(f"(1) {left_pos}, {right_pos}")
        else:                                # L and R are on neighboring squares
            num_seconds += center - 0.5 - left_pos + 1
            left_pos = center - 0.5
            right_pos = center + 0.5
            print(f"(1) {left_pos}, {right_pos}")

        # rock-paper-scissors
        if random.randint(0,1):
            print("Left wins!")                 # L wins if 0, R wins if 1
            if left_pos == num_hoops - 2.0:     # L, R = 6, 7
                left_pos += 1
                right_pos = num_hoops - 1.0
                print(f"(2) {left_pos}, {right_pos}")
            elif left_pos == num_hoops - 1.0:   # L, R = 7, 7
                print(f"Left has won the game in {num_seconds}s!")
                results.append(num_seconds)
                break
            else:
                right_pos = num_hoops - 1.0
                print(f"(2) {left_pos}, {right_pos}")
        else:
            print("Right wins!")
            if right_pos == 1:          # L, R = 0, 1
                right_pos -= 1
                print(f"(2) {left_pos}, {right_pos}")
            elif right_pos == 0:        # L, R = 0, 0
                print(f"Right has won the game in {num_seconds}s!")
                results.append(num_seconds)
                break
            else:
                left_pos = 0.0
                print(f"(2) {left_pos}, {right_pos}")

mean_game_length = sum(results)/num_simulations
print(f"After {num_simulations} trials, the average {num_hoops}-hoop game lasts {mean_game_length}s.")
print(f"Calculated in {time.perf_counter()}s")
