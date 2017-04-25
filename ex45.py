### Towers of Hanoi Game  for later use in Reinforecement 
### Learning Tutorial


class Board(object):
	def __init__(self,num_rods,num_disks):
		self.num_rods = num_rods
		self.num_disks = num_disks
	
	def set_start(self):
		
		self.start_state =[]
		
		for rod in range(0, self.num_rods):
			if rod == 0:
				first_rod = []
				for disk in reversed(range(0, self.num_disks)):
					first_rod.append(disk)
				self.start_state.append(first_rod)
			else:
				self.start_state.append([])
		
		return self.start_state
		
			
class Game(object):
	
    def __init__(self, board):
	
		self.board = board
		self.state = self.board.set_start()
    
    def test_move(self,start_rod,end_rod):
        
        if not self.state[start_rod]:
            return False
        elif not self.state[end_rod]:
            return True
        elif self.state[start_rod][-1] <  self.state[end_rod][0]:
            return True
        elif start_rod == end_rod:
            return False
        else:
            return False

    def move(self, start_rod, end_rod):

        valid_move = self.test_move(start_rod, end_rod)

        if valid_move:
            disk = self.state[start_rod].pop()
            self.state[end_rod].append(disk)
        else:
            print "not a valid move"

    def print_board(self):
        
        # List comprehension to create sublists inside "print list"
        # Use comprehension so that each sublist is a separate object
        # If  you append the same sublist object.  A change to one 
        # sublist object become a change to all since they are referring to t
        print_list = [[] for x in range(self.board.num_disks)]


        for r in range(0,len(self.state)):
            for d in range(0,len(self.state[r])):
                print_list[d].append(self.state[r][d])
                
        for i in reversed(range(0, len(print_list))):
            print print_list[i]

board1 = Board(3,3)
game1 = Game(board1)

#game1.print_board()
game1.move(0,1)
game1.move(1,2)
print game1.state
game1.print_board()









