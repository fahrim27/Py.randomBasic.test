#scope variabel lokal

nama_kucing = 'chaky'
makanan_kucing = 'pindang'

print('SCOPE VARIABEL LOKAL:')

def rubahNamaKucing(namaBaru):
    nama_kucing = namaBaru
    print('nama baru kucing saya adalah', nama_kucing)

rubahNamaKucing('choky')
print('nama kucing saya sekarang adalah', nama_kucing)
print(80*'+')

#scope variabel global
print('SCOPE VARIABEL GLOBAL:')

def namaKucingBaru(newName):
    global nama_kucing
    nama_kucing = newName
    print('nama baru kucing saya adalah', nama_kucing)

def kasihMakanKucing(makanan,nama):
    global nama_kucing,makanan_kucing
    nama_kucing = nama
    makanan_kucing = makanan

namaKucingBaru('unyil')
kasihMakanKucing('ikan','ucrit')
print('nama kucing saya sekarang adalah', nama_kucing,'dan makanannya', makanan_kucing)
print(80*'=')