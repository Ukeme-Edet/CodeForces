from sys import stdin, stdout


def input():
	return stdin.readline().strip()


def print(string):
	return stdout.write(str(string) + "\n")


def main():
	t = int(input())
	for _ in range(t):
		n = int(input())
		print("First" if n % 3 else "Second")


if __name__ == "__main__":
	main()