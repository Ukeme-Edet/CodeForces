def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split(" ")))
        if build_even(a, n) or build_odd(a, n):
            print("YES")
            continue
        print("NO")


def build_even(a, n):
    temp = 0
    even_hash = {"op": [], "on": [], "en": []}
    for i in range(n):
        if a[i] % 2 != 0 or a[i] < 1:
            if a[i] % 2 == 1 and a[i] > 0:
                even_hash["op"].append(a[i])
            elif a[i] % 2 == 0 and a[i] < 1:
                even_hash["en"].append(a[i])
            else:
                even_hash["on"].append(a[i])
    for i in range(n):
        if a[i] % 2 != 0 or a[i] < 1:
            if a[i] % 2 == 1 and a[i] > 0:
                opon = even_hash["op"] + even_hash["on"]
                for hash in opon:
                    temp = a[i] - hash
                    if temp < 1:
                        continue
                    if temp % 2 == 0:
                        break
                if temp % 2 != 0 or temp < 1:
                    return False
            elif a[i] % 2 == 0 and a[i] < 1:
                for hash in even_hash["en"]:
                    temp = a[i] - hash
                    if temp < 1:
                        continue
                    if temp % 2 == 0:
                        break
                if temp % 2 != 0 or temp < 1:
                    return False
            else:
                for hash in even_hash["on"]:
                    temp = a[i] - hash
                    if temp < 1:
                        continue
                    if temp % 2 == 0:
                        break
                if temp % 2 != 0 or temp < 1:
                    return False
    return True


def build_odd(a, n):
    temp = 0
    odd_hash = {"op": [], "en": [], "on": []}
    for i in range(n):
        if a[i] % 2 != 1 or a[i] < 1:
            if a[i] % 2 == 0 and a[i] > 0:
                continue
            elif a[i] % 2 == 1 and a[i] < 1:
                odd_hash["on"].append(a[i])
            else:
                odd_hash["en"].append(a[i])
        else:
            odd_hash["op"].append(a[i])
    for i in range(n):
        if a[i] % 2 != 1 or a[i] < 1:
            if a[i] % 2 == 0 and a[i] > 0:
                opon = odd_hash["op"] + odd_hash["on"]
                for hash in opon:
                    temp = a[i] - hash
                    if temp < 1:
                        continue
                    if temp % 2 == 1:
                        break
                if temp % 2 != 1 or temp < 1:
                    return False
            elif a[i] % 2 == 1 and a[i] < 1:
                for hash in odd_hash["en"]:
                    temp = a[i] - hash
                    if temp < 1:
                        continue
                    if temp % 2 == 1:
                        break
                if temp % 2 != 1 or temp < 1:
                    return False
            else:
                for hash in odd_hash["on"]:
                    temp = a[i] - hash
                    if temp < 1:
                        continue
                    if temp % 2 == 1:
                        break
                if temp % 2 != 1 or temp < 1:
                    return False
    return True


if __name__ == "__main__":
    main()
