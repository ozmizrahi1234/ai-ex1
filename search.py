# """
# In search.py, you will implement generic search algorithms
# """
#
# import util
# from util import Stack
# from util import Queue
# from util import PriorityQueueWithFunction
# from util import PriorityQueueWithFunction
#
#
# class Node:
#     def __init__(self, state, actions, cost):
#         self.state = state
#         self.actions = actions
#         self.cost = cost
#
#     def get_state(self):
#         return self.state
#
#     def set_state(self, state):
#         self.state = state
#
#     def get_actions(self):
#         return self.actions
#
#     def set_actions(self, actions):
#         self.actions = actions
#
#     def get_cost(self):
#         return self.cost
#
#     def set_cost(self, cost):
#         self.cost = cost
#
#     def __lt__(self, other):
#         return self.cost < other.cost
#
#     def __eq__(self, other):
#         return self.cost == other.cost
#
#     def __hash__(self):
#         return hash(self.state)
#
#     def __str__(self):
#         return str(self.state)
#
#     def __repr__(self):
#         return str(self.state)
#
#
# class SearchProblem:
#     """
#     This class outlines the structure of a search problem, but doesn't implement
#     any of the methods (in object-oriented terminology: an abstract class).
#
#     You do not need to change anything in this class, ever.
#     """
#
#     def get_start_state(self):
#         """
#         Returns the start state for the search problem
#         """
#         util.raiseNotDefined()
#
#     def is_goal_state(self, state):
#         """
#         state: Search state
#
#         Returns True if and only if the state is a valid goal state
#         """
#         util.raiseNotDefined()
#
#     def get_successors(self, state):
#         """
#         state: Search state
#
#         For a given state, this should return a list of triples,
#         (successor, action, stepCost), where 'successor' is a
#         successor to the current state, 'action' is the action
#         required to get there, and 'stepCost' is the incremental
#         cost of expanding to that successor
#         """
#         util.raiseNotDefined()
#
#     def get_cost_of_actions(self, actions):
#         """
#         actions: A list of actions to take
#
#         This method returns the total cost of a particular sequence of actions.  The sequence must
#         be composed of legal moves
#         """
#         util.raiseNotDefined()
#
#
# # class Node2:
# #     def __init__(self, state):
# #         self.state = state
# #         self.cost = 0
# #         self.list_of_actions = []
# #
# #     def add_actions(self, actions):
# #         self.list_of_actions.extend(actions)
# #
# #     def get_cost(self):
# #         return self.cost
# #
# #     def get_state(self):
# #         return self.state
# #
# #     def __eq__(self, other):
# #         return self.state == other.state
# #
# #     def __hash__(self):
# #         return hash(self.state)
#
#
# # TODO: change data_structure to generic, delete node2, check the code again and write the resultsn
# def generic_search(problem, generic):
#     """
#     Search the node by the generic data structure type (e.g. stack, queue, fringe etc.)
#     """
#     visited = set()
#     start = Node(problem.get_start_state(), [], 0)
#     generic.push(start)
#
#     while not generic.isEmpty():
#
#         node = generic.pop()
#
#         if problem.is_goal_state(node.get_state()):
#             return node.get_actions() + [node.get_state()]
#
#         if node.get_state() not in visited:
#             visited.add(node.get_state())
#
#             for successor, action, cost in problem.get_successors(node.get_state()):
#                 new_node = Node(successor, node.get_actions() + [action], node.get_cost() + cost)
#                 generic.push(new_node)
#     return []
#
#     # visited = set()
#     # current_node = Node2(problem.get_start_state())
#     # data_structure.push(current_node)
#     # while data_structure:
#     #     current_node: Node2 = data_structure.pop()
#     #
#     #     if problem.is_goal_state(current_node.state):
#     #         return current_node.list_of_actions
#     #
#     #     if current_node in visited:
#     #         continue
#     #
#     #     for state in problem.get_successors(current_node.state):
#     #         new_node = Node2(state[0])
#     #         new_node.add_actions(current_node.list_of_actions)
#     #         new_node.add_actions([state[1]])
#     #         new_node.cost = current_node.cost + state[2]
#     #         data_structure.push(new_node)
#     #
#     #     visited.add(current_node)
#
#
# def depth_first_search(problem):
#     """
#     Search the deepest nodes in the search tree first.
#
#     Your search algorithm needs to return a list of actions that reaches
#     the goal. Make sure to implement a graph search algorithm.
#
#     To get started, you might want to try some of these simple commands to
#     understand the search problem that is being passed in:
#
#     print("Start:", problem.getStartState())
#     print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
#     print("Start's successors:", problem.getSuccessors(problem.getStartState()))
#     """
#     stack = Stack()
#     return generic_search(problem, stack)
#
#
# def breadth_first_search(problem):
#     """
#     Search the shallowest nodes in the search tree first.
#     """
#     queue = Queue()
#     return generic_search(problem, queue)
#
#
# def uniform_cost_search(problem: SearchProblem):
#     """
#     Search the node of-least total cost first.
#     """
#     fringe = PriorityQueueWithFunction(lambda node: node.get_cost())
#     return generic_search(problem, fringe)
#
#
# def null_heuristic(state, problem=None):
#     """
#     A heuristic function estimates the cost from the current state to the nearest
#     goal in the provided SearchProblem.  This heuristic is trivial.
#     """
#     return 0
#
#
# def a_star_search(problem, heuristic=null_heuristic):
#     """
#     Search the node that has the lowest combined cost and heuristic first.
#     """
#     "*** YOUR CODE HERE ***"
#     fringe = PriorityQueueWithFunction(lambda node: node.get_cost() + heuristic(node.get_state(), problem))
#     return generic_search(problem, fringe)
#
#
# # Abbreviations
# bfs = breadth_first_search
# dfs = depth_first_search
# astar = a_star_search
# ucs = uniform_cost_search

