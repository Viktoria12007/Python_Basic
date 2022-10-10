nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

flat_list = [list for subsublist in nice_list for sublist in subsublist for list in sublist]
print('Ответ:', flat_list)

