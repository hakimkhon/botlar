from lesson9 import sss


mevalar = ['olma', 'behi', 'qovun', 'shaftoli', 'anjir']
yangi_meva = mevalar[:]
yangi_meva2 = mevalar
mevalar.append('bodom')
sortMeva = sorted(mevalar, reverse=True)
sortMeva.sort()
# print(sortMeva)
# print(yangi_meva)
# print(yangi_meva2)

ali = []

ali.append('olma')
print(sss(ali))
ali.clear()
print(sss(ali))

def sss(ls):
    sumString = ""
    for i in ls:
        sumString+= f"{i} "
    return sumString