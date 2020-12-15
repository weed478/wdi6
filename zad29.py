from math import sqrt

import matplotlib.pyplot as plt
from matplotlib import animation

from myszka import meszgen


class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"


def points_plot(tab, gif=False):
    x, y, z = [], [], []
    a = tab[-1]
    tab = tab[:-1]
    for point in tab:
        x.append(point.get_x())
        y.append(point.get_y())
        z.append(point.get_z())

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(x, y, z, c='r', marker='o')
    ax.scatter(a.get_x(), a.get_y(), a.get_z(), c='b', marker='o')
    ax.scatter(0, 0, 0, c='g', marker='o')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    fig.show()

    if gif:
        def rotate(angle):
            ax.view_init(azim=angle)

        print("Making animation")
        rot_animation = animation.FuncAnimation(fig, rotate, frames=range(0, 360, 1))
        rot_animation.save('rotation.gif', fps=30, dpi=80, writer='imagemagick')


points = [Point(2, 3, 9), Point(3, 5, 0), Point(5, 7, -8), Point(1, 4, 6), Point(9, 7, 1), Point(6, -0, -10)]


def srodek(tab):
    n = len(tab)
    x, y, z = 0, 0, 0
    for _ in tab:
        x += _.get_x()
        y += _.get_y()
        z += _.get_z()
    return Point(x / n, y / n, z / n)


def zad29(tab, r):
    n = len(tab)

    def next_i(i=None):
        if i is None:
            return 0

        elif i + 1 < n:
            return i + 1

        else:
            return None

    for i in meszgen(next_i):
        _tab = [tab[j] for j in i]
        if len(_tab) > 2:
            s = srodek(_tab)
            x = s.get_x()
            y = s.get_y()
            z = s.get_z()
            d = sqrt(x * x + y * y + z * z)
            if d > r:
                _tab.append(s)
                points_plot(_tab)
                # print(s)
                return True
    return False


print(zad29(points, 7))
