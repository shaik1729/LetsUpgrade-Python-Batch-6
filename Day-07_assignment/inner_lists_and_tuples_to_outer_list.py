list1 = [(1,2,3),[1,2],["a","hit","less"]]
list2 = list1[1]+list1[2]
list3 = list(list1[0])
list3.append(list2)
print(list3)