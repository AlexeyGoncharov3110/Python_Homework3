size=int(input('Введите размер списка : '))
my_list=[]
from decimal import Decimal 
for i in range(size):
    i=Decimal(input('Введите элементы списка : '))
    if i<0:
        i*=(-1)
    my_list.append(i)
min=my_list[0]%1 
max=my_list[0]%1
count=0
while count<size:
    if min ==0:
     min=my_list[count+1]
    else: count+=1      
difference=0
for i in range(len(my_list)):
  if my_list[i]%1!=0 and my_list[i]%1<=min:
    min=my_list[i]%1
  if my_list[i]%1!=0 and my_list[i]%1>=max:
    max=my_list[i]%1
print(max)
print(min) 
if min==max:
    print('Не корректно введенны данные')   
difference=max-min
print(round(difference,4))

