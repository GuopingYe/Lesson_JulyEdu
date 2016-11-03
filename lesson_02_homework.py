# -- coding: utf-8 --
from math import sqrt

# lesson_2 homework 1, reverse sentence
print('\n========================', ' Homework 1 ', '==================\n')
mystr = 'I love China!'

# split to splitt a sentence to words in a list, then [::-1], used as [start:end:step] to reverse the list,
#   then join to concatenate all strings in a list,
newStr = ' '.join(mystr.split(' ')[::-1])

print(newStr)

# lesson_2 homework 2, print out all prime numbers within 100,000
print('\n========================', ' Homework 1 ', '==================\n')
def prime_number(giveNum):
    result = ""
    if giveNum != int(giveNum):
        print("Given number ", giveNum, " is not a integer!")
    else:
        result = "True"
        for loop_i in range(2, int(sqrt(giveNum)) + 1):
            if giveNum % loop_i == 0:
                result = "False"
                break
            else:
                result = "True"

    return result

prime_number(3.3)

for i in range(1, 100000):
    if prime_number(i) == "True":
        print(j)
    else:
        pass

# lesson_2 homework 3, define a function with changable parameters
print('\n========================', ' Homework 1 ', '==================\n')
def func(a, b, c, *job, test = '', **dics):
    print(a, b, c, job, test, dics)

func(1, '. a', 'python', 'programmer', city = 'Shanghai', gender = 'M')


# lesson_2 homework 4, define a recursive function to solve hanoi problem
print('\n========================', ' Homework 1 ', '==================\n')
def hanoi(n, source, target, helper):
    if n == 1:
        print(source, ' -> ', target)
    else:
        hanoi(n - 1, source, helper, target)
        print(source, ' -> ', target)
        hanoi(n - 1, helper, target, source)

hanoi(3, 'A', 'B', 'C')

# lesson_2 homework 5, bubble sort with a defined comaprision function
print('\n========================', ' Homework 5 ', '==================\n')
def comp(a, b):
    if a > b:
        return "GE"
    elif a < b:
        return "LE"
    else:
        return "EQ"

num = [8, 1, 4, 2, 3, 2, 9 ,3, 1]
for i in range(len(num)):
    for j in range(i + 1, len(num)):
        if comp(num[i], num[j]) == 'GE':
            helper = num[i]
            num[i] = num[j]
            num[j] = helper

print(num)
