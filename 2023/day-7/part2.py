class Hand:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = int(bid)
        self.rankings = {"J": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "Q": 12, "K": 13, "A": 14}
        self.counts = dict()
        for letter in self.hand:
            self.counts[letter] = self.counts.get(letter, 0) + 1

        self.count_to_add = 0
        if "J" in self.counts and self.counts["J"] != 5:
            self.count_to_add = self.counts["J"]
            self.counts.pop("J")
    
    def rank(self):
        return max(self.counts.values()) + self.count_to_add
    
    def __gt__(self, other):
        self_rank = self.rank()
        other_rank = other.rank()

        if self_rank == other_rank:
            if self_rank == 3 or self_rank == 2:
                if len(self.counts) != len(other.counts):
                    return not len(self.counts) > len(other.counts)
            for hand_index in range(len(self.hand)):
                if self.hand[hand_index] == other.hand[hand_index]:
                    continue
                else:
                    return self.rankings[self.hand[hand_index]] > self.rankings[other.hand[hand_index]]
        else:
            return self_rank > other_rank
    
    def __str__(self):
        return self.hand


def get_input():
    puzzle_lines = list()
    with open("input.txt", "r") as puzzle_input:
        lines = puzzle_input.readlines()
        for line in lines:
            line = line.strip()
            if line:
                hand, bid = line.split() 
                puzzle_lines.append((hand, bid))
    
    return puzzle_lines


def main():
    import heapq
    hand_heap = list()
    lines = get_input()
    for hand, bid in lines:
        heapq.heappush(hand_heap, Hand(hand, bid))
    
    running_sum = 0
    counter = 1
    while hand_heap:
        hand = heapq.heappop(hand_heap)
        running_sum += counter * hand.bid
        counter += 1
    
    print(running_sum)


if __name__ == "__main__":
    main()