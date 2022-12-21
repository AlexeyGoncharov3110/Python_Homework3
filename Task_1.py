size=int(input('Введите размер списка : '))
my_list=[]
sum=0
for i in range(size):
    i=int(input('Введите элементы списка : '))
    my_list.append(i)
print(my_list)    
for i in range(1,len(my_list),2):
    sum+=my_list[i]
print(sum)