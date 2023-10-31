from sys import stdin, stdout


def input():
	return stdin.readline().strip()


def print(string):
	return stdout.write(str(string) + "\n")


def main():
	t = int(input())
	for _ in range(t):
		n, k = [int(x) for x in input().split()]
		a = sorted([(int(x), i) for i, x in enumerate(input().split())])
		segments = 1
		for i in range(1, n):
			if a[i][1] - a[i - 1][1] != 1:
				segments += 1
		print("Yes" if segments <= k else "No")


if __name__ == "__main__":
	main()