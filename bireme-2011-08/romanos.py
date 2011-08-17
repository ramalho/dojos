arabic2roman = (
	(1000, 'M'),
	(900, 'CM'),
	(500, 'D'),
	(400, 'CD'),
	(100, 'C'),
	(90, 'XC'),
	(50, 'L'),
	(40, 'XL'),
	(10, 'X'),
	(9, 'IX'),
	(5, 'V'),
	(4, 'IV'),
	(1, 'I'),
)
class OutOfBounds(Exception):
	"""Too large number"""

def arabico_para_romano(n):

	if n > 3999:
		raise OutOfBounds(n)

	for a,r in arabic2roman:
		if a == n:
			return r
		else:
			if n > a:
				return r + arabico_para_romano(n-a)