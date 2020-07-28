List1 = [1,2,3,4,5,7,8] 
List2 = ["a","b","c","d","e","f","g"] 

res = {List1[i]: List2[i] for i in range(len(List1))} 

print ("Resultant dictionary is : " + str(res)) 
