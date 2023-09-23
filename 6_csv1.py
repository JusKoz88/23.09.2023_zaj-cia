mode = 'r'
path = 'rozliczenie.csv'
with open(path,mode) as moj_plik:
  content = moj_plik.readlines()
print(content)

for i in range (len(content)):
    content[i] = content[i].split(',')

print(content)
print(content[3])
print(content[3][2])   # pierwszy index - wiersz, drugi index - kolumna
print(content[0][2][3:-2]) #3ci indeks, znaki stringa

#przykład replace
#slowo = 'zosia.franek'
#slowo = slowo.replace(__old='a', __new='A')
#print(slowo)

#przykład split
#slowo = 'zosia.franek'
#slowo = slowo.split(' . ')
#print(slowo)
