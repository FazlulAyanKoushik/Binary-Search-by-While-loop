from turtle import left
from xmlrpc.client import Boolean


def binary_search(list, target):
    count = 0
    left = 0
    right = len(list)-1
    print(f"count {count}")
    while left <= right:
        count = count + 1
        print(f'Count {count}')
        middle = (left + right) // 2
        print(f"left is {left}, right is {right} middle pont is {middle}")
        if target == list[middle]:
            print(f"{list[middle]} is exist in index number {middle} and loop count {count}")
            break
        elif target > list[middle]:
            left = middle + 1
            
        elif target < list[middle]:
            right = middle - 1
            
        else:
            print('That number not found in your list')
            
            
            
numbers = [9,12,6,4,38,46,36,16,45,12,17,2,4,25,12,14,22,20]
numbers = sorted(numbers)
print(f'Sorted numbers are : {numbers}')
find = 16
binary_search(numbers, find)