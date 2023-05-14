def main():
    program_length = int(input())
    output = 0
    for _ in range(program_length):
        program = input()
        if program.find("++") > -1:
            output += 1
        else:
            output -= 1
    print(output)


if __name__ == "__main__":
    main()
