"""
9_B : Shuffle

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/9/ITP1_9_B

Result:
"""

import sys


input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesli = lambda: int(input()[0])
i_semli = lambda n: [i_sesli() for _ in range(n)]


def main():
    while True:
        cards = input()[0]
        if cards == '-':
            sys.exit()

        shuffle_num = i_sesli()
        shuffled_positions = i_semli(shuffle_num)
        print(shuffle(cards, shuffled_positions))


def shuffle(cards, shuffled_positions):
    shuffled_cards = cards
    card_nums = len(shuffled_cards)
    for num in shuffled_positions:
        shuffled_cards = shuffled_cards[- card_nums + num:] + shuffled_cards[:num]

    return shuffled_cards


if __name__ == '__main__':
    main()
