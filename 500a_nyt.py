from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, t = map(int, input().split())
    a = [int(x) for x in input().split()]
    graph = build_graph(a)
    current = 1
    while current < t:
        current = graph[current - 1]
        if current == t:
            print("YES")
            return
    print("NO")


def build_graph(a):
    graph = [None] * len(a)
    for i in range(len(a)):
        graph[i] = a[i] + i + 1
    return graph


if __name__ == "__main__":
    main()
