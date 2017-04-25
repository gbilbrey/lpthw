## SETUP: Import classes  and instantiate map and engine objects

from ex43 import * 
test_map = Map('central_corridor')
test_game = Engine(test_map)




# ## TESTS FOR SCENES AND MAP DICTIONARY



# # # Print out scenes
# print "   "
# print "------------------------------"
# print "SCENE DICT FROM MAP"
# print "------------------------------"
# print "   "

# for item in test_map.scenes:
	# print test_map.scenes[item]

# # put in a start scene an print out

# print "   "
# print "------------------------------"
# print "START SCENE KEY"
# print "------------------------------"
# print "   "

# print test_map.start_scene_key

# # Test central_corridor

# print "   "
# print "------------------------------"
# print "TEST FOR CENTRAL CORRIDOR CLASS"
# print "(choose 'tell a joke')"
# print "------------------------------"
# print "   "

# test_central_corridor = CentralCorridor()
# test_central_corridor_answer = test_central_corridor.enter()
# print "Scene returns %s" %test_central_corridor_answer

## TESTS FOR GAME PLAY

print "   "
print "------------------------------"
print "OPENING SCENE KEY IS"
print "------------------------------"
print "   "

print test_game.start_scene_key

print "   "
print "------------------------------"
print "CURRENT SCENE MAP IS At Start"
print "------------------------------"
print "   "

print test_game.scene_map

print "   "
print "------------------------------"
print "NOW PLAY A GAME"
print "------------------------------"
print "   "

test_game.play()
# print '-'*10
# print 'Current scene is now'
# print test_game.current_scene_key
# print test_game.current_scene








