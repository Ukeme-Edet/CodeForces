from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    polys = {"Tetrahedron": 4, "Cube": 6, "Octahedron": 8,
             "Dodecahedron": 12, "Icosahedron": 20}
    faces = 0
    for _ in range(n):
        faces += polys[input()]
    print(faces)


if __name__ == "__main__":
    main()
