def add_many(x, elem, lst):
    for item in lst:
        if item == x:
            lst.append(elem)

lst = [1, 2, 4, 2, 1]
add_many(2, 5, lst)
print(lst)  
