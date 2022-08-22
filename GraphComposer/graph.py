
"""
Empty Graph Template to implement :D

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

import random

class Vertex(object):
    def __init__(self, value):
        self.value = value
        self.adjacent = {} # Which vertices are connected to this vertex
        self.neighbors = []
        self.neighbors_weights = []

    # Add an edge to the vertex we input with weight
    def add_edge_to(self, vertex, weight=0):
        self.adjacent[vertex] = weight

    # Incrementing the weight of the edge
    def increment_edge(self, vertex):
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    # initializes probability map
    def get_probability_map(self):
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbors_weights.append(weight)

    def next_word(self):
        # Randomly select next word based on Weights
        return random.choices(self.neighbors, weights=self.neighbors_weights)[0]

    def get_adjacent_nodes(self):
        pass



class Graph(object):
    def __init__(self):
        self.vertices = {}

    # Values of all vertices
    def get_vertex_values(self):
        return set(self.vertices.keys())

    def add_vertex(self, value):
        self.vertices[value] = Vertex(value)

    def get_vertex(self, value):
        # If the value is not in the graph
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value]

    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()
