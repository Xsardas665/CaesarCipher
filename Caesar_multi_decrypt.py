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
	print("Ciąg zaszyfrowany : ")
	a=0;
	key = 0
	for index in range(0,26) :
		klucz = "[" + str(key) + "] "
		print(klucz, end="")
		for c in tekst :
			print(cezar_encrypt(tekst[a], key), end="")
			a=a+1
		print("")
		key = key +1
		a=0

main()
