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

def is_prime(nr):
	'''
	TODO
	'''
	if nr < 2:
		return False

	for i in range(2, nr): # 2, 3, 4, ..., nr - 1
		if nr % i == 0:
			return False

	return True



def main():
	while True:
		print('1. Minimul a trei numere.')
		print('2. Determinarea primalitatii.')
		print('x. Iesire din program - exit.')
		optiune = input('Alege optiunea: ')
		if optiune == '1':
			nr1 = int(input('Dati primul numar: '))
			nr2 = int(input('Dati al doilea numar: '))
			nr3 = int(input('Dati al treilea numar: '))
			minimul = get_minim(nr1, nr2, nr3)
			print(f'Minimul dintre {nr1}, {nr2}, {nr3} este {minimul}.')
		elif optiune == '2':
			nr = int(input('Dati un numar: '))
			if is_prime(nr):
				print('Numarul dat este prim.')
			else:
				print('Numarul dat nu este prim.')
		elif optiune == 'x':
			break
		else:
			print('Optiune invalida!')

main()

