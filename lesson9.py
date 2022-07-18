list1 = {'olma':'', 'nok':'', 'uzum':'', 'bodom':''}
lugat1 = {'olma': 'oq', 'nok': 'sariq', 'bodom': 'yashil'}
lugat10 = ['olma', 'oq', 'nok', 'sariq', 'bodom', 'yashil']

# for rang in list1:
#     if rang in lugat1:
#         print(lugat1[rang])

# # print(list1, '=', lugat1)
def sss(ls):
    sumString = ""
    for i in ls:
        sumString+= f"{i}, "
    print(sumString)

sss(lugat10)