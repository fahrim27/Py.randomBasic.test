angka = 0

while angka < 5:
    print(angka)
    angka += 1

start = True

while start:
    print('Proses perulangan')
    if angka is 50:
        start = False
        print('angka 50 ditemukan')
    angka += 1

print(80*"=")
print("\n")



#function in python
#definisi fungsi
def kucing_lucu():
    print('kucing lucu adalah chaky')

def suara_kucing():
    kucing_lucu()
    print("meow meow meow")

#memanggil fungsi
suara_kucing()
print(80*"=")

#fungsi dengan input argumen
def jumlahtotalkucing(x):
    jumlah = 10
    jumlahTotal = x*jumlah
    print('jumlah total kucing adalah',jumlahTotal)

jumlahtotalkucing(5)