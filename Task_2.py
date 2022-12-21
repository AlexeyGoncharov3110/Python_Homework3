size=int(input('Введите размер списка : '))
my_list=[]
sum=0
for i in range(size):
    i=int(input('Введите элементы списка : '))
    my_list.append(i)
print(my_list)
my_list2=[]
for i in range(len(my_list)-int(size/2)):
   my_list2.append(my_list[i]*my_list[len(my_list)-1-i])
print(my_list2)