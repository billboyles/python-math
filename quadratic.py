import radicals

def solve(a, b, c):

	#housekeeping
	answer = []
	a = str(a)
	b = str(b)
	c = str(c)

	#check for a = 0
	if a == 0:
		answer = "a cannot be equal to 0"
		return answer

	#handle non-ints 
	#a
	if a[0] in ('-', '+'):				#TODO: refactor?
		if a[1:].isdigit():
			a = int(a)
		else:
			answer = "Please enter an integer"
			return answer
	else:
		if a.isdigit():
			a = int(a)
		else:
			answer = "Please enter an integer"
			return answer

	#b
	if b[0] in ('-', '+'):
		if b[1:].isdigit():
			b = int(b)
		else:
			answer = "Please enter an integer"
			return answer
	else:
		if b.isdigit():
			b = int(b)
		else:
			answer = "Please enter an integer"
			return answer

	#c
	if c[0] in ('-', '+'):
		if c[1:].isdigit():
			c = int(c)
		else:
			answer = "Please enter an integer"
			return answer
	else:
		if c.isdigit():
			c = int(c)
		else:
			answer = "Please enter an integer"
			return answer

	#handle large numbers
	if a > 1000000000000 or b > 1000000000000 or c > 1000000000000:
		answer = "Numbers must be less than 1,000,000,000,000"
		return answer

	#quadratic formula: [-b ± √(b² - 4ac)] / 2a

	bottom_line = 2 * a

	radical = radicals.simplify((b * b) - (4 * a * c))
	
	try:
		radical = int(radical)

		top_line_plus = -b + radical
		top_line_minus = -b - radical

		if (top_line_plus / bottom_line).is_integer:
			answer.append(int(top_line_plus / bottom_line))
		else:
			answer.append(f"{top_line_plus} / {bottom_line}")

		if (top_line_minus / bottom_line).is_integer:
			answer.append(int(top_line_minus / bottom_line))
		else:
			answer.append(f"{top_line_minus} / {bottom_line}")

		return answer

	except ValueError:

		#TODO: add logic for simplifying by factoring (future update)
		answer.append(f"{-b} + {radical} / {bottom_line}")
		answer.append(f"{-b} - {radical} / {bottom_line}")		

		return answer

#example
def main():
	print(solve(1,2,3))

if __name__ == "__main__":
	main()
