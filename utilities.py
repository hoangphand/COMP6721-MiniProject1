from collections import deque
import random
import config

goal = []
for i in range(1, config.ROWS * config.COLS):
	goal.append(i)
goal.append(0)

def gen_children(current):
	children = []
	index_of_zero = current[0].index(0)

	# UP
	if index_of_zero > config.COLS - 1:
		up = current[0][:]
		tmp_path = current[2][:]
		tmp_path.append(index_of_zero - config.COLS)
		tmp = up[index_of_zero - config.COLS]
		up[index_of_zero] = tmp
		up[index_of_zero - config.COLS] = 0
		children.append((up, current[1] + 1, tmp_path))

	# UP RIGHT
	if index_of_zero > config.COLS - 1 and index_of_zero % config.COLS != config.COLS - 1:
		up_right = current[0][:]
		tmp_path = current[2][:]
		tmp_path.append(index_of_zero - config.COLS + 1)
		tmp = up_right[index_of_zero - config.COLS + 1]
		up_right[index_of_zero] = tmp
		up_right[index_of_zero - config.COLS + 1] = 0
		children.append((up_right, current[1] + 1, tmp_path))

	# RIGHT
	if index_of_zero % config.COLS != config.COLS - 1:
		right = current[0][:]
		tmp_path = current[2][:]
		tmp_path.append(index_of_zero + 1)
		tmp = right[index_of_zero + 1]
		right[index_of_zero] = tmp
		right[index_of_zero + 1] = 0
		children.append((right, current[1] + 1, tmp_path))

	# DOWN RIGHT
	if index_of_zero < config.COLS * (config.ROWS - 1) and index_of_zero % config.COLS != config.COLS - 1:
		down_right = current[0][:]
		tmp_path = current[2][:]
		tmp_path.append(index_of_zero + config.COLS + 1)
		tmp = down_right[index_of_zero + config.COLS + 1]
		down_right[index_of_zero] = tmp
		down_right[index_of_zero + config.COLS + 1] = 0
		children.append((down_right, current[1] + 1, tmp_path))

	# DOWN
	if index_of_zero < config.COLS * (config.ROWS - 1):
		down = current[0][:]
		tmp_path = current[2][:]
		tmp_path.append(index_of_zero + config.COLS)
		tmp = down[index_of_zero + config.COLS]
		down[index_of_zero] = tmp
		down[index_of_zero + config.COLS] = 0
		children.append((down, current[1] + 1, tmp_path))

	# DOWN LEFT
	if index_of_zero < config.COLS * (config.ROWS - 1) and index_of_zero % config.COLS != 0:
		down_left = current[0][:]
		tmp_path = current[2][:]
		tmp_path.append(index_of_zero + config.COLS - 1)
		tmp = down_left[index_of_zero + config.COLS - 1]
		down_left[index_of_zero] = tmp
		down_left[index_of_zero + config.COLS - 1] = 0
		children.append((down_left, current[1] + 1, tmp_path))

	# LEFT
	if index_of_zero % config.COLS != 0:
		left = current[0][:]
		tmp_path = current[2][:]
		tmp_path.append(index_of_zero - 1)
		tmp = left[index_of_zero - 1]
		left[index_of_zero] = tmp
		left[index_of_zero - 1] = 0
		children.append((left, current[1] + 1, tmp_path))

	# UP LEFT
	if index_of_zero > config.COLS - 1 and index_of_zero % config.COLS != 0:
		up_left = current[0][:]
		tmp_path = current[2][:]
		tmp_path.append(index_of_zero - config.COLS - 1)
		tmp = up_left[index_of_zero - config.COLS - 1]
		up_left[index_of_zero] = tmp
		up_left[index_of_zero - config.COLS - 1] = 0
		children.append((up_left, current[1] + 1, tmp_path))

	return children

def h1_evaluation(current):
	diff = 0

	for index in range(0, len(goal)):
		if goal[index] != current[index]:
			diff = diff + 1

	return diff

