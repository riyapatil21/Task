def Pushzero(num_list, n):       
    count = 0 
    for i in range(n):
        if num_list[i] != 0:
            num_list[count] = num_list[i]
            count+=1
    while count < n:
        num_list[count] = 0
        count += 1
#Driver code
num_list = [12,0,16,0,0,0,20,70]
n = len(num_list)
Pushzero(num_list, n)
num_list = [90,0,20,0,0,80,10,0]
n1 = len(num_list)
Pushzero(num_list, n1)
print("Array after pushing all zeros to end of array:")
print(num_list)
print(num_list)


