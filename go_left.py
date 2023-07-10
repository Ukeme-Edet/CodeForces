from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    for j in range(n):
        k, m = map(int, input().split())
        graph = [[] for _ in range(k)]
        for i in range(m):
            [a, b] = [int(x) for x in input().split()]
            graph[a].append(b)
            graph[b].append(a)
        if path_exists(graph, k-1):
            print(j+1)
            break


def path_exists(graph, destination):
    visited = [False] * len(graph)
    queue = [0]
    while queue:
        node = queue.pop(0)
        if node == destination:
            return True
        if not visited[node]:
            visited[node] = True
            queue.extend(graph[node])
    return False


if __name__ == "__main__":
    main()
