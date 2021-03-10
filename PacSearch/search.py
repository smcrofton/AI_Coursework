# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# (4) you provide clear attribution to RowanRobots: http://www.rowan.edu/robots
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

#
# Python2 to Python3 conversion and some other customization 
# by Jennifer Kay kay@rowan.edu
#






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
    """
    from util import Stack

    frontier = Stack()
    explored = []

    """
    Works by taking the list of successor values from the start node, then looking
    at that successor values' node's successors and so on.
    """

    #Set the start successor value containing the start node, then push it to frontier.
    n = problem.getStartState()
    s = (n, None, None)

    frontier.push([s])

    while frontier.isEmpty:
        """
        Pop the frontier and set that to the current successor list, 
        then add that node to the explored list
        """
        currentSuccessorList = frontier.pop()
        lastSuccessor = currentSuccessorList[len(currentSuccessorList) - 1]

        explored.append(lastSuccessor[0])

        """
        If we find that the last node in the successor list is the Goal,
        we iterate through the current successor list, grabbing all the
        directional values and return the solution to the maze.
        """

        if problem.isGoalState(lastSuccessor[0]):

            solution = []
            for i in currentSuccessorList:

                if i[1] != None:

                    solution.append(i[1])

            return solution

        """
        If we don't find the goal, we get all the possible successors to the
        last node in the current successor list, then push all the possible paths from that node 
        with nodes we have not explored yet to the frontier, then start over again 
        with whatever list of successors is on top of the frontier stack.
        """

        for i in problem.getSuccessors(lastSuccessor[0]):
            
            if (i[0] not in explored):

                tempList = currentSuccessorList.copy()
                tempList.append(i)
                frontier.push(tempList)

    print("lol")

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    from util import Queue

    frontier = Queue()
    explored = []

    """
    Works by taking the list of successor values from the start node, then looking
    at that successor values' node's successors and so on.
    """

    #Set the start successor value containing the start node, then push it to frontier.
    n = problem.getStartState()
    s = (n, None, None)

    frontier.push([s])

    while frontier.isEmpty:
        """
        Pop the frontier and set that to the current successor list, 
        then add that node to the explored list
        """
        currentSuccessorList = frontier.pop()
        lastSuccessor = currentSuccessorList[len(currentSuccessorList) - 1]

        """
        Now we check if our last successor node is in our explored,
        if it IS; we skip, pruning this path
        if it IS NOT; we add it to our explored, check if its our goal node,
        and then add it's successor values to our queue
        """

        if lastSuccessor[0] not in explored:
            explored.append(lastSuccessor[0])

            #Goal check
            if problem.isGoalState(lastSuccessor[0]):
                solution = []

                #solution maker
                for i in currentSuccessorList:
                    if i[1] != None:

                        solution.append(i[1])

                return solution
 
            #Path Population to queue.
            for i in problem.getSuccessors(lastSuccessor[0]):
            
                if (i[0] not in explored):


                    tempList = currentSuccessorList.copy()
                    tempList.append(i)
                    frontier.push(tempList)


def lowestCostFirstSearch(problem):
    """
    Search the lowest cost paths in the search tree first.
    """
    from util import PriorityQueue

    frontier = PriorityQueue()
    explored = []

    """
    Works by taking the list of successor values from the start node, then looking
    at that successor values' node's successors and so on.
    """

    #Set the start successor value containing the start node, then push it to frontier.
    n = problem.getStartState()
    s = (n, None, 0.0)

    frontier.push([s], 0.0)

    while frontier.isEmpty:
        """
        Pop the frontier and set that to the current successor list, 
        then add that node to the explored list
        """
        currentSuccessorList = frontier.pop()
        lastSuccessor = currentSuccessorList[len(currentSuccessorList) - 1]

        """
        Now we check if our last successor node is in our explored,
        if it IS; we skip, pruning this path
        if it IS NOT; we add it to our explored, check if its our goal node,
        and then add it's successor values to our queue
        """

        if lastSuccessor[0] not in explored:
            explored.append(lastSuccessor[0])

            #Goal check
            if problem.isGoalState(lastSuccessor[0]):
                solution = []

                #solution maker
                for i in currentSuccessorList:
                    if i[1] != None:

                        solution.append(i[1])

                return solution
 
            """
            When we update our Priority Queue, we need to give it a priority value,
            so we simply iterate through our current successor list's path costs
            adding them together as our priority.

            We push our current list with the iterated priority value,
            """
            for i in problem.getSuccessors(lastSuccessor[0]):
            
                if (i[0] not in explored):

                    tempList = currentSuccessorList.copy()
                    tempList.append(i)

                    priority = 0
                    for successor in tempList:
                        priority += successor[2]

                    frontier.update(tempList, priority)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the lowest cost paths in the search tree first.
    """
    from util import PriorityQueue

    frontier = PriorityQueue()
    explored = []

    """
    Works by taking the list of successor values from the start node, then looking
    at that successor values' node's successors and so on.
    """

    #Set the start successor value containing the start node, then push it to frontier.
    n = problem.getStartState()
    s = (n, None, 0.0)

    frontier.push([s], 0.0)

    while frontier.isEmpty:
        """
        Pop the frontier and set that to the current successor list, 
        then add that node to the explored list
        """
        currentSuccessorList = frontier.pop()
        lastSuccessor = currentSuccessorList[len(currentSuccessorList) - 1]

        """
        Now we check if our last successor node is in our explored,
        if it IS; we skip, pruning this path
        if it IS NOT; we add it to our explored, check if its our goal node,
        and then add it's successor values to our queue
        """

        if lastSuccessor[0] not in explored:
            explored.append(lastSuccessor[0])

            #Goal check
            if problem.isGoalState(lastSuccessor[0]):
                solution = []

                #solution maker
                for i in currentSuccessorList:
                    if i[1] != None:

                        solution.append(i[1])

                return solution
 
            """
            When we update our Priority Queue, we need to give it a priority value,
            so we simply iterate through our current successor list's path costs
            adding them together as our priority.

            We push our current list with the iterated priority value,
            """
            for i in problem.getSuccessors(lastSuccessor[0]):
            
                if (i[0] not in explored):

                    tempList = currentSuccessorList.copy()
                    tempList.append(i)

                    priority = 0
                    for successor in tempList:
                        priority += successor[2]

                    priority += heuristic(i[0], problem)

                    frontier.update(tempList, priority)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
lcfs = lowestCostFirstSearch
