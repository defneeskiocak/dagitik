def anahtarAlfabe(s):
    alfabe = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    anahtar = ['']*24
    for n in range(0, 24):
        anahtar[((n+s-1) % 24)] = alfabe[n]
    print (anahtar)

anahtarAlfabe(7)
