import random

isim=input("İsminizi giriniz : ")

print("Hoş geldin "+" "+isim)

while (True):
    print("1-->Kolay(1-10 arası sayı , 5 hak)")

    print("2-->Orta(1-50 arası sayı , 7 hak)")

    print("3-->Zor(1-100 arası sayı , 10 hak)")

    secim=int(input("Lütfen zorluk derecesini seçiniz : "))

    if(secim<1 or secim>3):

        print("Yanlış seçim yaptınız tekrar deneyiniz")

        print(" ")

    else:
        break


if(secim==1):
    tutulan1=random.randint(1,10)

    n=6 ##hak sayısı
    for i in range(1,n):

        tahminEdilenSayı=int(input("TAHMİNİNİZ : "+" "+"("+str(n-i)+" "+"hakkınız kaldı)"))

        

        if(tahminEdilenSayı<tutulan1):

            print("Daha büyük sayı söyle")

            continue

        elif(tahminEdilenSayı>tutulan1):

            print("Daha küçük sayı söyle")

            continue

        else:

            print("TEBRİKLER "+str(i)+". tahminde buldun ")

            print("PUANIN : "+str((n-i)*10))

            break


if(secim==2):
    tutulan2=random.randint(1,50)

    m=8 ##hak sayısı

    for k in range(1,m):

        tahminEdilenSayı=int(input("TAHMİNİNİZ : "+" "+"("+str(m-k)+" "+"hakkınız kaldı)"))

        

        if(tahminEdilenSayı<tutulan2):

            print("Daha büyük bir sayı söyleyiniz")

            continue

        if(tahminEdilenSayı>tutulan2):

            print("Daha küçük bir sayı söyleyiniz")

            continue

        else:

            print("TEBRİKLER"+" "+str(k)+".hamlede buldunuz")

            print("PUANIN : "+str((m-k)*10))

            break

            
if(secim==3):

    tutulan3=random.randint(1,100)

    u=11 ##hak sayısı

    for h in range(1,u):

        tahminEdilenSayı=int(input("TAHMİNİNİZ : "+" "+"("+str(u-h)+" "+"hakkınız kaldı)"))

        

        if(tahminEdilenSayı<tutulan3):

            print("Daha büyük bir sayı söyleyiniz")

            continue

        if(tahminEdilenSayı>tutulan3):

            print("Daha küçük bir sayı söyleyiniz")


        else :

            print("TEBRİKLER"+" "+str(h)+".hamlede buldunuz")

            print("PUANIN : "+str((u-h)*10))

            break




    














     