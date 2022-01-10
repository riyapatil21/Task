def Pushzero(arr, n):       
    count = 0 
    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count+=1
    while count < n:
        arr[count] = 0
        count += 1
#Driver code
num_list1 = [12,0,16,0,0,0,20,70]
n = len(num_list1)
Pushzero(num_list1, n)
num_list2 = [90,0,20,0,0,80,10,0]
n = len(num_list2)
Pushzero(num_list2, n)
print("Array after pushing all zeros to end of array:")
print(num_list1)
print(num_list2)


