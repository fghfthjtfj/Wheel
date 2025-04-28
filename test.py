import random
from collections import defaultdict
class Prize:
    def __init__(self, probability):
        self.probability = probability


prizes = [Prize(0.002), Prize(0.003), Prize(0.004), Prize(0.5), Prize(0.25), Prize(0.12), Prize(0.1), Prize(0.021)]

drop = defaultdict(int)


def main():
    total_probability = sum(prize.probability for prize in prizes)

    rand = random.uniform(0, total_probability)
    cumulative = 0
    selected_prize = None
    selected_index = None

    for index, prize in enumerate(prizes):
        cumulative += prize.probability
        if rand <= cumulative:
            selected_prize = prize
            selected_index = index
            return selected_prize.probability


for _ in range(100000):
    drop[main()] += 1
print(drop)
