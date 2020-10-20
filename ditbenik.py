print ("Hello you! Ik ben Simon.")
naam = input("Wie ben jij? ")
print ("Hello " + naam)
print("Ik ga je een quiz geven om mij beter te leren kennen.")
choice = input("Welke kleur haar heb ik? A: Blond, B: Rossig of C: Bruin?")
if choice == 'A' or choice == 'C':
	print("FOUT, probeer opnieuw!")
elif choice == 'B': 
	print("GOED!")
    choice2 = input("Vraag 2: Wat is mij favoriete kleur? A: Rood, B: Bruin of C: Groen?")
    if choice2 == 'A' or choice2 == 'B':
        print("FOUT, probeer opnieuw!")
    elif choice2 == 'C':
        print("GOED!")
        choice3 = input("Laatste vraag: Wat is mijn favoriete game? A: Fortnite, B: League of Legends of C: Call of Duty?")
        if choice3 == 'A' or choice3 == 'C':
	    print("FOUT, probeer opnieuw!")
        elif choice3 == 'B': 
	    print("GOED! Je hebt de quiz perfect gemaakt!")
        else:
            print("Verkeerd ingevoerd, probeer opnieuw!")
    else:
        print("Verkeerd ingevoerd, probeer opnieuw!")
else:
	print("Verkeerd ingevoerd, probeer opnieuw!")
