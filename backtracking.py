class State:
    def __init__(self, state_name, colors):
        self.name = state_name  # name of the region
        self.final_color = ''
        self.domain = colors  # domain values for each region
        self.neighbors = 0


class CSP:
    def __init__(self):
        self.N = 0
        self.d = 0
        self.regions = []
        self.colors = []
        self.map = []
        self.state_tracker = []

    def select_unassigned_variable(self, csp, assignment):
        """
        Which variable should be assigned next?
        minimum remaining value heuristic : chooses variable with the smallest domain
        degree heuristic : chooses variable with the largest number of unassigned neighbors
        """
        ...

    def inference(self, index_of_state, assign_color):
        """
        What inferences should be performed at each step in the search?
        apply forward checking
        """
        constr_of_curr_state = self.map[index_of_state]
        # modify domain values for the adjacent states
        # modify the number of unassigned variables
        # inferences fail when domain of neighbor is empty

        for ii in range(len(constr_of_curr_state)):
            if constr_of_curr_state[ii] == '1':  # indicates adjacent state
                if self.state_tracker[ii].final_color == '' and self.state_tracker[ii].domain == [assign_color]:
                    return -1  # failure!
                else:
                    self.state_tracker[ii].domain.remove(assign_color)




    def backtrack(self, csp, assignment):
        ...

    def backtracking_search(self, csp):
        ...

    def read_file(self, file_name):
        """
        input: file
        returns NxN array that will be used in the backtracking algorithm
        """

        with open(file_name, "r") as f:
            line_1 = f.readline().strip('\n').split(" ")
            self.N, self.d = line_1[0], line_1[1]  # number of variables and number of domain values
            self.regions = f.readline().strip('\n').split(" ")  # list of variable names

            self.colors = f.readline().strip('\n').split(" ")  # list of domain values

            for i in range(self.N):  # reading NxN array
                self.map.append(f.readline().strip('\n').split(" "))

            # initializes object of type state
            for ii in range(len(self.regions)):
                state = State(self.regions[ii], self.colors)
                state.neighbors = self.map[ii].count('1')
                self.state_tracker.append(state)


def main():
    f = input("Enter input file name: ")
    csp = CSP()
    csp.read_file(f)
