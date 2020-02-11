import random

class User:
    def __init__(self, name):
        self.name = name

class Queue():
  def __init__(self):
      self.queue = []
  def enqueue(self, value):
      self.queue.append(value)
  def dequeue(self):
      if self.size() > 0:
          return self.queue.pop(0)
      else:
          return None
  def size(self):
      return len(self.queue)

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}
    
    def get_neighbors(self, vertex_id):
      """
      Get all neighbors (edges) of a vertex.
      """
      neighbors = []
      if vertex_id in self.friendships:
        for node in self.friendships[vertex_id]:
          neighbors.append(node)
      else:
        return []
      return neighbors

    def bfs(self, starting_vertex, destination_vertex):
      """
      Return a list containing the shortest path from
      starting_vertex to destination_vertex in
      breath-first order.
      """
      hash = {}
      q = Queue()
      q.enqueue({ "value": starting_vertex, "previous_items": [] })
      while q.size() > 0:
        current_node = q.dequeue()
        current_value = current_node["value"]
        current_previous_items = current_node["previous_items"]

        if current_value == destination_vertex:
          return current_previous_items + [current_value]
        #add to hash
        if current_value not in hash:
          hash[current_value] = True 

          for neighbor in self.get_neighbors(current_value):
            q.enqueue({"value": neighbor, "previous_items": current_previous_items + [current_value] })
      return []
    def get_percentage_of_other_users(self, starting_vertex):
      """
      Start with starting_vertex as given user
      count every node in graph

      percentage of other users that are not the user or immediate friends
      """
      hash = {}
      q = Queue()
      q.enqueue(starting_vertex)
      count = 0 
      while q.size() > 0:
        current_node = q.dequeue()

        #add to hash
        if current_node not in hash:
          count += 1
          hash[current_node] = True 

          for neighbor in self.get_neighbors(current_node):
            q.enqueue(neighbor)
      # self.friendships is dictionary with user_id: {3, 4, 2}
      # len will give us length
      other_users = count - 1 - len(self.friendships[starting_vertex])
      # other users divided by all users
      return round(other_users/len(self.users)*100)
    
    def degree_of_separation(self, starting_vertex):
      """
      Start with starting_vertex as given user
      count every node in graph
      """
      hash = {}
      q = Queue()
      q.enqueue({"value": starting_vertex, "depth": 0})
      other_users = 0 
      total_depth = 0
      while q.size() > 0:
        current = q.dequeue()
        #add to hash
        if current["value"] not in hash:
          other_users += 1
          total_depth += current["depth"]
          hash[current["value"]] = True 

          for neighbor in self.get_neighbors(current["value"]):
            q.enqueue({"value": neighbor, "depth": current["depth"] + 1})
    
      return round(total_depth/other_users, 2)

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Average number of friends to add
        total_friends = avg_friendships * num_users

        # Add users
        for user_id in range(1, num_users + 1):
          self.add_user(user_id)
        
        # make friendship pairs
        friendship_pairs = []
        for i in range(1, num_users + 1):
          for j in range(i + 1, num_users + 1):
            friendship_pairs.append((i, j))
        
        random.shuffle(friendship_pairs)
        # 10 pairs -> 20 relationships
        count = total_friends // 2
        for friendship_pair in friendship_pairs:
          if count == 0:
            break
          if len(self.friendships[friendship_pair[0]]) < 4 and len(self.friendships[friendship_pair[1]]) < 4:
            self.add_friendship(friendship_pair[0], friendship_pair[1])
            count -= 1
        

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        for num in self.users.keys():
          if len(self.bfs(user_id, num)) > 0:
            visited[num] = self.bfs(user_id, num)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(1000, 5)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
    print(sg.degree_of_separation(1))