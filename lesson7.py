countries = {
    'Uzbekistan': 'Tashkent',
    'Turkiye': 'Ankara',
    'Zimbabwe': 'Harare',
    'Vietnam': 'Hanoi',    'Yemen': 'Sana\'a',    'Wales': 'Cardiff',    'Venezuela': 'Caracas',
    'Vatican': 'Vatican',    'Vanuatu': 'Port Vila',    'Ukraine': 'Kiev',    'United Kingdom': 'London',
}
while True:
    state = input('Davlarni kiriting: ')

    if not state in countries:
        capital = input(f'{state} davlati poytaxti bizni bazada yo\'q, bilsangiz kiriting: ')
        new_country = {state: capital}
        countries.update(new_country)

    elif state in countries:
        print(f'{state} davlati poytaxti {countries[state]}')


# vazifa 2
# taomnoma = {
#     'osh': 15000,
#     'shurva': 12000,
#     'mastava': 9500,
#     'qotirma': 18000,
#     'shashlik': 11000,
#     'lagman': 13000,
#     'borj': 11000,
#     'mampar': 13000,
# }
# soni = int(input('ovqatlarni sonini kiriting: '))
# tanlangan = []
# for i in range(soni):
#     taom = input(f'{i+1} - taomni kiriting: ')
#     tanlangan.append(taom)
# summa = 0
# for mahsulot in taomnoma:
#     if mahsulot in tanlangan:
#         summa += taomnoma[mahsulot]
#         print(f"{mahsulot.title()} {taomnoma[mahsulot]} so'm")
# for yuqlari in tanlangan:
#     if yuqlari not in taomnoma:
#         print(f"Kechirasiz bizda {yuqlari.title()} yo'q edi")
# print(f'sizdan jami {summa} so\'m ')