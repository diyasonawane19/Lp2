class Node:
    def __init__(self, data, level, fval):
        """Initialize the node with the data, level, and f-value"""
        self.data = data
        self.level = level
        self.fval = fval

    def generate_child(self):
        """Generate child nodes by moving the blank space"""
        x, y = self.find(self.data, '_')

        # Possible moves: left, right, up, down
        val_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]

        children = []
        for i in val_list:
            child = self.shuffle(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.level + 1, 0)
                children.append(child_node)

        return children

    def shuffle(self, puz, x1, y1, x2, y2):
        """Move blank space if within bounds"""
        if 0 <= x2 < len(self.data) and 0 <= y2 < len(self.data):
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None

    def copy(self, root):
        """Create a deep copy of the puzzle"""
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    def find(self, puz, x):
        """Find position of blank space"""
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if puz[i][j] == x:
                    return i, j


class Puzzle:
    def __init__(self, size):
        """Initialize puzzle size and lists"""
        self.n = size
        self.open = []
        self.closed = []

    def accept(self):
        """Accept puzzle input"""
        puz = []
        for i in range(self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    def f(self, start, goal):
        """f(x) = h(x) + g(x)"""
        return self.h(start.data, goal) + start.level

    def h(self, start, goal):
        """Calculate number of misplaced tiles"""
        temp = 0
        for i in range(self.n):
            for j in range(self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp

    def process(self):
        """Run the puzzle solver"""
        print("Enter the start state matrix:\n")
        start = self.accept()

        print("Enter the goal state matrix:\n")
        goal = self.accept()

        start = Node(start, 0, 0)
        start.fval = self.f(start, goal)

        self.open.append(start)

        print("\n\n")

        while True:
            cur = self.open[0]

            print("")
            print(" | ")
            print(" | ")
            print(" \\/ \n")

            for i in cur.data:
                for j in i:
                    print(j, end=" ")
                print("")

            # Goal check
            if self.h(cur.data, goal) == 0:
                break

            # Generate children
            for i in cur.generate_child():
                i.fval = self.f(i, goal)
                self.open.append(i)

            self.closed.append(cur)
            del self.open[0]

            # Sort by f-value
            self.open.sort(key=lambda x: x.fval)


# Run the program
puz = Puzzle(3)
puz.process()
