def add_vectors(u, v):
    """
      >>> add_vectors([1, 0], [1, 1])
      [2, 1]
      >>> add_vectors([1, 2], [1, 4])
      [2, 6]
      >>> add_vectors([1, 2, 1], [1, 4, 3])
      [2, 6, 4]
      >>> add_vectors([11, 0, -4, 5], [2, -4, 17, 0])
      [13, -4, 13, 5]
      >>> a = [1, 2, 3]
      >>> b = [1, 1, 1]
      >>> add_vectors(a, b)
      [2, 3, 4]
      >>> a
      [1, 2, 3]
      >>> b
      [1, 1, 1]
    """
    sum_vec = []
    if len(u) == len(v):
        for i in range(len(u)):
            sum_vec.append((u[i]+v[i]))
        return sum_vec
    else:
        print("The vectors have to be the same length")


def scalar_mult(s, v):
    """
      >>> scalar_mult(5, [1, 2])
      [5, 10]
      >>> scalar_mult(3, [1, 0, -1])
      [3, 0, -3]
      >>> scalar_mult(7, [3, 0, 5, 11, 2])
      [21, 0, 35, 77, 14]
      >>> a = [1, 2, 3]
      >>> scalar_mult(4, a)
      [4, 8, 12]
      >>> a
      [1, 2, 3]
    """
    multi_vec = []
    for i in v:
        multi_vec.append(i*s)
    return multi_vec


def dot_product(u, v):
    """
      >>> dot_product([1, 1], [1, 1])
      2
      >>> dot_product([1, 2], [1, 4])
      9
      >>> dot_product([1, 2, 1], [1, 4, 3])
      12
      >>> dot_product([2, 0, -1, 1], [1, 5, 2, 0])
      0
    """
    dot_product = 0
    if len(u) == len(v):
        for i in range(len(u)):
            dot_product += (u[i] + v[i])
        return dot_product
    else:
        print('The vectors have to be the same length')


a = [2, 0, -1, 1]
b = [1, 5, 2, 0]
print(dot_product(a, b))
