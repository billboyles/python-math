#required modules
import math, factors
from functools import reduce
from collections import Counter


def simplify(n):

	#housekeeping	
	is_neg = False 
	remove = ""			
		
	#handle non-ints
	try:
		n = int(n)
	except:
		return "Please enter an integer"

	#handle large numbers
	if n > 1000000000000:
		return "Number must be less than 1,000,000,000,000"

	#handle negatives
	if n < 0:
		n *= -1
		is_neg = True
	
	#handle trivial cases
	if n == 0 or n == 1:
		answer = f"{n}"
		if is_neg:
			answer = "i"
		return answer

	#check for perfect square
	if math.sqrt(n).is_integer():
		answer = f"{int(math.sqrt(n))}"
		if is_neg:
			answer += "i"
		return answer

	#if none of the above, simplify square root
	factors_list = factors.factor(n)

	prime_factors = []

	while len(factors_list) > 2:
		#slice off ends of factor_list
		factors_list = factors_list[1:-1]
		#add new lowest to primes
		prime_factors.append(factors_list[0])
		#factor new highest, repeat until only 2 factors left
		factors_list = factors.factor(factors_list[-1])
		

	#add last factor
	prime_factors.append(factors_list[1])

	#get count of each prime factor
	counts = Counter(prime_factors)
	
	remainders = []
	removes = []

	for k,v in counts.items():
		i = v
		while i > 1:
			removes.append(k)
			i -= 2
		if i == 1:
			remainders.append(k)

	#calculate up remainders
	remainder = reduce(lambda a, b: a * b, remainders)
	
	#if there were factors removed
	if len(removes) > 0:
		#calculate up removes
		remove = reduce(lambda a, b: a * b, removes)
		
		#convert to string
		remove = str(remove)

		#add i for negative inputs
		if is_neg:
			remove += "i"
		
	#add square root sign and remainder
	return remove + u"\u221A" + str(remainder)


#example
def main():
	print(simplify(-20))

if __name__ == "__main__":
	main()