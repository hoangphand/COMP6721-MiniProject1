from utilities import gen_children_h1
from utilities import h1_evaluation
from utilities import sort_BFS
import config

input_file = open("input.txt", "r")
input = input_file.read().split()
input = map(int, input)
goal = []
for i in range(1, config.ROWS * config.COLS):
	goal.append(i)
goal.append(0)

open_list = [input]
h_input = h1_evaluation(input)
open_list_details = [(input, h_input, 0, h_input, [])]
closed = []
closed_details = []
count = 0

# print goal
# print input
# print open_list_details[0]
# children = gen_children_h1(open_list_details[0])
# children = sorted(children, key = lambda el: el[1], reverse=True)

# for child in children:
# 	print child

while open_list != []:
	open_list.pop()
	current = open_list_details.pop()
	count = count + 1
	print(count)
	print(current[0])

	if current[0] == goal:
		print "yay"
		print current
		print count
		break
	else:
		children = gen_children_h1(current)

		closed_details.append(current)
		closed.append(current[0])

		clone_children = [el[0] for el in children]

		for child in clone_children:
			try:
				index = open_list.index(child)
				index_of_child_open = -1
				for child_details in children:
					if child_details[0] == child:
						index_of_child_open = children.index(child_details)
						break
			except ValueError:
				index_of_child_open = -1

			if index_of_child_open != -1:
				del children[index_of_child_open]

			try:
				index = closed.index(child)
				index_of_child_closed = -1
				for child_details in children:
					if child_details[0] == child:
						index_of_child_closed = children.index(child_details)
						break
			except ValueError:
				index_of_child_closed = -1

			if index_of_child_closed != -1:
				del children[index_of_child_closed]

		clone_children = [el[0] for el in children]

		open_list_details.extend(children)
		open_list_details = sort_BFS(open_list_details)
		open_list.extend(clone_children)

f = open("puzzleBFS-h1.txt", "w")
f.write("0 " + str(input) + "\n")
for step in current[4]:
	index_of_zero = input.index(0)
	tmp = input[step]
	input[step] = 0
	input[index_of_zero] = tmp
	f.write(chr(97 + step) + " " + str(input) + "\n")