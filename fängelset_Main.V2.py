import random
import os


print("1. Starta spelet")
print("2. Avsluta")
val = input("Vad vill du göra?")
if (val == "1"):
    spelet_körs = True

# Rum 1: Cellen
print("Välkommen till fängelset")
def rum_1(): 
    tid_kvar = 0
    print("Du är i rum 1.")
    print("Du ser en kista i hörnet av rummet.")
    while True:
        val = input("Vad vill du göra? (1) Öppna kistan, (2) Stanna kvar:")
        if val == "1":
            print("Du öppnar kistan och hittar en nyckel!")
            print("Nyckeln passar till cellens dörr. Du går ut")
            break
        elif val == "2":
            print("Dörren är låst, men du ser inget annat att göra.")
            tid_kvar = tid_kvar + 1
            if (tid_kvar >= 3):
                print("Du har stannat för länge i cellen och dör av hunger. Spelet är över.")
                exit()
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
            print("Trollet ser dig och anfaller!")
            strid_med_troll()
            break
        else:
            print("Ogiltigt val. Försök igen.")


# Stridssystem för trollet
def strid_med_troll():
    spelar_hp = 20
    troll_hp = 25
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
            print("Du besegrade trollet och fick en magisk amulett!")
            rum_3()
            break
        if spelar_hp <= 0:
            print("Trollet besegrade dig...")
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
    print("Du är i rum 4.")
    print("Du tar vägen mot friheten och ser ljuset i fjärran!")
    print("Grattis, du har flytt fängelset och är fri!")
    

# Rum 5: Stupet
def rum_stup():
    print("Du är i rum 5.")
    print("Du går vänster och plötsligt står du vid kanten av ett stup!")
    print("Du håller på att falla...")
    while True:
        val = input("Vad vill du göra? (1) Försöka klättra tillbaka, (2) Fortsätta framåt mot avgrunden:")
        if val == "1":
            if random.random() > 0.3:  # 50% chans att klara det
                print("Du lyckas klättra tillbaka till grottan.")
                rum_3()
                break
            else:
                print("Du misslyckas, faller ner i stupet och förlorar amuletten. Spelet är över.")
                break
        elif val == "2":
            print("Du går framåt, faller ner i stupet och förlorar amuletten. Spelet är över.")
            break
        else:
            print("Ogiltigt val. Försök igen.")





while (spelet_körs == True):
    rum_1()
    rum_2()
    
    exit()




