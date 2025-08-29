"""The coordinates function"""

__author__ = "730773852"


def get_coords(xs: str, ys: str) -> None:
    i = 0
    while i < len(xs):
        j = 0
        while j < len(ys):
            print("(" + xs[i] + "," + ys[j] + ")")
            j += 1
        i += 1
