###############################################################################################
ml=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4,4,4,4]
my_list = ml+ml
lis = []
l1=[]
s = my_list[0]
for i in range(1,len(my_list)/2+1):
    print(my_list[i])
    if my_list[i-1] == s:
        l1.append(s)
    else:
        s = my_list[i+1]
        if l1 != []:
            lis.append(l1)
        l1 = []
        lis.append([my_list[i-1]])
if my_list[-1]==my_list[-2]==my_list[-3]:
    lis.append(my_list[len(my_list)-3::])
if my_list[-1] == my_list[-2]!=my_list[-3]:
    lis.append(my_list[len(my_list)-2::])
print(lis)
# OUTPUT [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]] ###############
