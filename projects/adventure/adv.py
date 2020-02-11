from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
def reverse_direction(direction):
  if direction == "n":
    return "s"
  elif direction == "s":
    return "n"
  elif direction == "e":
    return "w"
  elif direction == "w":
    return "e"
  else:
    return "Invalid direction"

# TRAVERSAL TEST
visited_rooms = set()
traversal_path = []
player.current_room = world.starting_room
current_directions = []
while len(visited_rooms) != 500:
    visited_rooms.add(player.current_room)
    exits = player.current_room.get_exits()
    if "n" in exits and player.current_room.get_room_in_direction("n") not in visited_rooms:
        current_directions.append('n')
        traversal_path.append('n')
        player.current_room = player.current_room.get_room_in_direction("n")
    elif "w" in exits and player.current_room.get_room_in_direction("w") not in visited_rooms:
        current_directions.append('w')
        traversal_path.append('w')
        player.current_room = player.current_room.get_room_in_direction("w")
    elif "s" in exits and player.current_room.get_room_in_direction("s") not in visited_rooms:
        current_directions.append('s')
        traversal_path.append('s')
        player.current_room = player.current_room.get_room_in_direction("s")
    elif "e" in exits and player.current_room.get_room_in_direction("e") not in visited_rooms:
        current_directions.append('e')
        traversal_path.append('e')
        player.current_room = player.current_room.get_room_in_direction("e")
    else:
        last_direction = current_directions.pop()
        traversal_path.append(reverse_direction(last_direction))
        player.current_room = player.current_room.get_room_in_direction(reverse_direction(last_direction))


for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
