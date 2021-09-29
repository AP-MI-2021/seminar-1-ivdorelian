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

def test_is_prime():
	assert is_prime(-5) == False
	assert is_prime(0) == False
	assert is_prime(1) == False
	assert is_prime(2) == True
	assert is_prime(3) == True
	assert is_prime(9) == False
	assert is_prime(15) == False
	assert is_prime(103) == True
	assert is_prime(101*103) == False
	assert is_prime(666013) == True


def print_primality(lst):
	for i in range(len(lst)): # 0, 1, 2, ..., len(lst) - 1
		if is_prime(lst[i]):
			print(f'{lst[i]} este prim.')
		else:
			print(f'{lst[i]} nu este prim.')

def get_digits_in_reverse_order(nr):
	'''
	TODO
	'''
	result = ''
	while nr:
		result = result + str(nr % 10)
		nr = nr // 10

	return result

def main():
	while True:
		print('1. Minimul a trei numere.')
		print('2. Determinarea primalitatii.')
		print('3. Afisare primalitate pentru elementele unei liste.')
		print('4. Afisarea cifrelor unui numar in ordine inversa.')
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
		elif optiune == '3':
			numere_str = input('Dati numerele separate prin spatiu: ')
			numere_str_lst = numere_str.split(' ')
			numere_int_lst = []
			for nr_str in numere_str_lst:
				numere_int_lst.append(int(nr_str))
			print_primality(numere_int_lst)
		elif optiune == '4':
			nr = int(input('Dati un numar: '))
			print('Inversul este:', get_digits_in_reverse_order(nr))
		elif optiune == 'x':
			break
		else:
			print('Optiune invalida!')

def f(x, y):
	return 2*x, y-6

p, q = f(5, 8)
print(p, q)

test_is_prime()
main()

