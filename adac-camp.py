# Roman numeral codes
roman_numerals = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}


def get_digit(number, n):
	'''returns nth digit in a integer number'''
	return number // 10**n % 10

def substring(digit, nth_digit):
	'''
	returns roman numerals for nth digit
	digit - nth digit
	nth_digit - value of (10 power n)
	'''
	roman_digit = ''
	if 0 < digit < 4:
		roman_digit = roman_numerals[1 * nth_digit] * digit
	elif digit == 4:
		roman_digit = roman_numerals[1*nth_digit] + roman_numerals[5*nth_digit]
	elif digit == 5:
		roman_digit = roman_numerals[5*nth_digit]
	elif 5 < digit < 9:
		roman_digit = roman_numerals[5*nth_digit] + roman_numerals[1*nth_digit] * (digit - 5)
	elif digit == 9:
			roman_digit = roman_numerals[1*nth_digit] + roman_numerals[10*nth_digit]
	return roman_digit

def get_roman_numerals(number):
	'''
	returns roman numerals for nth digit
	number - integer hindu-arabic numerals
	'''
	if 0 < number > 3999:
		return 'Invalid Roman Number'
	elif number%1000:
		set1 = get_digit(number, 3)
		roman_set1 = roman_numerals[1000] * set1

		set2 = get_digit(number, 2)
		roman_set2 = substring(set2, 100)

		set3 = get_digit(number, 1)
		roman_set3 = substring(set3, 10)

		set4 = get_digit(number, 0)
		roman_set4 = substring(set4, 1)

		roman = roman_set1 + roman_set2 + roman_set3 + roman_set4
	return roman
		

if __name__ == '__main__':
	# calling function 
	print(get_roman_numerals(4999))
