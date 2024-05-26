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
        board_array = state.state
        for x, y in self.corners:
            if board_array[y][x] == -1:
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
    # Get corners and board matrix
    corners = problem.corners
    board_matrix = state.state

    # Initialize variables
    uncovered_corners = 0
    pieces = problem.piece_list.pieces
    min_piece_size = math.inf

    # Find the minimum piece size
    for p in pieces:
        min_piece_size = min(min_piece_size, p.num_tiles)

    # Count the number of uncovered corners
    for corner_x, corner_y in corners:
        if board_matrix[corner_y][corner_x] == 0:  # This corner is already covered
            continue
        uncovered_corners += 1

    # Calculate a multiplicative factor based on the minimum piece size and board size
    mult_factor = min(min_piece_size, (min(problem.board_h, problem.board_w) + 1) / 2.0)

    # Return the heuristic value
    return mult_factor * uncovered_corners



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


def blokus_cover_heuristic(state, problem):
    "*** YOUR CODE HERE ***"
    # TODO: write this
