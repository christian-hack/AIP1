# search.py
# ---------
# This codebase is adapted from UC Berkeley AI. Please see the following information about the license.

# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # initialize dict for storing popped (visited) nodes
    visited = {}
    # initialize dict for parent nodes
    parent = {}
    # initialize list var for storing solution path
    spath = []
    # initialize Queue for storing tuplets containing [name, direction, cost]
    queue = util.Queue()
    # store start state to var // oof
    start = problem.getStartState()
    # append starting node/state to Queue
    queue.push((start, 'null', 0))
    # set starting node/state direction to null
    visited[start] = 'null'
    # ensure start state is not goal state
    if problem.isGoalState(start):
        return spath
    # create loop to continue until queue reaches end // add a conditional to cover case of goal being reached
    isGoal = False
    while (queue.isEmpty() is False and isGoal is False):
        # assign what's being popped off of queue to m
        m = queue.pop()
        # print stmnts to keep track of successors
        # print("Start's successors:", problem.getSuccessors(m))
        # print(m, end = " ")

        # store direction/node
        visited[m[0]] = m[1]
        # check if goal is reached
        if problem.isGoalState(m[0]):
            snode = m[0]
            isGoal = True
            break

        # assign successors of node to var
        sucs = problem.getSuccessors(m[0])
         # loop through successors of current state to check for existence in visited
        # if state not found in visited, store parent and successor nodes
        for successor in sucs:
            if successor[0] not in parent.keys() and successor[0] not in visited.keys():
                parent[successor[0]] = m[0]
                queue.push(successor)

    # find/store solution
    # obtain parent node
    # prepend to spath
    while (snode in parent.keys()):
        oldS = parent[snode]
        spath.insert(0, visited[snode])
        snode = oldS
    return spath
    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
