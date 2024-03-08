def rm_all(elem, lst):
    new_list = []
    for item in lst:
        if item != elem:
            new_list.append(item)
    lst[:] = new_list
        
    

x = [3, 1, 2, 1, 5, 1, 1, 7]
rm_all(1, x)
print(x)  

