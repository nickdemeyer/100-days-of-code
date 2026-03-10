#exercise 1: cijferlijst
try:
    invoer = "twaalf"
    getal = int(invoer)
    print(f"Het getal is: {getal}")
except ValueError:
    print("cijfer nodig, niet in letters schrijven!")

#oefening 2: de verboden som
try:
    voornaam = "Python"
    leeftijd = 33
    bericht = "Naam: " + voornaam + " - Leeftijd: " + leeftijd
    print(bericht)
except TypeError:
    print(f"naam: {voornaam} - leeftijd: {leeftijd}")

#oefening 3: verdwenen tekst
try:
    with open("mijn_geheime_wachtwoorden.txt", "r") as bestand:
        inhoud = bestand.read()
        print(inhoud)
except FileNotFoundError: 
    print("Oeps! Dat bestand bestaat niet.")

#oefening 4: final boss
try:
    items = ["appel", "banaan", "kers"]
    index = "0"
    print("Het gekozen item is: " + items[index])
except TypeError:
    print("type een getal!")
except IndexError:
    print("getal is te hoog!")