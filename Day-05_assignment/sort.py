def pushZerosToEnd(orig_list, n):
    count = 0  
    for i in range(n):
        if orig_list[i] != 0:
            orig_list[count] = orig_list[i]
            count += 1
            
    while count < n:
        orig_list[count] = 0
        count += 1

orig_list = [0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
orig_list.sort()
n = len(orig_list)
pushZerosToEnd(orig_list, n)
print(orig_list)