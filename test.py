# loading file in program
with open("example.in") as file:
    lines = [line.split() for line in file]

# declaration of variables for cutting pizza
numbers = lines[0]
R = int(numbers[0]) # rows
C = int(numbers[1]) # columns
MIN = int(numbers[2]) # min of each ingredient per slice
MAX = int(numbers[3]) # max cells per slice

#remove numbers from input data
lines.remove(lines[0])

#'create' pizza list
pizza = []
i=0
while(i < len(lines)):
	temp = lines[i]
	curStr = temp[0]
	curList = list(curStr)
	pizza.append(curList)
	i += 1

print(pizza)

