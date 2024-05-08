def y(t, v0, g):
    return v0 * t - 0.5 * g * t ** 2


def print_table(n, v0, g):
    interval = 2 * v0 / g
    step = interval / n

    # print a table header
    print("t\t|\ty(t)")
    print("------------------")

    # for loop
    print("Using a for loop:")
    for i in range(n + 1):
        t = i * step
        print(f"{t:.2f}\t|\t{y(t, v0, g):.2f}")

    print("\n")

    # while loop
    print("Using a while loop:")
    t = 0
    while t <= interval:
        print(f"{t:.2f}\t|\t{y(t, v0, g):.2f}")
        t += step
