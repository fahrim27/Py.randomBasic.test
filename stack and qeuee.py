#stack(tumpukan) pada python
tumpukan = [1,2,3,4,5,6,7,8,9,10]
print('data = ',tumpukan)

tumpukan.append(11)
print('data masuk = ',11)
print('data = ',tumpukan)
tumpukan.append(12)
print('data masuk = ',12)
print('data = ',tumpukan)

keluar = tumpukan.pop()
print('data keluar = ',keluar)
print('data baru = ',tumpukan)

keluar = tumpukan.pop()
print('data keluar = ',keluar)
print('data baru = ',tumpukan)

print(80*'=')



#antrian di python

from collections import deque

antrian = deque([1,2,3,4,5,6,7,8,9])

print('data = ',antrian)

antrian.append(10)
print('data masuk = ',10)
print('data = ',antrian)

antrian.append(11)
print('data masuk = ',11)
print('data = ',antrian)

#mengurangi antrian
out = antrian.popleft()
print('data keluar = ',out)
print('data sekarang = ',antrian)

out = antrian.popleft()
print('data keluar = ',out)
print('data sekarang = ',antrian)