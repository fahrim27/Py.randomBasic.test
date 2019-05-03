angka = 50

for i in range(10,100,5): #(awal,akhir,increments)
    print(i)

    if i is angka:
        print("angka ditemukan",i)
        break #interupsi untuk keluar dari looping
else:
    print('angka',angka, 'tidak ditemukan')
print(80*"=")
print("\n")


#continue and pass

for i in range(1,10):

    if i is 6:
        print('nilai i adalah',6)
        continue
        # pass : nilai kosong dapat digunakan sebagai dummy

    print("di dalam nilai adalah",i)
else:
    print("akhir perulangan")