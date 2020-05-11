#!/usr/bin/env python3


from mulTwoInt import mul
from addTwolnt import add

def demanderMult():

	try: #il arrive que la valeur entree ne soit pas en string selon le terminal (ex: Kali linux)
		i = input("Voulez-vous faire une multiplication (o/n) ?: ")
		return i;
	except:
		print("Veuillez mettre la valeur dans des ''")
		return demanderMult()

i = demanderMult()
	
if i in 'o':
	a = input('Entrez le 1er nombre: ')
	b = input('Entrez le 2eme nombre: ')

	try:
		print(mul(eval(a),eval(b)))
	except:
		print(mul(a,b))



