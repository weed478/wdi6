def semi_euler(connections, start_point=None):
    """Return Semi-Euler path or False if not found

    :param connections: List of connection nodes, e.g. [(1,2), (2,3), (4,3), (2,4)]
    :param start_point: Number from where route starts.
    """
    return euler(connections, start_point, True)


def euler(connections, start_point=None, semi=False):
    """Return Euler path or False if not found

    :param connections: List of connection nodes, e.g. [(1,2), (2,3), (4,3), (2,4)]
    :param start_point: Number from where route starts.
    :param semi: If True return Semi-Euler instead of Euler route.
    """
    n = len(connections)

    if n < 1:
        return False

    visited = [False] * n
    path = []

    def gen_next(con, a, b):
        visited[con] = True
        path.append(connections[con][a])
        if find_route(connections[con][b]):
            return path
        else:
            path.pop()
            visited[con] = False

    def find_route(start):
        if visited == [True] * n:
            path.append(start)
            if semi is False:
                if path[0] == start:
                    return path
            else:
                return path

        for con in range(len(connections)):
            if visited[con] is False:
                # check both points in node
                if connections[con][0] == start:
                    l = gen_next(con, 0, 1)
                    if l: return l
                if connections[con][1] == start:
                    r = gen_next(con, 1, 0)
                    if r: return r
        return False

    if start_point is None:
        points = set()
        for node in connections:
            for point in node:
                points.add(point)

        for point in points:
            a = find_route(point)
            if a:
                return a
            path.clear()
        return False

    return find_route(start_point)


if __name__ == "__main__":

    """
    3 --- 4 --- 5
    |   /   \   |
    | /       \ |
    2 --------- 6
      \       /
        \   /
          1

    3 --- 4 --- 5
    | \ /   \   |
    | / ----\ \ |
    2 --------- 6
      \
        \
          1
    """

    _list = [(1, 2), (1, 6), (2, 3), (2, 4), (2, 6), (3, 4), (4, 5), (4, 6), (5, 6)]
    print(euler(_list))
    _list[1] = (3, 6)
    print(euler(_list))
    print(semi_euler(_list))
