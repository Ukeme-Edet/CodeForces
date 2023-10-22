from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, k = [int(x) for x in input().split()]
        s = input()
        let_dict = [0] * 26
        for i in range(n):
            let_dict[ord(s[i]) - 97] += 1
        let_dict.sort(key=lambda x: (x % 2, -x), reverse=True)
        let_dict = [x for x in let_dict if x > 0]
        while k > 0 and sum([x % 2 for x in let_dict]) > 0:
            let_dict[0] -= 1
            k -= 1
            if let_dict[0] == 0:
                let_dict.pop(0)
            else:
                let_dict.sort(key=lambda x: (x % 2, -x), reverse=True)
        if k == 0 and sum([x % 2 for x in let_dict]) > 1:
            print("NO")
        elif k > 0:
            while k > 0 and let_dict:
                curr = let_dict[0]
                let_dict[0] -= min(k, let_dict[0])
                k -= min(k, curr)
                if let_dict[0] == 0:
                    let_dict.pop(0)
                else:
                    let_dict.sort(key=lambda x: (x % 2, -x), reverse=True)
            if sum([x % 2 for x in let_dict]) > 1:
                print("NO")
            else:
                print("YES")
        else:
            print("YES")


if __name__ == "__main__":
    main()
