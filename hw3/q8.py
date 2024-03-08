def sym(l):
    if len(l) <= 1:
        return True
    else:
        if l[0] == l[-1]:
            return sym(l[1:-1])
        else:
            return False

print(sym([]))
print(sym([1]))
print(sym([1,4,5,1]))
print(sym([1,4,4,1]))
print(sym(["1","o","1"]))