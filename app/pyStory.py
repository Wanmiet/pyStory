print("Welcome to some boring story from my past.")
print('\n')
with open('1.txt') as f:
    file_obj = f.read()
print(file_obj)
print('\n')
print('Boring, huh?')
u_i = input('1 - Yes, 2 - No, 3 - Idk ' + '\n')
if u_i == '1':
    print('Sure.')
elif u_i == '2':
    print('Right?')
elif u_i == '3':
    print('K then.')
else:
    print('Ummm...?')
print('\n')
print('Part 2')
print('\n')
with open('2.txt') as f:
    file_obj = f.read()
print(file_obj)
print('\n')
print('Yay?')
u_i = input('1 - Yes, 2 - No, 3 - Idk' + '\n')
if u_i == '1':
    print('Sure.')
elif u_i == '2':
    print('Right?')
elif u_i == '3':
    print('K then.')
else:
    print('Ummm...?')
print('\n')
print('Part 3')
print('\n')
with open('3.txt') as f:
    file_obj = f.read()
print(file_obj)
print('\n')
print('The end?')
print('\n')
u_i = input('1 - Yes, 2 - No, 3 - Idk' + '\n')
if u_i == '1':
    print('Sure.')
elif u_i == '2':
    print('Right?')
elif u_i == '3':
    print('K then.')
else:
    print('Ummm...?')