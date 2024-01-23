
first_sym = ''
for i in range(ord('A'), ord('Z')+1):
    first_sym += chr(i)
for i in range(ord('А'), ord('Я')+1):
    first_sym += chr(i)
first_sym += 'Ё'

other_sym = first_sym.lower() + '-'


def check_name(name):
    if name[0] not in first_sym:
        return False
    for sym in name[1:]:
        if sym not in other_sym:
            return False
    return True


name = input('Enter your name>')
if check_name(name):
    print(f'{name} is valid name')
else:
    print(f'{name} is invalid name')


