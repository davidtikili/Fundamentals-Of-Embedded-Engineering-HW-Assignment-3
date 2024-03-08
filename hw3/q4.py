def f(suits, numbers):
    suits_numbers = []
    for suit in suits:
        for number in numbers:
            suits_numbers.append([suit,number])
    return suits_numbers


print(f(['S', 'C'], [1, 2, 3]))
print(f(['S', 'C'], [3, 2, 1]))
print(f([], [3, 2, 1]))
print(f(['S', 'C'], []))
