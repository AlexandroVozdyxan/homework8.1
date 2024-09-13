def add_one(some_list):
# Convert list to number without any separators
    list_to_str = int("".join(map(str, some_list)))
# add one to our number
    list_to_str += 1
# we return our number + 1 to str and next we return our str to list
    return [int(i) for i in str(list_to_str)]
# print our function
print(add_one([1, 2, 3]))
# test our function
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")





