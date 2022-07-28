from xmlrpc.client import Boolean

i = 0
numbers = [9,12,6,4,38,46,36,16]
have = Boolean
sorted_numbers = sorted(numbers)
find = 38
print(f'Sorted numbers are : {sorted_numbers}')

middle_length = int(len(sorted_numbers)/2)
middle_number = sorted_numbers[int(len(sorted_numbers)/2)]

print(f'Middle Number : {middle_number}')

while True:
    i = i + 1
    
    if find == middle_number:
        have = True
        break

    if find > middle_number:
        for index in range(middle_length+1, len(sorted_numbers), 1):
            if find == sorted_numbers[index]:
                have = True
                print(f'Your number is {find} and index is {index}')
            i = i + 1
            if have == True:
                break
    
    if find < middle_number:
        for index in range(middle_length-1, 0, -1):
            if find == sorted_numbers[index]:
                have = True
                print(f'Your number is {find} and index is {index}')
            i = i + 1
        
    
print(f'Total Iteration : {i}')
