path = 'my_file (1).txt'
mode = 'r'
with open(path, mode)as moj_plik:
   #content1 = moj_plik.read() #przeczyta wszystko
   content2_1 = moj_plik.read(10)  #czytamy 5 pierwszych/kolejnych
   #content2_2 = moj_plik.read(10)
   #content3 = moj_plik.readlines

#print(content1)
#print(type(content1))

print(content2_1)
#print(content2_2)
#print(content3)
#print(type(content3))