def gen_children_h1(current):
	children = []
	index_of_zero = current[0].index(0)

	# UP
	if index_of_zero > config.COLS - 1:
		up = current[0][:]
		tmp_path = current[4][:]
		tmp_path.append(index_of_zero - config.COLS)
		tmp = up[index_of_zero - config.COLS]
		up[index_of_zero] = tmp
		up[index_of_zero - config.COLS] = 0
		h = h1_evaluation(up)
		children.append((up, current[2] + 1 + h, current[2] + 1, h, tmp_path))

	# UP RIGHT
	if index_of_zero > config.COLS - 1 and index_of_zero % config.COLS != config.COLS - 1:
		up_right = current[0][:]
		tmp_path = current[4][:]
		tmp_path.append(index_of_zero - config.COLS + 1)
		tmp = up_right[index_of_zero - config.COLS + 1]
		up_right[index_of_zero] = tmp
		up_right[index_of_zero - config.COLS + 1] = 0
		h = h1_evaluation(up_right)
		children.append((up_right, current[2] + 1 + h, current[2] + 1, h, tmp_path))

	# RIGHT
	if index_of_zero % config.COLS != config.COLS - 1:
		right = current[0][:]
		tmp_path = current[4][:]
		tmp_path.append(index_of_zero + 1)
		tmp = right[index_of_zero + 1]
		right[index_of_zero] = tmp
		right[index_of_zero + 1] = 0
		h = h1_evaluation(right)
		children.append((right, current[2] + 1 + h, current[2] + 1, h, tmp_path))

	# DOWN RIGHT
	if index_of_zero < config.COLS * (config.ROWS - 1) and index_of_zero % config.COLS != config.COLS - 1:
		down_right = current[0][:]
		tmp_path = current[4][:]
		tmp_path.append(index_of_zero + config.COLS + 1)
		tmp = down_right[index_of_zero + config.COLS + 1]
		down_right[index_of_zero] = tmp
		down_right[index_of_zero + config.COLS + 1] = 0
		h = h1_evaluation(down_right)
		children.append((down_right, current[2] + 1 + h, current[2] + 1, h, tmp_path))

	# DOWN
	if index_of_zero < config.COLS * (config.ROWS - 1):
		down = current[0][:]
		tmp_path = current[4][:]
		tmp_path.append(index_of_zero + config.COLS)
		tmp = down[index_of_zero + config.COLS]
		down[index_of_zero] = tmp
		down[index_of_zero + config.COLS] = 0
		h = h1_evaluation(down)
		children.append((down, current[2] + 1 + h, current[2] + 1, h, tmp_path))

	# DOWN LEFT
	if index_of_zero < config.COLS * (config.ROWS - 1) and index_of_zero % config.COLS != 0:
		down_left = current[0][:]
		tmp_path = current[4][:]
		tmp_path.append(index_of_zero + config.COLS - 1)
		tmp = down_left[index_of_zero + config.COLS - 1]
		down_left[index_of_zero] = tmp
		down_left[index_of_zero + config.COLS - 1] = 0
		h = h1_evaluation(down_left)
		children.append((down_left, current[2] + 1 + h, current[2] + 1, h, tmp_path))

	# LEFT
	if index_of_zero % config.COLS != 0:
		left = current[0][:]
		tmp_path = current[4][:]
		tmp_path.append(index_of_zero - 1)
		tmp = left[index_of_zero - 1]
		left[index_of_zero] = tmp
		left[index_of_zero - 1] = 0
		h = h1_evaluation(left)
		children.append((left, current[2] + 1 + h, current[2] + 1, h, tmp_path))

	# UP LEFT
	if index_of_zero > config.COLS - 1 and index_of_zero % config.COLS != 0:
		up_left = current[0][:]
		tmp_path = current[4][:]
		tmp_path.append(index_of_zero - config.COLS - 1)
		tmp = up_left[index_of_zero - config.COLS - 1]
		up_left[index_of_zero] = tmp
		up_left[index_of_zero - config.COLS - 1] = 0
		h = h1_evaluation(up_left)
		children.append((up_left, current[2] + 1 + h, current[2] + 1, h, tmp_path))

	return children

