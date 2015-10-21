def anahtarAlfabe(s):
    alfabe = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    anahtar = ['']*24
    for n in range(0, 24):
        anahtar[((n+s-1) % 24)] = alfabe[n]
    dictAnahtar = dict(zip(alfabe, anahtar))
    #print (dictAnahtar)
    return dictAnahtar

s = raw_input("anahtar alfabe olusturmak icin s parametresi girin\ns: ");
key = anahtarAlfabe(int(s))

f = open("metin.txt", "r")
metin = f.read()
print (metin)
metin = metin.lower()
crypted = ''
str = ''
str = key[metin[0]]
crypted = str.upper()
for n in range(1, len(metin)):
    if metin[n] in key:
        str = key[metin[n]]
        crypted += str.upper()
    else:
        crypted += metin[n].upper()
print (crypted)
f.close()
fC = open("crypted.txt", "w")
fC.write(crypted)
fC.close()
