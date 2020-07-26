test_list1 = [10,20,40,60,70,80]
test_list2 = [5,15,25,35,45,60]

print ("The original list 1 is : " + str(test_list1))
print ("The original list 2 is : " + str(test_list2))

size_1 = len(test_list1)
size_2 = len(test_list2)

res = []
i, j = 0, 0

while i < size_1 and j < size_2:
    if test_list1[i] < test_list2[j]:
        res.append(test_list1[i])
        i += 1
    else:
        res.append(test_list2[j])
        j += 1

res = res + test_list1[i:] + test_list2[j:]
print ("The combined sorted list is : " + str(res))
