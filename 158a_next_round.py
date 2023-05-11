def main():
    _, k = map(int, input().split(" "))
    scores = list(map(int, input().split(" ")))
    if scores[k - 1] > 0:
        while k < len(scores) and scores[k - 1] == scores[k]:
            k += 1
    elif scores[k - 1] < 1:
        while k > 1 and scores[k - 1] == scores[k - 2]:
            k -= 1
        k -= 1
    print(k)


if "__main__" == __name__:
    main()
