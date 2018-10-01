dic = { '1.2' : [1,2,3] , '2.2' : [4,5,6] , '3.3' :[7,8,9]}
new_dic = {}
for key,lis in dic.items():
    new_dic[key] = sum(lis)
print(new_dic)