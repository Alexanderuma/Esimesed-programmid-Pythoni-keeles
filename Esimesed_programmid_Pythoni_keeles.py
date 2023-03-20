from math import*


# Ülesanne 1
# Kirjuta programm, mis sind tervitab.
print("Ülesanne 1")
print("Hello Aleksander!")


##****************************************************************************************************************************************************************************
# Ülesanne 2
# Koosta programm on öeldud tehte 3 + 8 / (4 - 2) * 4 vastuse?
# +Kuidas mõjutab sulgude kasutamine/kasutamata jätmine tööd?
# +Katseta erinevaid kombinatsioone paralleelselt ning lisa ka selgitavad tekstid, et väljund oleks arusaadav.

#Variant 1
# Kui jättame nii nagu oli, siis tulemuseks tuleb vastuseks float: 19.0
print()
print()
print("Ülesanne 2")
print("Koosta programm on öeldud tehte 3 + 8 / (4 - 2) * 4 vastuse?")
print("Vastus: ", (3 + 8 / (4 - 2) * 4))

#Variant 2
# Kui paneme lisa sulgud ja lisame int tüübi, siis meil tuleb vastuseks int: 19
print()
print("Variant 2")
print("Kui paneme lisa sulgud ja lisame int tüübi, siis meil tuleb vastuseks int:")
print(int(3 + 8 / (4 - 2) * 4))

#Variant 3
#Kui võtame kõik sulgud ära siis arvutamise järjekord muutub. Ja vastuseks tuleb: -3.0
print()
print("Variant 3")
print("Kui võtame kõik sulgud ära siis arvutamise järjekord muutub. Ja vastuseks tuleb: ")
print(3 + 8 / 4 - 2 * 4)

#Variant 4
# Kui paneme sulged teisele kohale siis arvutamise protsessi järjekord muutub. Vastus ka muutub. vastuseks saame: 22.0
print()
print("Variant 4")
print("Kui paneme sulged teisele kohale siis arvutamise protsessi järjekord muutub. Vastus ka muutub. vastuseks saame: ")
print((3 + 8) / (4 - 2) * 4)


##****************************************************************************************************************************************************************************
#Ülesanne 2.1
#Ruudu sees asub ring. Ringi raadius on 3.
#Leia ja väljasta ekraanile ruudu pindala, ruudu ümbermõõt, ringi pindala, ringi ümbermõõt.
print()
print()
print("Ülesanne 2.1" )
r = 3

a = 2*r

Sruud = a * a
Pruud = 4 * a
Sring = pi*r*r
Cring = 2*pi*r

print("Ruudu pindala on: ", Sruud)
print("Ruudu ümbermõõt on: ", Pruud)
print("Ringi pindala on: ", round(Sring,2))
print("Ringi ümbermõõt on: ",round(Cring,2))

#Ülesanne 2.2
"""
Koosta programm, mis arvutab välja Maa ümbermõõdu ekvaatori kohal 2-eurostes müntides ehk teisisõnu: kui palju 2-euroseid münte tuleb panna üksteise kõrvale, et rida ulatuks ümber Maa. Kasuta teadmist, et Maa raadius ekvaatori kohal on 6378 km.

Algandmed (Maa raadius, mündi läbimõõt jne) omista programmi alguses sisukate nimedega muutujatele. Kuna ümbermõõdu arvutamiseks tuleb kasutada  PI-d (3,14...), siis võid selle (umbkaudse) väärtuse otse programmi kirjutada.  
Püüdke välja mõelda viise, kuidas juhuslikest vigadest valemis hoiduda (teisendamised, ümardamise täpsus jne). Võimalusel võrrelge tulemusi teistega. Kui on erinevusi, leidke ühiselt põhjused.
Kas programm on piisavalt hästi kirjutatud, et algandmete muutumise korral (näiteks juhul, kui on vaja arvutada Marsi ümbermõõtu 1-eurostes müntides) on parandusi selge ja lihtne teha?Ülesanne 2.2
"""
print() 
print() 
print("Ülesanne 2.2")
print("Marsi raadius 3389,5 km","\n1 EUR mündi diameeter 23,25 mm",
"\nMaa raadius 6378km",
"\n2EUR Mündi Diaameter 25,75 mm")

