#linear serach
def linear_search(lst,n,item):
    for i in range(0,n):
        if (lst[i] == item):
            return i
    return -1

lst = [3,7,6,9,1,44,55,66,100]
n = len(lst)
item = 100
index = linear_search(lst,n,item)
if (index==-1):
    print('item is not found')
else:
    print('item is found at index :',index)