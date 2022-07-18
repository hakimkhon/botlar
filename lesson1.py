import numpy
# O'zgaruvchini qiymatini uzgartirish mumkin
yosh = "Hozirda mening yoshim {} da 3 yildan keyin esa {} bo'ladi"
# a = int(input("Yoshingizni kiriting: "))
# print(yosh.format(a, a+3))

b = ['lada', 'damas', 'labo', 'nexia', 'matiz']
# b.append('tiko')
# b.insert(2, 'damas')
# print(len(b))

# print(b)
# b.sort()
# print(b)

# for i in b:
#     print(i, " ")
sonlar = list(range(100))
juft = sonlar[10: 90: 2]
urtasi = len(juft)
soni = 10
# sdf= tuple
print(juft)
print(juft[int(urtasi/2-soni/2): int(urtasi/2+soni/2)])