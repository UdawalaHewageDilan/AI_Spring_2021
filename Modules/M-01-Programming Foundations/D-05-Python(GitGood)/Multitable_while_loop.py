def multi_while_loop(raw, column):
    i = 1
    while i <= raw:
        print(" ")
        for j in range(column):
            if i <= column:
                print(f"{(i * (j+1)):02d}", end=' ')
        i += 1


multi_while_loop(4, 5)





