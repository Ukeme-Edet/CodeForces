from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        tree = [[] for i in range(n)]
        for i in range(n-1):
            u, v = map(int, input().split())
            u -= 1
            v -= 1
            tree[u].append(v)
            tree[v].append(u)
        leaf_count = [0 for _ in range(n)]
        stack = [(0, 0, -1)]
        while stack:
            node, visit_count, parent = stack.pop()
            if visit_count == 0:
                stack.append((node, 1, parent))
                for child in tree[node]:
                    if child != parent:
                        stack.append((child, 0, node))
            else:
                if tree[node] == [parent]:
                    leaf_count[node] = 1
                else:
                    leaf_count[node] = sum(leaf_count[child]
                                           for child in tree[node] if child != parent)
        q = int(input())
        for i in range(q):
            x, y = map(int, input().split())
            x -= 1
            y -= 1
            print(leaf_count[x] * leaf_count[y])


if __name__ == "__main__":
    main()
