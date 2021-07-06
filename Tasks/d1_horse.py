def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    _possible_steps = [(+ 1, - 2), (+ 1, + 2), (+ 2, - 1), (+ 2, + 1)]
    field = [[0] * shape[1] for _ in range(shape[0])]
    field[0][0] = 1

    for i in range(shape[0]):
        for j in range(shape[1]):
            if field[i][j] != 0:
                for step in _possible_steps:
                    if 0 <= i + step[0] < shape[0] and 0 <= j + step[1] < shape[1]:
                        field[i + step[0]][j + step[1]] += field[i][j] * 2

    return field[point[0]][point[1]]


