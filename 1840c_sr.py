import math


def main():
    t = int(input())
    for _ in range(t):
        n, k, q = map(int, input().split())
        a = list(map(int, input().split()))
        consecutive_days = []
        current_consecutive_days = 0
        for i in range(n):
            if a[i] > q and current_consecutive_days > 0:
                consecutive_days.append(current_consecutive_days)
                current_consecutive_days = 0
            elif a[i] <= q:
                current_consecutive_days += 1
        if current_consecutive_days > 0:
            consecutive_days.append(current_consecutive_days)
        consecutive_days = [min(x, n) for x in consecutive_days]
        consecutive_days = [x for x in consecutive_days if x >= k]
        total_consecutive_days = 0
        for i in range(len(consecutive_days)):
            total_consecutive_days += calculate_selection(
                consecutive_days[i], k)
        print(total_consecutive_days)


def calculate_selection(consecutive_day, k):
    total_selection = 0
    for j in range(k, consecutive_day + 1):
        total_selection += consecutive_day - j + 1
    return total_selection


if __name__ == "__main__":
    main()
