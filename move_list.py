barang = ['celana','baju','daleman','kaos','kemeja']
print(barang)

#manipulasi list
#menambah list
barang.append('boxer')
print(barang)

barang.extend('sepatu')
print(barang)

barang.insert(3,'kaos kaki')
print(barang)

#menghitung anggota list
jumlahBarang = barang.count('daleman')
print('jumlah daleman adalah',jumlahBarang)

#menghapus data list
barang.remove('boxer')
print(barang)

barang.reverse()
print(barang)

print(80*'=')

baru = barang.copy()
baru.append('kolor')
print('barang baru: ',baru)
print('barang lama: ',barang)