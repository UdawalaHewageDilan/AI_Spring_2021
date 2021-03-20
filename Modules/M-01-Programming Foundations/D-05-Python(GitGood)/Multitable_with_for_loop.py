def multi_table(raw, column):
    """Prints a the multiplication table of given number of raws and columns"""
    first_raw = ". |   01   02   03   04   05   06   07   08   09   10"
    second_raw = " - - - - - - - - - - - - - - - - - - - - - - - - - - -"
    print(f"{first_raw}")   # the output would be better if these were in another function.
    print(f"{second_raw}")  # the output would be better if these were in another function.
    for i in range(raw):
        print(f'\n {i+1}|', end=' ')
        for j in range(column):
            print(f' ', end=' ')
            print(f"{((i+1) * (j+1)):02d}", end=' ')


multi_table(10, 10)
