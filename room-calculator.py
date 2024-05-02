import sys

def main(args: list):
	'''

	args[1] -> rent cost
	args[2] - > unit sq ft
	args[3] -> master bedroom dimensions
	args[4] -> regular bedroom dimensions

	master sqft = master bedroom width * master bedroom length
	reg sqft = reg bedroom width * reg bedroom length
	bedroom sqft = master sqft + reg sqft
	shared sqft = unit sqft - bedroom sqft

	master ratio = master sqft / unit sqft
	reg ratio = reg sqft / unit sqft
	shared ratio = shared sqft / unit sqft

	shared cost = rent cost * shared ratio / 2
	master cost = (rent cost * master ratio) + shared cost
	reg cost = (rent cost * reg ratio) + shared cost
	
	'''
	if (len(args) == 1 or args[1] == 'info'):
		return "arguments: rent cost, unit sq ft, master bedroom dimensions, regular bedroom dimensions"

	rent_cost = float(args[1])
	unit_sqft = float(args[2])
	master_sqft = float(args[3])
	reg_sqft = float(args[4])

	bedroom_sqft = (master_sqft + reg_sqft)
	shared_sqft = unit_sqft - bedroom_sqft

	master_ratio = master_sqft / unit_sqft
	reg_ratio = reg_sqft / unit_sqft
	shared_ratio = shared_sqft / unit_sqft

	total_ratio = master_ratio + reg_ratio + shared_ratio
	print(total_ratio)

	shared_cost = rent_cost * shared_ratio
	master_cost = rent_cost * master_ratio + (shared_cost / 2)
	reg_cost = rent_cost * reg_ratio + (shared_cost / 2)

	return f"Master: ${master_cost} and Regular: ${reg_cost}"

if __name__ == '__main__':
	exit(main(sys.argv))