def evaluate_manhattan(current):
	h = 0

	for index in range(0, len(current)):
		# h = h + evaluate_tile_usual_manhattan(current, current[index])
		h = h + evaluate_tile_special_manhattan(current, current[index])

	return h

def evaluate_tile_usual_manhattan(current, tile):
	index_in_current_x = current.index(tile) % config.COLS
	index_in_current_y = current.index(tile) / config.COLS
	index_in_goal_x = goal.index(tile) % config.COLS
	index_in_goal_y = goal.index(tile) / config.COLS

	distance = abs(index_in_goal_x - index_in_current_x) + abs(index_in_goal_y - index_in_current_y)

	return distance

def evaluate_tile_special_manhattan(current, tile):
	index_in_current_x = current.index(tile) % config.COLS
	index_in_current_y = current.index(tile) / config.COLS
	index_in_goal_x = goal.index(tile) % config.COLS
	index_in_goal_y = goal.index(tile) / config.COLS

	diff_x = abs(index_in_goal_x - index_in_current_x)
	diff_y = abs(index_in_goal_y - index_in_current_y)
	distance = min(diff_x, diff_y) + abs(diff_y - diff_x)

	return distance

def gen_children_h2(current):
	children = []
	index_of_zero = current[0].index(0)

	# UP
	if index_of_zero > config.COLS - 1:
		up = current[0][:]
		tmp_path = current[4][:]
		tmp_path.append(index_of_zero - config.COLS)
		tmp = up[index_of_zero - config.COLS]
		up[index_of_zero] = tmp
		up[index_of_zero - config.COLS] = 0
		h = evaluate_manhattan(up)
		children.append((up, current[2] + 1 + h, current[2] + 1, h, tmp_path))

	# UP RIGHT
	if index_of_zero > config.COLS - 1 and index_of_zero % config.COLS != config.COLS - 1:
		up_right = current[0][:]
		tmp_path = current[4][:]
		tmp_path.append(index_of_zero - config.COLS + 1)
		tmp = up_right[index_of_zero - config.COLS + 1]
		up_right[index_of_zero] = tmp
		up_right[index_of_zero - config.COLS + 1] = 0
		h = evaluate_manhattan(up_right)
		children.append((up_right, current[2] + 1 + h, current[2] + 1, h, tmp_path))

	# RIGHT
	if index_of_zero % config.COLS != config.COLS - 1:
		right = current[0][:]
		tmp_path = current[4][:]
		tmp_path.append(index_of_zero + 1)
		tmp = right[index_of_zero + 1]
		right[index_of_zero] = tmp
		right[index_of_zero + 1] = 0
		h = evaluate_manhattan(right)
		children.append((right, current[2] + 1 + h, current[2] + 1, h, tmp_path))

	# DOWN RIGHT
	if index_of_zero < config.COLS * (config.ROWS - 1) and index_of_zero % config.COLS != config.COLS - 1:
		down_right = current[0][:]
		tmp_path = current[4][:]
		tmp_path.append(index_of_zero + config.COLS + 1)
		tmp = down_right[index_of_zero + config.COLS + 1]
		down_right[index_of_zero] = tmp
		down_right[index_of_zero + config.COLS + 1] = 0
		h = evaluate_manhattan(down_right)
		children.append((down_right, current[2] + 1 + h, current[2] + 1, h, tmp_path))

	# DOWN
	if index_of_zero < config.COLS * (config.ROWS - 1):
		down = current[0][:]
		tmp_path = current[4][:]
		tmp_path.append(index_of_zero + config.COLS)
		tmp = down[index_of_zero + config.COLS]
		down[index_of_zero] = tmp
		down[index_of_zero + config.COLS] = 0
		h = evaluate_manhattan(down)
		children.append((down, current[2] + 1 + h, current[2] + 1, h, tmp_path))

	# DOWN LEFT
	if index_of_zero < config.COLS * (config.ROWS - 1) and index_of_zero % config.COLS != 0:
		down_left = current[0][:]
		tmp_path = current[4][:]
		tmp_path.append(index_of_zero + config.COLS - 1)
		tmp = down_left[index_of_zero + config.COLS - 1]
		down_left[index_of_zero] = tmp
		down_left[index_of_zero + config.COLS - 1] = 0
		h = evaluate_manhattan(down_left)
		children.append((down_left, current[2] + 1 + h, current[2] + 1, h, tmp_path))

	# LEFT
	if index_of_zero % config.COLS != 0:
		left = current[0][:]
		tmp_path = current[4][:]
		tmp_path.append(index_of_zero - 1)
		tmp = left[index_of_zero - 1]
		left[index_of_zero] = tmp
		left[index_of_zero - 1] = 0
		h = evaluate_manhattan(left)
		children.append((left, current[2] + 1 + h, current[2] + 1, h, tmp_path))

	# UP LEFT
	if index_of_zero > config.COLS - 1 and index_of_zero % config.COLS != 0:
		up_left = current[0][:]
		tmp_path = current[4][:]
		tmp_path.append(index_of_zero - config.COLS - 1)
		tmp = up_left[index_of_zero - config.COLS - 1]
		up_left[index_of_zero] = tmp
		up_left[index_of_zero - config.COLS - 1] = 0
		h = evaluate_manhattan(up_left)
		children.append((up_left, current[2] + 1 + h, current[2] + 1, h, tmp_path))

	return children

