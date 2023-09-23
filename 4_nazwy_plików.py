import datetime
import time
def mnozenie(a, b, c):
    return round(a * b * c)

print(mnozenie(a=23, b=3.3, c=1))


for i in range (10):
    now = datetime.datetime.now()
    moja_nazwa = now.strftime('report%H%M%S.txt')
    print('moja nazwa to', moja_nazwa)
    time.sleep(2)

