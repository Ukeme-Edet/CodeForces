from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    tree = [[] for _ in range(n + 1)]
    roots = []
    for i in range(n):
        p = int(input())
        if p > 0:
            tree[p].append(i + 1)
        else:
            roots.append(i + 1)
    queue, max_level = [(root, 1) for root in roots], 0
    while queue:
        node, level = queue.pop(0)
        max_level = max(max_level, level)
        for child in tree[node]:
            queue.append((child, level + 1))
    print(max_level)


if __name__ == "__main__":
    main()
