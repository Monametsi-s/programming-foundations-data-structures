
def find_second_smallest(my_list):
    if len(my_list) < 2:
        return None
    sorted_list = sorted(my_list)
    return sorted_list[1]



def  find_second_smallone(lis):
    lis = sorted(lis)
    second_smallest = lis[1]
    return second_smallest

#Creating a random arraty for testing
import random as rand
def random_array():
    '''Creates a random array'''
    random_arr = rand.sample(range(1, 28), 7, counts=None)
    return random_arr

test_list = random_array()
print(test_list)























def find_second_smallest_v2(my_list):
    if len(my_list) < 2:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for num in my_list:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    return second_smallest

print(find_second_smallest_v2([5, 8, 3, 2, 6]))
