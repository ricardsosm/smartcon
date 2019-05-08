import hashlib
import string
import random

def random_key(size=5):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for x in range(size))

def generate_hash_key(salt, random_str_size=5):
    random_str = random_key(random_str_size)
    text = random_str + salt
    return hashlib.sha224(text.encode('utf-8')).hexdigest()

def saldo_token(size, digi):
	digitos = int(digi)
	palavra = str(size)
	tamanho = len(size)
	diferenca = tamanho - digitos
	if tamanho <= 18:
		feito = '0.'
		for i in range(digitos-tamanho):
			feito = feito + '0'
		feito = feito +palavra
	else:
		depois = palavra[diferenca:(digitos+1)]
		antes = palavra[0:diferenca]
		feito = antes + '.'+depois

	return feito
