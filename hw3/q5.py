def merge_sorted_lists(a, b):
  
    if not a:
        return b
    if not b:
        return a
    if a[0] < b[0]:
        return [a[0]] + merge_sorted_lists(a[1:], b)
    else:
        return [b[0]] + merge_sorted_lists(a, b[1:])


print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  
print(merge_sorted_lists([], [2, 4, 6]))       
print(merge_sorted_lists([1, 2, 3], []))         
print(merge_sorted_lists([5, 7], [2, 4, 6]))     
