vit1 = 1
vit2 = 2
empate = 0
permitidos = ('pedra', 'tesoura', 'papel')

class JogadaInvalida(Exception):
	'''jogada diferente das permitidas'''

def jokenpo(jogada1, jogada2):
	if jogada1 not in permitidos:
		raise JogadaInvalida
	if jogada2 not in permitidos:
		raise JogadaInvalida

	if jogada1 == jogada2:
		return empate

	if jogada1 == permitidos[permitidos.index(jogada2) - 1]:
		return vit1
	else:
		return vit2