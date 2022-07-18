bozorlik = []
soni = int(input('nechta mahsulot olmoqchisiz? '))
for n in range(soni):
    maxsulot = input(f'{n+1} - maxsulotni kiriting: ')
    while bozorlik.count(maxsulot) > 0:
        maxsulot = input(f'{maxsulot} maxsuloti bor boshqa kiriting: ')
    bozorlik.append(maxsulot)
print(bozorlik)

# bozorlik = ['olma', 'nok', 'uzum', 'non']
# maxsulot = input('maxsulotni kiriting: ')
# print(bozorlik.count(maxsulot))