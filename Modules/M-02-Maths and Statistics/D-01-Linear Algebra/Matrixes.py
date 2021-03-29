def copy_matrix(matrix):
    """
      >>> copy_matrix([[1, 2], [3, 4]])
      [[1, 2], [3, 4]]
      >>> copy_matrix([[1, 2, 3], [4, 5, 6]])
      [[1, 2, 3], [4, 5, 6]]
      >>> copy_matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
      [[1, 2], [3, 4], [5, 6], [7, 8]]
      >>> m = [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
      >>> copyofm = copy_matrix(m)
      >>> copyofm
      [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
      >>> for row_num, row in enumerate(copyofm):
      ...     for col_num, col_val in enumerate(row):
      ...         copyofm[row_num][col_num] = 42
      ...
      >>> copyofm
      [[42, 42, 42], [42, 42, 42], [42, 42, 42]]
      >>> m
      [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
    """
    import numpy as np
    copy_of_m = np.copy(matrix)
    return copy_of_m


def add_row(matrix):
    """
      >>> m = [[0, 0], [0, 0]]
      >>> add_row(m)
      [[0, 0], [0, 0], [0, 0]]
      >>> n = [[3, 2, 5], [1, 4, 7]]
      >>> add_row(n)
      [[3, 2, 5], [1, 4, 7], [0, 0, 0]]
      >>> n
      [[3, 2, 5], [1, 4, 7]]
    """
    import numpy as np
    shape = np.shape(matrix)
    if matrix is np.zeros(shape):
        return matrix.append(np.zeros(shape[0]))



def add_column(matrix):
    """
      >>> m = [[0, 0], [0, 0]]
      >>> add_column(m)
      [[0, 0, 0], [0, 0, 0]]
      >>> n = [[3, 2], [5, 1], [4, 7]]
      >>> add_column(n)
      [[3, 2, 0], [5, 1, 0], [4, 7, 0]]
      >>> n
      [[3, 2], [5, 1], [4, 7]]
      """
    import numpy as np
    shape = np.shape(matrix)
    if matrix is np.zeros(shape):
    pass


def add_matrices(m1, m2):
    """
      >>> a = [[1, 2], [3, 4]]
      >>> b = [[2, 2], [2, 2]]
      >>> add_matrices(a, b)
      [[3, 4], [5, 6]]
      >>> c = [[8, 2], [3, 4], [5, 7]]
      >>> d = [[3, 2], [9, 2], [10, 12]]
      >>> add_matrices(c, d)
      [[11, 4], [12, 6], [15, 19]]
      >>> c
      [[8, 2], [3, 4], [5, 7]]
      >>> d
      [[3, 2], [9, 2], [10, 12]]
   """
    import numpy as np
    shape = np.shape(m1)
    sum_matrix_l = []
    for row, column in enumerate(m1):
        sum_matrix_l.append(m1[row,column]+m2[row,column])
    sum_matrix = np.array(sum_matrix_l)
    return sum_matrix.reshape(shape)


def scalar_mult(s, m):
    """
      >>> a = [[1, 2], [3, 4]]
      >>> scalar_mult(3, a)
      [[3, 6], [9, 12]]
      >>> b = [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
      >>> scalar_mult(10, b)
      [[30, 50, 70], [10, 10, 10], [0, 20, 0], [20, 20, 30]]
      >>> b
      [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
    """
    for row, column in enumerate(m):
        m[row,column] *= s

    return m


def row_times_column(m1, row, m2, column):
    """
      >>> row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 0)
      19
      >>> row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 1)
      22
      >>> row_times_column([[1, 2], [3, 4]], 1, [[5, 6], [7, 8]], 0)
      43
      >>> row_times_column([[1, 2], [3, 4]], 1, [[5, 6], [7, 8]], 1)
      50
    """

    pass


def matrix_mult(m1, m2):
   """
      >>> matrix_mult([[1, 2], [3,  4]], [[5, 6], [7, 8]])
      [[19, 22], [43, 50]]
      >>> matrix_mult([[1, 2, 3], [4,  5, 6]], [[7, 8], [9, 1], [2, 3]])
      [[31, 19], [85, 55]]
      >>> matrix_mult([[7, 8], [9, 1], [2, 3]], [[1, 2, 3], [4, 5, 6]])
      [[39, 54, 69], [13, 23, 33], [14, 19, 24]]
    """
   pass


def transpose(m):
   """
     >>> m = [[3, 4, 6]]
     >>> transpose(m)
     [[3], [4], [6]]
     >>> m
     [3, 4, 6]
     >>> m = [[3, 4, 6], [1, 5, 9]]
     >>> transpose(m)
     [[3, 1], [4, 5], [6, 9]]
   """

   pass