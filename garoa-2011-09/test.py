from jokenpo import jokenpo as jkp
from jokenpo import vit1, vit2, empate
from jokenpo import JogadaInvalida

def teste_empate():
	'''ver se o teste esta sendo testado, uai!'''
	assert empate == jkp('pedra','pedra')

def teste_vit1():
	assert vit1 == jkp('pedra', 'tesoura')

def teste_vit2():
	assert vit2 == jkp('pedra', 'papel')

def teste_vit1_tesoura():
	assert vit1 == jkp('tesoura', 'papel')

def teste_vit2_tesoura():
    assert vit2 == jkp('tesoura','pedra')
    
def teste_vit1_papel():
	assert vit1 == jkp('papel','pedra' )

def teste_jogador_sacana():
	try:
		jkp('pedra', 'pistola')
		assert False, 'nao deveria chegar aqui'
	except JogadaInvalida:
		pass