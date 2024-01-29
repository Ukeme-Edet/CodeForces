def solve_eqn(a, b, c):
    delta = pow(pow(b, 2) - 4*a*c, .5)
    res = [0, 0]
    return res


a, b, c = [int(x) for x in input(
    "Enter the coeficients of the quadratic equation a, b and c in the form ax² + bx + c = 0: \n").split()]
res = solve_eqn(a, b, c)
print(f"x = {res[0]} and x = {res[1]}")
