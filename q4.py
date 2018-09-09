a = [5,7,9,3,2,1,4,2,6,3,0,9,8]
num = int(input("Choose a number: "))
new_list = []
for i in a:
	if i < num:
		new_list.append(i)
print (new_list)
