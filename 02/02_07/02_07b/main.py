# Linear Search

my_list = [8, 5, 0, 3, 9, 7]
target = 7

def linear_search(list, target):
  for element in list:
    if element == target:
      return True
  return False

is_7_in = linear_search(my_list, target)
is_5_in = linear_search(my_list, 5)
is_1_in = linear_search(my_list, 1)

print(is_7_in)
print(is_5_in)
print(is_1_in)


#Array.sort() and sorted(Array) Functions
arr = [3, 1, 6, 4, 2, 67, 5]
print(sorted(arr))
print(arr)
#Output 
