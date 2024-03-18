from sys import stdin, stdout


def input() -> str:
    return stdin.readline().strip()


def print(string) -> int:
    return stdout.write(str(string) + "\n")


def main() -> None:
    t = int(input())
    for _ in range(t):
        n, k = [int(x) for x in input().split()]
        a: list[int] = [int(x) for x in input().split()]
        x: list[int] = [abs(int(x)) for x in input().split()]
        ax: list[tuple[int, int]] = [(0, 0) for _ in range(n)]
        for i in range(n):
            ax[i] = (a[i], x[i])
        ax.sort(key=lambda x: (x[1]))
        last = next = 0
        for i in range(n):
            if ax[i][0] > k * (ax[i][1] - last) + next:
                print("NO")
                break
            next += k * (ax[i][1] - last) - ax[i][0]
            last: int = ax[i][1]
        else:
            print("YES")


if __name__ == "__main__":
    main()
