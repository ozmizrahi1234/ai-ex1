import numpy as np
import math
from board import Board
from search import SearchProblem, ucs
import util
from typing import *
import numpy
from typing import List
import util


class BlokusFillProblem(SearchProblem):
    """
    A one-player Blokus game as a search problem.
    This problem is implemented for you. You should NOT change it!
    """

    def __init__(self, board_w, board_h, piece_list, starting_point=(0, 0)):
        self.board = Board(board_w, board_h, 1, piece_list, starting_point)
        self.expanded = 0

    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        return self.board

    def is_goal_state(self, state):
        """
        state: Search state
        Returns True if and only if the state is a valid goal state
        """
        return not any(state.pieces[0])

    def get_successors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        # Note that for the search problem, there is only one player - #0
        self.expanded = self.expanded + 1
        return [(state.do_move(0, move), move, 1) for move in state.get_legal_moves(0)]

    def get_cost_of_actions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        return len(actions)


#####################################################
# This portion is incomplete.  Time to write code!  #
#####################################################
class BlokusCornersProblem(SearchProblem):
    def __init__(self, board_w, board_h, piece_list, starting_point=(0, 0)):
        self.piece_list = piece_list
        self.board_h = board_h
        self.board_w = board_w
        self.expanded = 0
        self.corners = [(board_w - 1, board_h - 1), (board_w - 1, 0), (0, board_h - 1), (0, 0)]
        self.board = Board(board_w, board_h, 1, piece_list, starting_point)

    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        return self.board

    def is_goal_state(self, state):
        """"
        Returns True if and only if the state is a valid goal state
        """
        for x, y in self.corners:
            if state.state[y][x] == -1:
                return False
        return True

    def get_successors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        # Note that for the search problem, there is only one player - #0
        self.expanded = self.expanded + 1
        return [(state.do_move(0, move), move, move.piece.get_num_tiles()) for move in state.get_legal_moves(0)]

    def get_cost_of_actions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        return sum([action.piece.get_num_tiles() for action in actions])


def chebyshev_distance(point1, point2):
    """
    returns the Chevyshev distance between two points.
    """
    return max(abs(point1[0] - point2[0]), abs(point1[1] - point2[1]))


def blokus_corners_heuristic(state, problem):
    """
        A heuristic for the BlokusCornersProblem that you defined.

    This heuristic should be consistent.
    """

def blokus_heuristic_template(state, to_reach: List, corners: bool = False):
    max_value = state.board_h * state.board_w
    min_reach = np.array([max_value for i in to_reach])
    flags = [False for i in to_reach]
    board = state.state
    for xy, element in np.ndenumerate(board):
        if element != -1:
            distances = check_distances_from_points(xy, to_reach, flags)
            min_reach = np.minimum(min_reach, distances)
    for i, flag in enumerate(flags):
        if flag and min_reach[i] != 0:  # Check for false alarm, if the goal is occupied everything is good
            return max_value

    ## --- In the corners there might be max of 1 intercect (with valid pieces).
    ## --- The minimum case that it would happen is with a distance if 4
    if corners:
        if state.board_h != state.board_w:
            return np.max(min_reach)
        res = np.sum(min_reach)
        return res if res < 4 else res - 1
    return np.max(min_reach)


def check_distances_from_points(xy, points: List, flags) -> np.ndarray:
    """
    caclulates the distance between a point xy to all points
    @param xy:
    @param points:
    @return: ndarray with the distance of the point from all the rest of the points
    """
    distances = []
    for i, point in enumerate(points):
        che_dist = chebyshev_distance(xy, point)
        man_dist = util.manhattanDistance(xy, point)
        if man_dist == 1:
            flags[i] = True
        distances.append(che_dist)
    return np.array(distances)


class BlokusCoverProblem(SearchProblem):
    def __init__(self, board_w, board_h, piece_list, starting_point=(0, 0), targets=[(0, 0)]):

        self.targets = targets.copy()
        self.expanded = 0
        self.board = Board(board_w, board_h, 1, piece_list, starting_point)

    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        return self.board

    def is_goal_state(self, state):
        for x, y in self.targets:
            if state.get_position(y, x) == -1:
                return False
        # for x, y in self.targets:
        #     print(f"looking for row number {x} and col number {y}")
        #     if state.get_position(x, y) == -1:
        #         return False
        return True

    def get_successors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        # Note that for the search problem, there is only one player - #0
        self.expanded = self.expanded + 1
        return [(state.do_move(0, move), move, move.piece.get_num_tiles()) for move in state.get_legal_moves(0)]

    def get_cost_of_actions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        return sum([action.piece.get_num_tiles() for action in actions])


def blokus_cover_heuristic(state, problem):
    "*** YOUR CODE HERE ***"
    # TODO: write this
