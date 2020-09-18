print("Je loopt op school langs het snoepautomaat, wat doe je?")
print("Koop je SNOEP, KOEK, NIKS of ga je DRINKEN halen.")
choice = input()
if choice == 'SNOEP':
	print("Je eet je gekochte snoep en word misselijk. Je bent je €1 kwijt en hebt spijt.")
elif choice == 'KOEK': 
	print("Je eet je gekochte koek en word misselijk. Je bent je €1 kwijt en hebt spijt.")
elif choice == 'NIKS': 
	print("Je loopt verder, je koopt niks en bent geen geld kwijt")
elif choice == 'DRINKEN': 
	print("Je loopt verder naar de drinkmachine, hij is kapot. Je bent teleurgesteld.")
else:
	print("Ik begrijp dit niet, " + choice + ", probeer het nog een keer.")