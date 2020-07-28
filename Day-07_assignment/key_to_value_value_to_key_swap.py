port1 = {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"}

port2 = dict([(value, key) for key, value in port1.items()]) 
	

print ("Original dictionary is : ") 
print(port1) 

print() 


print ("Dictionary after swapping is : ") 
print("keys: values") 
for i in port2: 
	print(i, " : ", port2[i]) 