# Marsi raadius 3389,5 km
# 1EUR mündi diameeter 23,25 mm
# Maa raadius 6378km
# 2EUR Mündi Diaameter 25,75 mm
print()
print()
planediRaadius = float(input("Sissesta planeedi raadius: "))

MundiDiaameter = (float(input("Sissesta mündi diaameter: "))/1000000)

PI = 3.14

planeediUmbermoot = 2*PI*planediRaadius
print() 
print() 
print("Planeedi ümbermõõt kilomeetridest: ", round(planeediUmbermoot,1))
print("Tuleb panna nii palju 2 EURoset mündi järjest: ", int(planeediUmbermoot // MundiDiaameter))


#****************************************************************************************************************************************************************************
#Ülesanne 3
"""
Eelnevaid teadmisi kasutades kirjuta programm, mis väljastaks:
kill-koll kill-koll killadi-koll kill-koll kill-koll killadi-koll kill-koll kill-koll killkoll
kill-koll

Kas kasutasid muutujaid? Millistel juhtudel oleks muutujate kasutamine kindlasti otstarbekas?
"""
print()
print()
print("Ülesanne 3")
print("Eelnevaid teadmisi kasutades kirjuta programm, mis väljastaks:/nkill-koll kill-koll killadi-koll kill-koll kill-koll killadi-koll kill-koll kill-koll killkoll kill-koll")

# Või on võimalik kasutada mutujaid. Aga neid tuleb jälgida ja lugeda mitu tükki väljastada. 
kill = "kill-koll "
ladi = "killadi-koll "

print("kill-koll kill-koll killadi-koll kill-koll kill-koll killadi-koll kill-koll kill-koll killkoll kill-koll")
print("Oleks lihtsam ja osatarbelikum lihtsalt väljastada terve lause. Ja mitte kasutada mutujaid." )


#****************************************************************************************************************************************************************************
#Ülesanne 4
"""
Koosta programm, mis väljastaks järgmised laulusõnad:

Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?

Kuidas lahendasid ülesande? Kas seda saaks teha kuidagi paremini? Kui lihtne oleks sellest programmist teha uus, kui
soovitakse hoopis järgmist laulu?

Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill.


....Sisend, väljund, tingimus....
"""
print()
print("Ülesanne 4")
print("Koosta programm, mis väljastaks järgmised laulusõnad:")

print("Rong see sõitis tsuhh tsuhh tsuhh,")
print("piilupart oli rongijuht.")
print("Rattad tegid rat tat taa,")
print("rat tat taa ja tat tat taa.")
print("Aga seal rongi peal,")
print("kas sa tead, kes olid seal?")

print()
print("Rong see sõitis tuut tuut tuut,")
print("piilupart oli rongijuht.")
print("Rattad tegid kill koll koll,")
print("kill koll koll ja kill koll kill.")



#****************************************************************************************************************************************************************************
#Ülesanne 5
"""
Koosta programm, mis küsib kasutajalt ristküliku lähiskülgede pikkused ning väljastab ekraanile ristküliku ümbermõõdu ja pindala.
"""
print()
print()
print("Ülesanne 5")
print("Koosta programm, mis küsib kasutajalt ristküliku lähiskülgede pikkused ning väljastab ekraanile ristküliku ümbermõõdu ja pindala.")
# Kasutaja sissestab külg A ja B
aKulg = int(input("Sissesta A kulg: "))
kulgB = int(input("Sissesta B kulg: "))

# Arvutame ristküliku ümbermõõdu ja pindala
Pristkuliku = (aKulg + kulgB) * 2
Sristkuliku = aKulg * kulgB

print()
# Väljastab ekraanile ristküliku ümbermõõdu ja pindala.
print("Ristküliku ümbermõõt on: ", Pristkuliku)
print("Ristküliku pindala on: ", Sristkuliku)





