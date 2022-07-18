# sonlar = list(range(1200))
# juft = sonlar[120: 1200: 2]
# print('1-topshiriq: \njuft sonlar',juft)
# print('2-topshiriq: \nyig\'indi', sum(juft))
# print('3-topshiriq: \nmax-min',(max(juft)-min(juft)))
# soni = len(juft)
# print('4-topshiriq: \nelementlar soni', soni)
# first = juft[:20]
# midle = juft[int(soni/2-20/2): int(soni/2+20/2)]
# last = juft[-20:]
# last.reverse()
# print('5-topshiriq:','\nboshidagi 20 tasi:', first, '\noxiridagi 20 tasi:', last, '\nurtasidagi 20 tasi:', midle )

taomlar = ['osh', 'manti', 'shurva', 'chuchvara', 'mastava']
print(taomlar)
nonushta = taomlar.copy()
nonushta.remove('manti')
nonushta.remove('chuchvara')
nonushta.remove('shurva')
nonushta.append('sut')
nonushta.append('qaymoq')
print(nonushta)
