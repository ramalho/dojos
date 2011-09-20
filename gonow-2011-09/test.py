from telefones import _para_numero, para_numeros

def teste_traco_permanece_inalterado():
	assert _para_numero('-') == '-'

def teste_0_eh_0():
	assert _para_numero('0') == '0' 

def teste_1_eh_1():
	assert _para_numero('1') == '1'

def teste_ABC_representam_2():
	assert _para_numero('A') == '2'
	assert _para_numero('B') == '2'
	assert _para_numero('C') == '2'

def test_D_eh_3():
	assert _para_numero('D') == '3'

def test_0DA_eh_032():
	assert para_numeros("0DA") == "032"

def teste_0A_eh_02():
	assert para_numeros('0A') == '02'

def teste_00_eh_00():
	assert para_numeros('00') == '00'

def test_gg_eh_44():
	assert para_numeros('gg') == '44'

def test_j_eh_5():
	assert para_numeros('j') == '5'

def test_m_eh_6():
	assert para_numeros('m') == '6'

def teste_conversao_porto():
	assert para_numeros('333-porto') == '333-76786'

