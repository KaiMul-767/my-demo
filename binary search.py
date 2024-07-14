lst = [3,7,8,32,51,55,57,89,91,99]
item = 7
left = 0
right = len(lst)-1

while(left<=right):
    middle = (left + right) // 2
    if (lst[middle] == item):
        print('item founded', middle)
        exit()
    elif (lst[middle] < item):
        left = middle + 1
    else:
        right = middle - 1
print('item not founded')
