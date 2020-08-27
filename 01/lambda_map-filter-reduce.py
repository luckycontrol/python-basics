from functools import reduce

arr1 = [1, 2, 3, 4, 5]
arr2 = [5, 6, 7, 8, 9]

# map - lambda
print(list(map(lambda x, y: x + y, arr1, arr2)))

# filter - lambda
print(list(filter(lambda x: x % 2 == 0, arr1)))

# reduce - lambda
print(reduce(lambda x, y: x + y, arr1))

print(reduce(lambda x, y: x + y, range(1, 11)))