no = [1,2,3,4,5,6,7,8]

sub1 = no [0]
sub2 = no [1]

sub3 = no [-3]
sub4 = no [-5]

#memotong list
sub5 = no [1:5]
sub6 = no [:4]
sub7 = no [-4:]

print (sub5, sub6, sub7)

#menambah list
no2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
sum1 = no + no2

#a = data[:] //titik dua digunakan agar data tidak asosiatif

print (sum1)
print ("\n")
#merubah isi list
print ("list awal", no)
no[2:5] = [10,100,1000]
print ("list setelah dirubah", no)
print("\n")


#list dalam list
x = [no, no2]
y = x[0][5] #mengakses nilai komponen pada list multidimensi [list_number] [komponen_number]
print(x)
print(y)
print("\n")

#method pada list
no.append(50) #menyisipkan data pada list terakhir
print(no)
panjang_list = len(no)
print(panjang_list)
#function pada list
