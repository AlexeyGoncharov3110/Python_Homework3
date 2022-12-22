number=int(input('Введите неотрицательно десятичное число: '))
if number<0:
    print('Не корректно введенны данные , повторите ввод')
bin=''
num=number
while number>0:
    bin=str(number%2)+bin
    number//=2
print(f'Число {num} , в десятичной системе равно {bin} в двоичной.') 

