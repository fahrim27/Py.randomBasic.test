#return value pada python

def kuadrat(x):
    total = x**2
    print('nilai kuadrat dari',x,'adalah = ',total)
    return total

print(kuadrat(5))
print(80*"=")

#fungsi return value dengan multiple argumen

def nilai(x,y):
    total = x + y
    print(x,'+',y,'=',total)
    return total

def perkalian(i,j):
    hasil = i * j
    print(i,'*',j,'=')
    return hasil

print(nilai(x=10,y=100))
print(20*'+')
print(perkalian(10,nilai(x=10,y=100)))
print(80*'=')
print("\n")



#fungsi lamba pada python
def jumlah(a,b):
    c = a+b
    return c

kali = lambda x,y: x*y
print(kali(3,4))