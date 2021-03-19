def multi_table(raw, column):
    for i in range(raw):
        print('  ')
        for j in range(column):
            print(' ', end=' ')
            print(f"{((i+1) * (j+1)):02d}", end=' ')


print(multi_table(5, 5))
