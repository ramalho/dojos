from romanos import arabico_para_romano as ar
from romanos import OutOfBounds

def teste_1():
    assert ar(1) == 'I'

def teste_2():
	assert ar(2) == 'II'

def teste_5():
	assert ar(5) == 'V'
  
def teste_3():
	assert ar(3) == 'III'

def teste_6():
	assert ar(6) == 'VI'

def teste_4():
	assert ar(4) == 'IV'

def teste_7():
	assert ar(7) == 'VII'

def teste_86():
	assert ar(86) == 'LXXXVI'

def teste_9():
	assert ar(9) == 'IX'

def teste_2000():
	assert ar(2000) == 'MM'

def teste_4000():
	try:
		ar(4000)
	except OutOfBounds:
		pass
	else:
		assert False

def teste_90():
	assert ar(90) == 'XC'