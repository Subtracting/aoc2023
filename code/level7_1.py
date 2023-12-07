filename = "inputs\level7_input.txt"

total = 1

hands = dict()

with open(filename) as file:
    for line in file:
        line_list = line.rstrip().split(" ")
        hand = line_list[0]
        bid = int(line_list[1])

        hands[hand] = bid

winnings = 0
card_number = len(hands)
sort_list = [[], [], [], [], [], [], []]
card_order = "AKQJT98765432"

for hand in hands:
    uniques = len(set(hand))
    fiveofakind = uniques == 1
    fourofakind = uniques == 2 and any([hand.count(label) == 4 for label in hand])
    fullhouse = uniques == 2 and any([hand.count(label) == 3 for label in hand])
    threeofakind = uniques == 3 and any([hand.count(label) == 3 for label in hand])
    twopair = uniques == 3 and sum([1 for label in hand if hand.count(label) == 2]) == 4
    onepair = uniques == 4
    highcard = uniques == 5

    types = [
        fiveofakind,
        fourofakind,
        fullhouse,
        threeofakind,
        twopair,
        onepair,
        highcard,
    ]

    for i in range(len(types)):
        if types[i]:
            sort_list[i].append(hand)
            break

for same_hands in sort_list:
    sorted_hands = sorted(
        same_hands, key=lambda word: [card_order.index(c) for c in word]
    )
    for hand in sorted_hands:
        winnings += hands[hand] * card_number
        card_number -= 1

print(winnings)
