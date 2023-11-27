import random


class Karakter:
    def __init__(self, can, sp):
        self.can = can
        self.sp = sp
        return


savascı = Karakter(100, random.randint(0, 10))
okcu = Karakter(75, random.randint(0, 20))
buyucu = Karakter(80, random.randint(5, 15))

dusman = Karakter(100, random.randint(0, 15))

oyuncu = input("bir sayı seç \n 1.savaşçı \n 2.okçu \n 3.büyücü \n")

if oyuncu == "1":
    oyuncu = savascı
elif oyuncu == "2":
    oyuncu = okcu
elif oyuncu == "3":
    oyuncu = buyucu
else:
    oyuncu = savascı



oyuncu_tur = 0
Dusman_tur = 0

S = 0
print("başlamak için ve saldırmak için h tuşuna, çıkmak için k tuşuna bas")
while dusman.can >= 0 and oyuncu.can >= 0:
    if oyuncu.can <= 0:
        break
    else:
        if oyuncu_tur <= Dusman_tur:
            S = input()
            if S == "h":
                dusman.can = dusman.can - dusman.sp
            print("Düşmanın canı", dusman.can)
            if S == "k":
                dusman.can = dusman.can - 100
            S = 0
            oyuncu_tur = oyuncu_tur + 1
        else:
            oyuncu.can = oyuncu.can - dusman.sp
            print("senin canın", oyuncu.can)
            Dusman_tur = Dusman_tur + 1
