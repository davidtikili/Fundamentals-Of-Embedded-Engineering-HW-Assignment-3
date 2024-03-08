from operator import add, sub, mul

def fld(lst, g, m):
    if not lst:
        return m
    else:
        return fld(lst[1:], g, g(m, lst[0]))


s = [3, 2, 1]
print(fld(s, sub, 0))  
print(fld(s, add, 0)) 
print(fld(s, mul, 1))  
print(fld([], sub, 100))  
