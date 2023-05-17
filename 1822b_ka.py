def calculate_max_beauty(n, array):
    max_beauty = float('-inf')

    for i in range(n - 1):
        max_beauty = max(max_beauty, array[i] * array[i+1], max_beauty)

    return max_beauty


# Read the number of test cases
t = int(input())

# Iterate over each test case
for _ in range(t):
    # Read the inputs for the current test case
    n = int(input())
    array = list(map(int, input().split()))

    # Call the function to calculate the maximum beauty
    result = calculate_max_beauty(n, array)

    # Print the result
    print(result)
