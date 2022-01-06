def sayiAtama():
    number = int(input("enter a 2-digit value:"))

    if number > 9 and number < 100:
        sayiOkunusu(number)
    else:
        print("i told you to enter a two-digit value")

def sayiOkunusu(number):
    onedigit = {1: "bir", 2: "iki", 3: "üç", 4: "dört",
                5: "beş", 6: "altı", 7: "yedi", 8: "sekiz",
                9: "dokuz"}

    twodigit = {10: "on", 20: "yirmi", 30: "otuz", 40: "kırk",
                50: "elli", 60: "altmış", 70: "yetmiş", 80: "seksen",
                90: "doksan"}

    stringNumber = str(number)
    birlerBasamagi = int(stringNumber[1])
    onlarBasamagi = int(stringNumber[0] + "0")

    if birlerBasamagi == 0:
        print(twodigit[onlarBasamagi])
    else:
        print(twodigit[onlarBasamagi], onedigit[birlerBasamagi])


sayiAtama()
