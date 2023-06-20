def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        tree = Tree(n)
        for i in range(n-1):
            n1, n2 = map(int, input().split())
            tree.add_edge(n1, n2)
        q = int(input())
        for j in range(q):
            x, y = map(int, input().split())
            total_x = tree.number_of_end_nodes(x-1)
            total_y = tree.number_of_end_nodes(y-1)
            print(total_x * total_y)


class Tree:
    def __init__(self, n):
        self.nodes = [None for _ in range(n)]
        self.nodes[0] = Node()

    def add_edge(self, n1, n2):
        if self.nodes[n1-1] is None:
            self.nodes[n1-1] = Node()
        if self.nodes[n2-1] is None:
            self.nodes[n2-1] = Node()
        if n1 < n2:
            self.nodes[n1-1].add_child(n2-1)
        else:
            self.nodes[n2-1].add_child(n1-1)

    def number_of_end_nodes(self, node):
        if len(self.nodes[node].children) == 0:
            return 1
        count = 0
        for child in self.nodes[node].children:
            count += self.number_of_end_nodes(child)
        return count


class Node:
    def __init__(self):
        self.children = []
        apple = False

    def add_child(self, child):
        self.children.append(child)

    def add_apple(self):
        self.apple = True


if __name__ == "__main__":
    main()