def sort_BFS(list_of_states):
	return sorted(list_of_states, key = lambda el: el[3], reverse=True)

def sort_AS(list_of_states):
	return sorted(list_of_states, key = lambda el: el[1], reverse=True)

def gen_input(no_ite):
	# initial = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0]
	initial = []
	for i in range(1, config.ROWS * config.COLS):
		initial.append(i)
	initial.append(0)

	moves = []

	for ite in range(0, no_ite):
		moves.append(random.randint(1, 8))

	for move in moves:
		index_of_zero = initial.index(0)

		if move == 1 and index_of_zero > config.COLS:
			# UP
			tmp = initial[index_of_zero - config.COLS]
			initial[index_of_zero] = tmp
			initial[index_of_zero - config.COLS] = 0
		elif move == 2 and index_of_zero > config.COLS and index_of_zero % config.COLS < config.COLS - 1:
			# UP RIGHT
			tmp = initial[index_of_zero - config.COLS - 1]
			initial[index_of_zero] = tmp
			initial[index_of_zero - config.COLS - 1] = 0
		elif move == 3 and index_of_zero % config.COLS < config.COLS - 1:
			# RIGHT
			tmp = initial[index_of_zero + 1]
			initial[index_of_zero] = tmp
			initial[index_of_zero + 1] = 0
		elif move == 4 and index_of_zero < config.COLS * (config.ROWS - 1) - 1 and index_of_zero % config.COLS < config.COLS - 1:
			# DOWN RIGHT
			tmp = initial[index_of_zero + config.COLS + 1]
			initial[index_of_zero] = tmp
			initial[index_of_zero + config.COLS + 1] = 0
		elif move == 5 and index_of_zero < config.COLS * (config.ROWS - 1) - 1:
			# DOWN
			tmp = initial[index_of_zero + config.COLS]
			initial[index_of_zero] = tmp
			initial[index_of_zero + config.COLS] = 0
		elif move == 6 and index_of_zero < config.COLS * (config.ROWS - 1) - 1 and index_of_zero % config.COLS != 0:
			# DOWN LEFT
			tmp = initial[index_of_zero + config.COLS - 1]
			initial[index_of_zero] = tmp
			initial[index_of_zero + config.COLS - 1] = 0
		elif move == 7 and index_of_zero % config.COLS != 0:
			# LEFT
			tmp = initial[index_of_zero - 1]
			initial[index_of_zero] = tmp
			initial[index_of_zero - 1] = 0
		elif move == 8 and index_of_zero > config.COLS and index_of_zero % config.COLS != 0:
			# UP LEFT
			tmp = initial[index_of_zero - config.COLS - 1]
			initial[index_of_zero] = tmp
			initial[index_of_zero - config.COLS - 1] = 0

	return initial