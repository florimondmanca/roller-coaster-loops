import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import ode


class Problem:
    g = 9.81

    def __init__(self, C, y0=0, v0=25, ds=0.01, s1=10):
        self.C = C
        self.y0 = y0
        self.v0 = v0
        self.ds = ds
        self.s1 = s1
        self.x = None
        self.y = None

    def f(self, s, z):
        return [
            self.C / (self.v0 ** 2 / self.g - 2 * z[2]),
            np.cos(z[0]),
            np.sin(z[0]),
        ]

    def solve(self):
        self.x, self.y = [], []

        r = ode(self.f)
        r.set_initial_value([0, 0, self.y0], 0)

        while r.successful():
            _, xi, yi = r.integrate(r.t + self.ds)
            self.x.append(xi)
            self.y.append(yi)
            if r.t >= self.s1 and abs(yi - self.y0) < 1e-2:
                break

    def plot(self):
        if self.x is None or self.y is None:
            raise ValueError("Not solved yet")

        plt.plot(self.x, self.y, label=f"$C$ = {self.C}")


def main(cs, v0):
    for c in cs:
        p = Problem(C=c, v0=v0)
        p.solve()
        p.plot()

    plt.xlabel("$x$ (m)")
    plt.ylabel("$y$ (m)")
    plt.axis("equal")
    plt.title(
        "Loop shapes. "
        "Constant centripetal acceleration: $a_c = Cg$. "
        f"Initial velocity: $v_0 = {v0}$."
    )
    plt.legend()
    plt.show()


if __name__ == "__main__":
    cs = [int(c) for c in sys.argv[1:]] or [3]
    main(cs, v0=25)
