from sys import stdin, stdout


class Card:
    def __init__(self, color, next, prev):
        self.color = color
        self.next = next
        self.prev = prev


class Deck:
    def __init__(self, cards):
        self.cards = cards
        self.head = Card(0, None, None)
        self.tail = Card(0, None, None)
        self.head.next, self.tail.prev = self.tail, self.head
        for i in cards[::-1]:
            self.add_top(i)

    def add_top(self, card):
        card.next, card.prev = self.head.next, self.head
        self.head.next.prev = card
        self.head.next = card

    def remove(self, card):
        card.next.prev = card.prev
        card.prev.next = card.next
        return card

    def search(self, color):
        cur = self.head.next
        i = 0
        while cur != self.tail:
            i += 1
            if cur.color == color:
                return [cur, i]
            cur = cur.next
        return None

    def query(self, color):
        res = self.search(color)
        if res:
            card, i = res
            self.add_top(self.remove(card))
            return i
        else:
            return -1


def input():
    return stdin.readline().strip()


def main():
    n, q = [int(_) for _ in input().split()]
    a = [int(_) for _ in input().split()]
    t = [int(_) for _ in input().split()]
    deck = Deck([Card(i, None, None) for i in a])
    for i in range(q):
        stdout.write(str(deck.query(t[i])) + (" " if i < q - 1 else ""))
    stdout.write("\n")


if __name__ == "__main__":
    main()
