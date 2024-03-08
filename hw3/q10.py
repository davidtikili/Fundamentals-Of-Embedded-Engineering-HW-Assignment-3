def crte_2d_arr(rows, columns):
    
    new_list = []
    for i in range(rows):
        i = []
        for j in range(columns):
            i.append("-")
        new_list.append(i)
    return new_list
    
    

print(crte_2d_arr(3, 5))
