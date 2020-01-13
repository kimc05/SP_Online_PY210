
tups = (2, 123.4567, 10000, 12345.67)

print("--- Task01 ---")
print('file_{:03d} :    {:.2f}, {:.2e}, {:.2e}'.format(tups[0], tups[1], tups[2], tups[3]))

print("\n" + "--- Task02 ---")
print(f'file_{tups[0]:03d} :    {tups[1]:.2f}, {tups[2]:.2e}, {tups[3]:.2e}')

print("\n" + "--- Task03 ---")
print("enter numbers into function 'formatter()'")
def formatter(in_tuple):
    form_string = 'the ' + str(len(in_tuple)) + ' numbers are: {:d}'
    for t in range(len(in_tuple)-1):
        form_string += ', {:d}'
    return form_string.format(*in_tuple)

print("\n" + "--- Task04 ---")
taskfour = (4, 30, 2017, 2, 27)
print(taskfour)
print('{3:02d}, {4:02d}, {2:02d}, {0:02d}, {1:02d}'.format(*taskfour))

print("\n" + "--- Task05 ---")
t = ['oranges', 1.3, 'lemons', 1.1]
print(f'The weight of an {t[0][:-1]} is {t[1]} and the weight of a {t[2][:-1]} is {t[3]}.')
print(f'The weight of an {t[0][:-1].upper()} is {t[1]*1.2} and the weight of a {t[2][:-1].upper()} is {t[3]*1.2}.')

print("\n" + "--- Task06 ---")
print('{:<15}{:<10}{:<9}'.format('name', 'age', 'cost'))
print('{:<15}{:<10}{:<7.2f}'.format('Sylvester', 49, 584.84))
print('{:<15}{:<10}{:<7.2f}'.format('Forest', 6, 435537.9145))
print('{:<15}{:<10}{:<7.2f}'.format('Park Bench', 34, 3814.11))

print("\n" + "--- Task06_extra_task ---")
tups = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(('{:<5}' * len(tups)).format(*tups))
