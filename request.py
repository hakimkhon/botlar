import requests
from bs4 import BeautifulSoup
manzil = 'https://namozvaqtlari.com/namoz/11-namangan-namoz-vaqtlari-bugungi-namoz-vaqti.html'
r = requests.get(manzil)
s = BeautifulSoup(r.text, 'html.parser')
t = s.find_all(class_ = 'info')
print(t[0].text)
print(t[1].text)

# print(t[2].text)
# print(t[3].text)
# print(t[4].text)
# print(t[5].text)

# manzil = 'https://uz.islamery.com/uz/fergana/fergana'
# r = requests.get(manzil)
# s = BeautifulSoup(r.text, 'html.parser')
# t = s.find_all("h6", {"class": "my-1"})
# print(t[0])
