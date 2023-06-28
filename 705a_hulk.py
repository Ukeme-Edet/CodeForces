from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    layers = ["I hate", "I love"]
    n = int(input())
    print(" that ".join(layers[i % 2] for i in range(
        n)) + " it" if n > 1 else layers[0] + " it")


if __name__ == "__main__":
    main()
