from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    def dfs(parent, node):
        if len(tree[node]) == 1 and tree[node][0] == parent:
            leaf_count[node] = 1
        else:
            for child in tree[node]:
                if child != parent:
                    if leaf_count[child] == 0:
                        dfs(node, child)
                    leaf_count[node] += leaf_count[child]

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
        dfs(-1, 0)
        q = int(input())
        for i in range(q):
            x, y = map(int, input().split())
            x -= 1
            y -= 1
            print(leaf_count[x] * leaf_count[y])


if __name__ == "__main__":
    main()
