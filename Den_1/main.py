import random as rd

print("saldırmak için h tuşuna bas\n çıkmak için k tuşuna bas")
saldiri = rd.randint(0, 10)
oyuncu_can = 100

Dusman_can = 100
Dusman_saldırı = rd.randint(0, 15)

oyuncu_tur = 0
Dusman_tur = 0

S = 0
while Dusman_can >= 0 and oyuncu_can >= 0:
    if oyuncu_can <= 0:
        break
    else:
        S = input()
        if oyuncu_tur <= Dusman_tur:
            if S == "h":
                Dusman_can = Dusman_can - saldiri
            print("Düşmanın canı", Dusman_can)
            if S == "k":
                Dusman_can = Dusman_can - 100
            S = 0
            oyuncu_tur = oyuncu_tur + 1
        else:
            oyuncu_can = oyuncu_can - Dusman_saldırı
            print("senin canın", oyuncu_can)
            Dusman_tur = Dusman_tur + 1
