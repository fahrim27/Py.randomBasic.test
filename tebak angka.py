#tebak angka

import random

def main():
    print('program tebak angka yang sangat absurd')
    print(80*'=')

    angka = random.randint(1,100)

    skor = 100

    ketemu = False

    while not ketemu:
        tebak = input('masukkan angka tebakanmu = ')
        tebak = int(tebak)

        if tebak is angka:
            print('tebakan anda benar')
            ketemu = True
        elif tebak > angka:
            print('angka yang anda masukkan terlalu besar')
            skor -= 2
        else:
            print('angka yang anda masukkan terlalu kecl')
            skor -= 2

        print(80*'+')
        print('skor anda adalah =',skor)
        print(80*'=')
        print('Terima kasih telah menjadi uji caba kami')

if __name__ == "__main__":
    main()