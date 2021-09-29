def get_minim(a, b, c):
	'''
	Determina minimul a 3 numere.
	Input:
	- a, b, c: int
	Output:
	- minimul dintre a, b si c
	'''
	m = a
	if b < m:
		m = b
	if c < m:
		m = c
	return m

def main():
	nr1 = int(input('Dati primul numar: '))
	nr2 = int(input('Dati al doilea numar: '))
	nr3 = int(input('Dati al treilea numar: '))
	minimul = get_minim(nr1, nr2, nr3)
	print(f'Minimul dintre {nr1}, {nr2}, {nr3} este {minimul}.')

main()