"""
In search.py, you will implement generic search algorithms
"""

import util
from util import Stack
from util import Queue
from util import PriorityQueueWithFunction
from util import PriorityQueueWithFunction


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def is_goal_state(self, state):
        """
        state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def get_successors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def get_cost_of_actions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


class Node:
    def __init__(self, state, actions, cost):
        self.state = state
        self.actions = actions
        self.cost = cost

    # make getter and setter methods for the state, actions, and cost
    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def get_actions(self):
        return self.actions

    def set_actions(self, actions):
        self.actions = actions

    def get_cost(self):
        return self.cost

    def set_cost(self, cost):
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.cost == other.cost

    def __hash__(self):
        return hash(self.state)

    # def __str__(self):
    #     return str(self.state)

    # def __repr__(self):
    #     return str(self.state)


def generic_search(problem, generic):
    """
    Search the node by the generic data structure type (e.g. stack, queue, fringe etc.)
    """
    visited = set()
    start = Node(problem.get_start_state(), [], 0)
    generic.push(start)
    while not generic.isEmpty():
        node = generic.pop()
        if problem.is_goal_state(node.get_state()):
            return node.get_actions()
        if node.get_state() not in visited:
            for successor, action, cost in problem.get_successors(node.get_state()):
                generic.push(Node(successor, node.get_actions() + [action], node.get_cost() + cost))
            visited.add(node.get_state())
    return []


def depth_first_search(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches
    the goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    stack = Stack()
    return generic_search(problem, stack)


def breadth_first_search(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    queue = Queue()
    return generic_search(problem, queue)


def uniform_cost_search(problem: SearchProblem):
    """
    Search the node of-least total cost first.
    """
    fringe = PriorityQueueWithFunction(lambda node: node.get_cost())
    return generic_search(problem, fringe)


def null_heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def a_star_search(problem, heuristic=null_heuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    fringe = PriorityQueueWithFunction(lambda node: node.get_cost() + heuristic(node.get_state(), problem))
    # fringe = PriorityQueueWithFunction(_)
    return generic_search(problem, fringe)


# Abbreviations
bfs = breadth_first_search
dfs = depth_first_search
astar = a_star_search
ucs = uniform_cost_search
