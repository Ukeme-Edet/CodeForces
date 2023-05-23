def main():
    # test_cases = int(input())
    # for i in range(test_cases):
    #     n, max_abs_deviation = map(int, input().split(" "))
    #     forcasted_temps = list(map(int, input().split(" ")))
    #     real_temps = list(map(int, input().split(" ")))
    #     for j in range(n):
    #         if abs(forcasted_temps[j] - real_temps[j]) > max_abs_deviation:
    #             k = j + 1
    #             while k < n - 1 and abs(forcasted_temps[j] - real_temps[k]) > max_abs_deviation:
    #                 k += 1
    #             real_temps[j], real_temps[k] = real_temps[k], real_temps[j]
    #     print(" ".join(list(map(str, real_temps))))
    def sort_by_value(t):
        return t[0]

    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split(" ")))
        b = list(map(int, input().split(" ")))
        a_c, b_c = a.copy(), b.copy()
        for i in range(n):
            a[i] = (a[i], i)
            b[i] = (b[i], i)
        a.sort(key=sort_by_value)
        b.sort(key=sort_by_value)
        for i in range(n):
            b_c[a[i][1]] = b[i][0]
        print(" ".join(list(map(str, b_c))))


if __name__ == "__main__":
    main()
