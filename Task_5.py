n = int(input('Введите число для последовательности Фибоначи :'))
my_list = []
fn1 = 1
fn2 = -1
for i in range(n):
    if i == 0:
        my_list.insert(0, fn1)
    if i == 1:
        my_list.insert(0, fn2)
    if i > 1:
        temp = fn2
        fn2 = fn1-fn2
        fn1 = temp
        my_list.insert(0, fn2)
fp1 = fp2 = 1
my_list.append(0)
for i in range(n):
    if i == 0 or i == 1:
        my_list.append(fp1)
    if i > 1:
        temp1 = fp2
        fp2 = fp1+fp2
        fp1 = temp1
        my_list.append(fp2)
print(my_list)
