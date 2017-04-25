## Towers of Hanoi game.  Plan is later use this with 
## Reinforcement Learning model to find optimal strategy

## Create Initial Game State
def game_setup():
	state = [[1,2,3,4],[],[]]
	return state


## Check to see if rod is empty

def is_empty(rod,state):
	if len(state[rod]) == 0:
		is_empty = True
	else:
		is_empty = False
	return is_empty


## Check to see if move is legal. Returns 1 if valid

def check_valid_move(from_rod,to_rod,state):
	if is_empty(from_rod,state):
		valid_move = 0
	elif is_empty(to_rod,state):
		valid_move = 1
	elif state[from_rod][0] < state[to_rod][0]:
		valid_move = 1
	elif state[from_rod][0] > state[to_rod][0]:
		valid_move = 0
	else:
		valid_move = 2
		print "something weird is happening here"
	return valid_move


## Make a move
def move(from_rod,to_rod,state):
	if check_valid_move(from_rod,to_rod,state)== 1:
		disk_to_move = state[from_rod].pop(0)
		state[to_rod].insert(0,disk_to_move)
		print "Valid move!  New board is: %r" %state
	elif check_valid_move(from_rod,to_rod,state)== 0:
		print "Try again"
		print  "Current board is %r" %state
	else:
		print "It looks like the move didn't make sense. valid move = 2"


		



		
	
	



	
	

	
	
	



