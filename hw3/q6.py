def flatten(lst):
    new_list = []
    for item in lst:
        if isinstance(item, list):
            new_list.extend(flatten(item))
        else:
            new_list.append(item)
    return new_list


print(flatten([1, 2, 3]))  
x = [1, [2, 3], 4]
print(flatten(x))          
x = [[1, [1, 1]], 1, [1, 1]]
print(flatten(x))           
