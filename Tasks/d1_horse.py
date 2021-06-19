_possible_steps = ((+ 1, - 2), (+ 1, + 2), (+ 2, - 1), (+ 2, + 1))


def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    field = [[0] * shape[1] for _ in range(shape[0])]
    field[0][0] = 1
    for i in range(shape[0]):
        for j in range(shape[1]):
            print(field[i][j], end='\t')
        print()
    for i in range(shape[0]):
        for j in range(shape[1]):
            if field[i][j] != 0:
                step1 = (i + 1, j - 2)
                if 0 <= step1[0] < shape[0] and 0 <= step1[1] < shape[1]:
                    field[step1[0]][step1[1]] += field[i][j] * 2
                step2 = (i + 1, j + 2)
                if 0 <= step2[0] < shape[0] and 0 <= step2[1] < shape[1]:
                    field[step2[0]][step2[1]] += field[i][j] * 2
                step3 = (i + 2, j - 1)
                if 0 <= step3[0] < shape[0] and 0 <= step3[1] < shape[1]:
                    field[step3[0]][step3[1]] += field[i][j] * 2
                step4 = (i + 2, j + 1)
                if 0 <= step4[0] < shape[0] and 0 <= step4[1] < shape[1]:
                    field[step4[0]][step4[1]] += field[i][j] * 2



calculate_paths((8, 8), (7, 7))
