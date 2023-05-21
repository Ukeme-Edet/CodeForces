def main():
    test_cases = int(input())
    for i in range(test_cases):
        n, max_abs_deviation = map(int, input().split(" "))
        forcasted_temps = list(map(int, input().split(" ")))
        real_temps = list(map(int, input().split(" ")))
        for j in range(n):
            if abs(forcasted_temps[j] - real_temps[j]) > max_abs_deviation:
                k = j + 1
                while k < n - 1 and abs(forcasted_temps[j] - real_temps[k]) > max_abs_deviation:
                    k += 1
                real_temps[j], real_temps[k] = real_temps[k], real_temps[j]
        print(" ".join(list(map(str, real_temps))))


if __name__ == "__main__":
    main()
