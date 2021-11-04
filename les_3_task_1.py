"""
В диапазоне натуральных чисел от 2 до 99 определить,
 сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

start_ = 2
stop_ = 99
stop_2 = 9

span = [[i, 0] for i in range(start_, stop_ + 1)]
dev_span = [i for i in range(start_, stop_2 + 1)]
#print(span)
#print(dev_span)

count = 0
for i in range(len(span)):
    for j in range(len(dev_span)):
        if (span[i][0] % dev_span[j]) == 0:
            #print(f'{span[i][0]} кратно числу {dev_span[j]}')
            count += 1
        else:
            continue
    span[i][1] = count
    #print(f'количество кратных чисел = {count}')
    count = 0

for i in range(len(span)):
    print(f'число {span[i][0]} кратно - \t{span[i][1]} раз(а)')