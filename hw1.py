def bolunenSayiBulma(min_sayi, max_sayi, bolunecek_sayi):
    tamBolunenler = []
    sayiAraligi = 0

    for x in range(min_sayi, max_sayi):
        sayiAraligi += 1

        if x % bolunecek_sayi == 0:
            tamBolunenler.append(x)

    print(tamBolunenler)

    toplam_sayi = len(tamBolunenler)

    return toplam_sayi, sayiAraligi


print(bolunenSayiBulma(3, 20, 3))
