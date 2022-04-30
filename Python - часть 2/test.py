num = int(input('Enter a number: '))

hex = ''

while(num > 0):
    remainder = num % 16
    hex = hex_dict[remainder] + hex
    num = num // 16

print(f'Hexadecimal: {hex}')