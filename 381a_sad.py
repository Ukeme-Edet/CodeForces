from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, cards, scores, l, r, turn = int(input()), [int(
        x) for x in input().split()], [0, 0], 0, -1, 0
    while l <= n + r:
        if cards[l] > cards[r]:
            scores[turn % 2] += cards[l]
            l += 1
        else:
            scores[turn % 2] += cards[r]
            r -= 1
        turn += 1
    print(f"{scores[0]} {scores[1]}")


if __name__ == "__main__":
    main()
