from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    v = int(input())
    b_tree = [[] for _ in range(v)]
    for i in range(v-1):
        [a, b] = [int(x) for x in input().split()]
        b_tree[a-1].append(b-1)
    leaf_nodes = [i for i in range(v) if not b_tree[i]]
    print(int(((len(leaf_nodes) - 1)/2)*len(leaf_nodes)))


if __name__ == "__main__":
    main()
