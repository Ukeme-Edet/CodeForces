from sys import stdin, stdout


def input():
	return stdin.readline().strip()


def print(string):
	return stdout.write(str(string) + "\n")


def main():
	n = int(input())
	a = [int(_) % 2 for _ in input().split()]
	a_sum = sum(a)
	for i in range(n):
		if a[i] == a_sum or (a[i] == 0 and a_sum > 1):
			print(i + 1)
			return


if __name__ == "__main__":
	main()
