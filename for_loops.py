nilai_ku = ['10','100','1000','10000','100000']

for i in nilai_ku:
    print(i)
    print(len(i)) #mengakses jumlah kharakter variabel

print(80*"=")

#string sebagai iterasi
fahri = 'fahri muhammad'
for j in fahri:
    print(j)
print(80*"=")

#nasted for
prodi = ['TI','SI','MI','PTI']
jurusan = ['Informatika','Elektro','Mesin','Sipil','PKK']

daftar_studi = [prodi,jurusan]

for subDaftarStudi in daftar_studi:
    print(subDaftarStudi)
    for char in subDaftarStudi:
        print(char)
print(80*"=")