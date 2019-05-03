import sys
import timeit

angka1 = [1,2,3,4,5,6,7,8,9]

#tuple (anggota data fix, tidak bisa di otak-atik)
#hanya bisa menggunakan perintah count dan index
#dta tuple lebih kecil size memorinya dibanding list, sehingga mudah di akses
angka2 = (10,20,30,40,50,60,70,80,90)

print(type(angka1))
print(type(angka2))
print(80*'=')


besar_angka1 = sys.getsizeof (angka1)
besar_angka2 = sys.getsizeof (angka2)

print('besar data angka1 = ', besar_angka1)
print('besar data angka2 = ', besar_angka2)

print(80*'=')

data_list = timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9]",number=1000000)
data_tuple = timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9)",number=1000000)

print('waktu akses data list = ', data_list)
print('waktu akses data tuple = ', data_tuple)
print(80*'=')
print('\n')



#tipe data set (himpunan)
#data yang sama akan ditampilkan sebagai satu kesatuan
#data set urutannya acak

kucing = {'chaky',
          'choky',
          'unyil',
          'ucrit',
          'lucu'}

print(kucing)

kucing2 = set()
kucing2.add('aaaaaaa')
kucing2.add('bbbbbbbbbbb')
kucing2.add('ccccccccccccccccc')

print(sorted(kucing2))

number = {1,2,3,4,5,6,7,8,9,10}
genap = {2,4,6,8,10}
ganjil = {1,3,5,7,9}

print(ganjil.union(genap))
print(genap.intersection(number))
print(80*'=')
print('\n')




#tipe data dictionary

mhs = {'Nama':'Fahri Muhammad',
       'NIM':29,
       'Jurusan':'Informatika',
       'Fakultas':'Teknik',
       'Instansi':'UNESA'} #{key:value, . . . . . .}

mhs2 = {'Nama':'Hafizh',
        'NIM':28,
        'Jurusan':'Informatika',
        'Fakultas':'Teknik',
        'Instansi':'UNESA'}

print(mhs)
print(mhs.keys())
print(mhs.values())
print(mhs.items())
print(mhs['Nama'])
print(80*'+')


mhsList = {29:mhs,28:mhs2}
print(mhsList[29])