def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        res = set()
        for i in range(len(a)):
            for j in range(i+1, len(a)):
                if (a[i] != 0 or a[j] != 0) and (abs(a[i] - a[j]) in a):
                    new = [a[i], a[j]]
                    new.sort(reverse=True)
                    res.add(",".join(list(map(str, new))))
        res = list(res)
        res = [x.split(",") for x in res]
        printed = False
        for j in range(1, len(res)):
            if res[0][0] not in res[j]:
                if res[0][1] != '0':
                    print(res[0][1])
                    printed = True
                    break
        if sum(a) == 0 and res == []:
            print(0)
            printed = True
        if not printed:
            print(res[0][0])


if __name__ == '__main__':
    main()
