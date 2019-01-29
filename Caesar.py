import string

def cezar_encrypt(napis, klucz) :
	if napis.islower() :
		alphabet = string.ascii_lowercase
		kod = alphabet[klucz:] + alphabet[:klucz]
		table = str.maketrans(alphabet, kod)
		return napis.translate(table)
	elif napis.isspace() :
		return napis
	else :
		alphabet = string.ascii_uppercase
		kod = alphabet[klucz:] + alphabet[:klucz]
		table = str.maketrans(alphabet, kod)
		return napis.translate(table)

def main() :
	tekst = input("Podaj Tekst do zaszyfrowania : ")
	klucz = int(input("Podaj Klucz : "))
	print("Ciąg zaszyfrowany : ")
	a=0;
	for c in tekst :
		print(cezar_encrypt(tekst[a], klucz), end="")
		a=a+1
	print("")

main()
