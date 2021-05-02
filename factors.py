import math

def factor(n):

	#housekeeping vars
	factors = []

	#handle non-ints
	try:
		n = int(n)
	except:
		answer = "Please enter an integer"
		return answer

	#handle large numbers
	if n > 1000000000000:
		answer = "Number must be less than 1,000,000,000,000"
		return answer
	
	#handle trivial cases
	if n == 0 or n == 1:
		answer = f"{n}"
		return answer

	#handle negatives
	if n < 0:
		answer = "Number must be positive"
		return answer
	

	for i in range(1, math.ceil(n / 2) + 1):
		j = n / i
		if j.is_integer():
			if i in factors:
				break
			else:
				factors.append(i)
				factors.append(int(j))


	answer = sorted(factors)

	#return dict
	return answer

def main():
	print(factor(144))

if __name__ == '__main__':
	main()