def notHesaplama():
    vize1 = int(input('Vize1 Notunuz : '))
    vize1 = notKontrol(vize1)
    vize2 = int(input('Vize2 Notunuz : '))
    vize2 = notKontrol(vize2)
    final = int(input('Final Notunuz : '))
    final = notKontrol(final)
    toplamNot = (float(vize1) * 0.3) + (float(vize2) * 0.3) + (float(final) * 0.4)
    harfNotu(toplamNot)


def harfNotu(ortalama):
    if (ortalama >= 70):
        if (ortalama >= 90):
            print(ortalama, "-----> AA")
        elif (ortalama >= 85):
            print(ortalama, "-----> BA")
        elif (ortalama >= 80):
            print(ortalama, "-----> BB")
        elif (ortalama >= 75):
            print(ortalama, "-----> CB")
        else:
            print(ortalama, "-----> CC")
    else:
        if (ortalama >= 65):
            print(ortalama, "-----> DC")
        elif (ortalama >= 60):
            print(ortalama, "-----> DD")
        elif (ortalama >= 55):
            print(ortalama, "-----> FD")
        else:
            print(ortalama, "-----> FF")


def notKontrol(number):
    if 0 < number < 101:
        return number
    else:
        number = int(input('0-100 arası değer giriniz.'))

        return notKontrol(number)


notHesaplama()
