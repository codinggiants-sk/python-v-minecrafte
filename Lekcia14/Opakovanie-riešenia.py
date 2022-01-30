#IDLE
# Zadanie 1
# Vytvorte premenné, do ktorých uložíte vaše meno (text), vek (číslo), obľúbené jedlo (text), obľúbená hra (text).
# Vypíšte text pomocou funkcie print(). Použite premenné, ktoré ste vytvorili.
# Príklad:
# Volám sa Adam, mám 15 rokov, moje obľúbené jedlo je pizza a moja obľúbená hra je Minecraft.
# Nezabudnite previesť číslo na text, použite funkciu str (). Na kombinovanie textu s premennými použite znak +.

meno="Adam"
vek=15
oblubeneJedlo="pizza"
oblubenaHra="Minecraft"

print("Volám sa "+meno+", mám "+str(vek)+" rokov, moje obľúbené jedlo je "+oblubeneJedlo+
" a moja obľúbená hra je "+ oblubenaHra)

# Zadanie 2
# Napíšte program, ktorý umožní používateľovi zadať známky z troch predmetov a zobraziť ich priemer.
# Na získanie údajov od používateľa použite funkciu input(). Pamätajte, že táto funkcia berie údaje ako text, zatiaľ čo my na vypočítanie priemeru
# potrebujeme číslo. Takže napríklad potrebujeme číslo 5, a nie text "5", pretože 5 + 5 = 10 a "5" + "5" = "55". Nakonverziu na číslo použite funkciu int().
# napr. int(input("zadaj známku z anglického jazyka: "))
# Priemer vypočítate tak, že sčítate všetky známky a vydelíte ich počtom (znamienko delenia je /).


znamkaMatematika=int(input("Zadaj známku z matematiky"))
znamkaInformatika=int(input("Zadaj známku z informatiky"))
znamkaSlovencina=int(input("Zadaj známku zo Slovenčiny"))
priemer=(znamkaMatematika+znamkaInformatika+znamkaSlovencina)/3
print("Tvoj priemer je "+str(priemer))


# Zadanie 3
# Prekladač – vytvorte program, ktorému zadáme 5 slov v Slovenčine a on ich preloží do angličtiny.
# Používateľ zadá slovo v Slovenčine, a potom dostane odpoveď, napr.
# >> Zadajte slovo, ktoré chcete preložiť: tlačidlo
# Tlačidlo v angličtine je button

# Pre slovo, ktorého preklad sme nenaprogramovali, by sa malo zobraziť:
    # "Žiaľ, v našej databáze zatiaľ nemáme preklad tohto slova."
# Použite podmienený príkaz if elif else.
# Aby sa to celé opakovalo do nekonečna, použite cyklus while True
# Pamätajte na odsadenie kódu (kláves tabelátor).

while True: 
    slovo=input("Zadaj slovo, ktoré chceš preložiť")
    if slovo=="cyklus":
        print(slovo+" sa po naglicky povie loop")
    elif slovo=="tlačidlo":
        print(slovo+" sa po naglicky povie button")
    elif slovo=="premenná":
        print(slovo+" sa po naglicky povie variable")
    elif slovo=="popisok":
        print(slovo+" sa po naglicky povie label")
    elif slovo=="výsledok":
        print(slovo+" sa po naglicky povie result")
    else:
        print("Žiaľ, v našej databáze zatiaľ nemáme preklad tohto slova.")


# Zadanie 4
# Vytvorte cyklus for, ktorý vypíše čísla od -10 do 100.
# Použi funkciu range().

for i in range(-10,101):
    print(i)


# Zadanie 5*
# Vytvor pole s názvom poleCisel a ulož do neho ľubovoľných 5 čísel.
# Pomocou cyklu prejdi každý prvok tohto poľa a vypíš jeho druhú mocninu.
# Príklad:
# Pre číslo 2 vypíšte "2 na druhú je 4"
# Pre číslo 5 "5 na druhú je 25"
# Použi funkciu len(), ktorá vráti dĺžku poľa
# Na výber daného prvku z poľa použite premennú cyklu for.

poleCisel=[2,5,6,8]

for i in range(len(poleCisel)):
    print(str(poleCisel[i])+" na druhú je "+str(poleCisel[i]*poleCisel[i]))

#alebo

##for i in poleCisel:
    ##    print(str(i)+" na druhú je "+str(i*i))
