from timeit2 import ti2

arg = range(10 ** 6)
ti2(
    max,
    sum,
    args=[arg],
    floor=4,
    print_return=True,
    return_label="ret: ",
    relative=True,
)