import radicals

def solve(a, b, c):

	answer = []

	if a == 0:
		return "a cannot be equal to 0"

	try:
		a = int(a)
		b = int(b)
		c = int(c)
	except:
		return "a, b, and c must all be integers"


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
	print(solve(1,1,1))

if __name__ == "__main__":
	main()
