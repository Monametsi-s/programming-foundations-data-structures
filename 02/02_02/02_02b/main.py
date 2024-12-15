''' 
Problem Statement: Compute the average number of pets each student 
has in a given class. 
'''
student_pet_count_list = [0, 1, 0, 2, 1, 1, 4, 0, 0, 0, 3, 2, 1, 3, 0, 2, 2, 4]

test1 = [3, 7, 8, 3, 2, 8, 9]

student_pet_count_list[2] += 3
student_pet_count_list[3] += 1
student_pet_count_list[-1] += 2

student_pet_count_list.append(4)



def avg(lis):
  total = 0
  for student in lis:
    total += student
  return total / len(lis), total


num_of_students = len(student_pet_count_list)
print(num_of_students)
print(avg(student_pet_count_list))
print(avg(test1))


