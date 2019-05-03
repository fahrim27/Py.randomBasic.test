
namaKucing = ['chaky', 'choky', 'unyil', 'ucrit']
warnaKucing = ['hitam', 'putih', 'orange', 'kuning']

i = 1
for kucing in namaKucing:
    print(i,kucing)
    i += 1
print(80*'=')


for j,kucing in enumerate(namaKucing):
    print(j,':',kucing)

print(80*'+')


for kucing,warna in zip(namaKucing,warnaKucing):
    print(kucing,'mempunyai warna',warna)

print(80*'=')

sifatKucing = {'lucu', 'menarik', 'menggemaskan', 'melucu', 'gila'}

for sifat in sorted(sifatKucing):
    print(sifat)

print(80*'=')

#dictionary

nama_kucing = {'chaky':'lucu', 'choky':'menggemaskan', 'unyil':'melucu', 'ucrit':'gila',}

for z,p in nama_kucing.items(): #{keys,values}
    print(z,p)

for i in reversed(range(1,5)):
    print(i)