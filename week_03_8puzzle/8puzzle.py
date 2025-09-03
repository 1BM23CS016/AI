import collections

def misplaced_tiles(current_state, goal_state):
    count = 0
    for i in range(9):
        if current_state[i] != 0 and current_state[i] != goal_state[i]:
            count += 1
    return count

def manhattan_distance(current_state, goal_state):
    distance = 0
    goal_positions = {}
    for i, tile in enumerate(goal_state):
        if tile != 0:
            goal_positions[tile] = (i // 3, i % 3)
    for i, tile in enumerate(current_state):
        if tile != 0:
            current_row, current_col = i // 3, i % 3
            goal_row, goal_col = goal_positions[tile]
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance

def greedy_best_first_search(initial_state, goal_state, heuristic_func):
    open_list = [(heuristic_func(initial_state, goal_state), initial_state, [initial_state])]
    visited = {tuple(initial_state)}
    while open_list:
        best_node = min(open_list, key=lambda x: x[0])
        open_list.remove(best_node)
        h_value, current_state, path = best_node
        if current_state == goal_state:
            return path
        for action in get_possible_actions(current_state):
            next_state = apply_action(current_state, action)
            if tuple(next_state) not in visited:
                visited.add(tuple(next_state))
                h_value_next = heuristic_func(next_state, goal_state)
                open_list.append((h_value_next, next_state, path + [next_state]))
    return None

def get_possible_actions(state):
    actions = []
    blank_pos = state.index(0)
    blank_row, blank_col = blank_pos // 3, blank_pos % 3
    if blank_row > 0: actions.append("UP")
    if blank_row < 2: actions.append("DOWN")
    if blank_col > 0: actions.append("LEFT")
    if blank_col < 2: actions.append("RIGHT")
    return actions

def apply_action(state, action):
    new_state = state[:]
    blank_pos = state.index(0)
    blank_row, blank_col = blank_pos // 3, blank_pos % 3
    if action == "UP":
        new_pos = (blank_row - 1) * 3 + blank_col
    elif action == "DOWN":
        new_pos = (blank_row + 1) * 3 + blank_col
    elif action == "LEFT":
        new_pos = blank_row * 3 + (blank_col - 1)
    elif action == "RIGHT":
        new_pos = blank_row * 3 + (blank_col + 1)
    new_state[blank_pos], new_state[new_pos] = new_state[new_pos], new_state[blank_pos]
    return new_state

def is_solvable(state):
    inversions = 0
    tiles = [tile for tile in state if tile != 0]
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            if tiles[i] > tiles[j]:
                inversions += 1
    return inversions % 2 == 0

def print_solution_path(path):
    for i, state in enumerate(path):
        print(f"Step {i}:")
        print(state[0], state[1], state[2])
        print(state[3], state[4], state[5])
        print(state[6], state[7], state[8])
        print()

def solve_and_print(heuristic_name, heuristic_func, initial, goal):
    print(f"Solving with Greedy Best-First Search ({heuristic_name})...")
    solution = greedy_best_first_search(initial, goal, heuristic_func)
    if solution:
        print(f"Solution found in {len(solution) - 1} moves.")
        print("--- Solution Path ---")
        print_solution_path(solution)
    else:
        print("No solution found.")

initial = [1, 2, 3, 4, 0, 5, 7, 8, 6]
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

if is_solvable(initial):
    solve_and_print("Manhattan Distance", manhattan_distance, initial, goal)
    print()
    solve_and_print("Misplaced Tiles", misplaced_tiles, initial, goal)
else:
    print("Puzzle is not solvable")
