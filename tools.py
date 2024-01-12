# f strings
import string

# user_name = 'Paul'
# user_age = 20
# user_information = f'{user_name} is {user_age} years old'
# bad_approach = user_name + 'is ' + str(user_age) + ' years old' #wrong approach
# print(user_information)

# single line if statements
# user_name = "Anna"
# user_age = 15
# user_status = 'Adult' if user_age >= 18 else 'Child' #single version (below is long version)
# if user_age < 18:
#     user_status = 'child'
# else:
#     user_status = 'Adult'
# print (f'{user_name} is {user_age} years old. The person is a {"Adult" if user_age >= 18 else "Child"}')

#list comprehension

# simple_list = [f'{j}{i}' for i in range(0, 11, 1) for j in ('a' , 'b', 'c') if j == 'a']
# for i in range(0, 11, 1):
#     simple_list.append(i)
# print(simple_list)

#lambda functions

# def double_value(num):
#     return num * 2

# double_value = lambda num: num * 2
# print(double_value(10))

#some functions want  function as an arguement

# random_list = [('Anna', 25), ('Bob', 35), ('David', 10)]
# random_list = [0,5,2,4,1,123,523]
# sorted_list = sorted(random_list, key=lambda user_tuple: user_tuple[1])
# print(sorted_list)

#exercise (battleships

battleship_board = [f'{letter}{num}' for letter in ('A', 'B', 'C', 'D', 'E') for num in range(1,6) if f'{letter}{num}' != 'C3']
print(battleship_board)
