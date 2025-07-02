import multiprocessing as mp
import time
import math
Results_a = []
Results_b = []
def make_calculation_one(numbers):
	for number in numbers:
		Results_a.append(math.sqrt(number **3))

def make_calculation_two(numbers):
	for number in numbers:
		Results_b.append(math.sqrt(number **4))

if __name__== "__main__": 

	number_list= list(range(10000000))
	p1 = mp.Process(target = make_calculation_one, args = (number_list,))
	p2 = mp.Process(target = make_calculation_two, args = (number_list,))
	start = time.time()
	p1.start()
	p2.start()
	end = time.time()
	print("time needed for calculation with multiprocessing", end-start)
	start = time.time()
	make_calculation_one(number_list)
	make_calculation_two(number_list)
	end = time.time()
	print("time needed for calculation without multiprocessing", end-start)