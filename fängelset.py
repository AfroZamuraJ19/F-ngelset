import random
import os

print("1. Starta spelet")
print("2. Avsluta")
val = input("Vad väljer du? ")
if (val == "1"):
    spelet_körs = True

print("Välkommen till fängelset")
def rum_1(): 
    print("Du är i rum 1.")
    print("Du ser en kista i hörnet av rummet.")
    while True:
        val = input("Vad vill du göra? (1) Öppna kistan, (2) Stanna kvar:")
        if val == "1":
            print("Du öppnar kistan och hittar en nyckel!")
            print("Nyckeln passar till cellens dörr. Du går ut")
            break
        elif val == "2":
            print("Dörren är låst,men du ser inget annat att göra.")
        else:
            print("Ogiltigt val. Försök igen.")

# Rum 2: Grottan och trollet
def rum_2():
    print("Du är i rum 2")
    print("Du går in i en mörk grotta. Plötsligt står ett stort troll framför dig!")
    while True:
        val = input("Vad vill du göra? (1) Slåss med trollet, (2) Försök smyga förbi: ")
        if val == "1":
            print("Du har valt att slåss med trollet.")
            strid_med_troll()
            break
        elif val == "2":
            print("Du försöker smyga förbi trollet...")
            if random.random() > 0.5:  # 50% chans att lyckas
                print("Du smyger förbi trollet och slipper strid.")
                break
            else:
                print("Trollet ser dig och anfaller!")
                strid_med_troll()
                break
        else:
            print("Ogiltigt val. Försök igen.")


# Stridssystem för trollet
def strid_med_troll():
    spelar_hp = 20
    troll_hp = 15
    while spelar_hp > 0 and troll_hp > 0:
        print(f"Ditt HP: {spelar_hp} | Trollens HP: {troll_hp}")
        val = input("Vad vill du göra? (1) Attackera, (2) Försvara: ")
        if val == "1":
            skada = random.randint(3, 6)
            troll_hp -= skada
            print(f"Du attackerar trollet och gör {skada} skada!")
        elif val == "2":
            skada = random.randint(0, 3)
            spelar_hp -= skada
            print(f"Du försvarar dig och tar {skada} skada!")
        else:
            print("Ogiltigt val. Trollet attackerar dig!")
            skada = random.randint(2, 5)
            spelar_hp -= skada
        
        if troll_hp <= 0:
            print("Du besegrade trollet!")
            print("Felsökning pågår... ")
            rum_3()
            break
        if spelar_hp <= 0:
            print("Trollet besegrade dig...")
            global spelet_körs
            spelet_körs = False
            return 
    
# Rum 3: Vägval - Friheten eller stupet
def rum_3():
    print("Du är i rum 3.")
    print("Nu står du vid en vägkorsning. Det finns två vägar.")
    while True:
        val = input("Vilken väg vill du ta? (1) Höger mot friheten, (2) Vänster mot stupet: ")
        if val == "1":
            rum_frihet()
            break
        elif val == "2":
            rum_stup()
            break
        else:
            print("Ogiltigt val. Försök igen.")

# Rum 4: Friheten
def rum_frihet():
    print("Du tar vägen mot friheten och ser ljuset i fjärran!")
    print("Grattis, du har flytt fängelset och är fri!")
    global spelet_körs
    spelet_körs = False
    

# Rum 5: Stupet
def rum_stup():
    print("\nDu går vänster och plötsligt står du vid kanten av ett stup!")
    print("Du håller på att falla...")
    while True:
        val = input("Vad vill du göra? (1) Försöka klättra tillbaka, (2) Fortsätta framåt: ")
        if val == "1":
            if random.random() > 0.3:  # 70% chans att klara det
                print("Du lyckas klättra tillbaka till grottan.")
                rum_2()
                break
            else:
                print("Du misslyckas och faller ner i stupet. Spelet är över.")
                global spelet_körs
                spelet_körs = False
                break
        elif val == "2":
            print("Du går framåt och faller ner i stupet. Spelet är över.")
            global spelet_körs
            spelet_körs = False
            break
        else:
            print("Ogiltigt val. Försök igen.")

# Rum 6: Återuppbyggd väg
def rum_6():
    print("Du hittar en bortglömd passage som leder till en ny väg.")
    print("Det verkar vara en gammal tunnel som leder till en annan del av fängelset.")
    print("Vad vill du göra?")
    while True:
        val = input("(1) Utforska tunneln, (2) Gå tillbaka: ")
        if val == "1":
            print("Tunneln leder till en annan fängelsecell där du hittar ett hemligt utgångsställe!")
            rum_frihet()
            break
        elif val == "2":
            print("Du går tillbaka till grottan för att ta den andra vägen.")
            rum_2()
            break
        else:
            print("Ogiltigt val. Försök igen.")



while (spelet_körs == True):
    rum_1()
    rum_2()
    exit()


# 1. Programmera rum 1 som är cellen. Pussel hitta en nyckel i en kista.
# 2. Programmera rum 2 som är grotta. Spelaren möter ett troll. Två vägar ut ur grottan. Ett till friheten en dålig väg.
# 3. Programmera vad som händer om spelaren väljer friheten, en avslutningstext.
# 4. Programmera den dåliga vägen. Spelaren håller på att trilla ner i ett stup (någon slags spelmekanik för detta). Kan göra val att gå tillbaka om den överlever.

# 5. Programmera ett stridssytem för striden med trollet
