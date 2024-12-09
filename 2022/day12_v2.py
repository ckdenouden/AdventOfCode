class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Node(self.x + other.x, self.y + other.y)


class Heightmap:
    def __init__(self, x_dim, y_dim, nodes):
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.nodes = nodes

    def __getitem__(self, coord):
        x, y = coord.x, coord.y
        return self.nodes[y*self.x_dim + x]

    def get_node(self, index):
        return Node((index%self.x_dim), (index//self.x_dim))

    def get_index(self, coords):
        return coords.y*self.x_dim + coords.x

    def find_path(self, start, end):
        pathlen = [None for _ in self.nodes]
        adjacents = [Node(0, 1), Node(1, 0), Node(-1, 0), Node(0, -1)]

        queue = []
        queue.insert(0, end)
        pathlen[self.get_index(end)] = 0
        while queue != []:
            pos = queue.pop()
            pos_elevation = self[pos]
            for a in adjacents:
                newpos = a + pos
                if newpos.x < 0 or newpos.y < 0 or newpos.x >= self.x_dim or newpos.y >= self.y_dim:
                    continue
                newpos_elevation = self[newpos]
                if pathlen[self.get_index(newpos)] is not None:
                    continue
                if pos_elevation - newpos_elevation <= 1:
                    pathlen[self.get_index(newpos)] = pathlen[self.get_index(pos)] + 1
                    queue.insert(0, newpos)
        return pathlen[self.get_index(start)]


nodes = []
start, end = None, None
with open("day12.txt", "r") as f:
    for idx_y, line in enumerate(f.readlines()):
        line = line.strip()
        for idx_x, char in enumerate(line):
            if char == "S":
                start = Node(idx_x, idx_y)
                nodes.append(0)
            elif char == "E":
                end = Node(idx_x, idx_y)
                nodes.append(26)
            else:
                nodes.append(ord(char) - ord("a"))

heightmap = Heightmap(len(line), idx_y + 1, nodes)
print("Length of shortest path from 'S':", heightmap.find_path(start, end))


nodes0_idx = [i for i in range(len(nodes)) if nodes[i] == 0]
nodes0 = [heightmap.get_node(i) for i in nodes0_idx]

optimum_start = None
optimum_pathlen = 1000000
for node in nodes0:
    pathlen = heightmap.find_path(node, end)
    if pathlen is not None and pathlen < optimum_pathlen:
            optimum_pathlen = pathlen
            optimum_start = node

print("Length of shortest path from 'a':", optimum_pathlen)