def chk_elm(lst, n):
    if n in lst:
        return True
    else:
        for item in lst:
            if isinstance(item, list):
                if chk_elm(item, n):
                    return True
    return False


a = [ [1,[2]], 3, [ [4], [5,[6] ] ] ]
print(chk_elm(a, 6))  
