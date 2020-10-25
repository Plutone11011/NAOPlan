from collections import OrderedDict
import numpy as np

from robot.constants import JOINT_NAMES, STAND_ZERO


class NaoState:
    """the Nao state is an ordered dict of joint names as keys
    and their current coordinates as values. The keys are ordered
    to provide consistency between operations with different states.
    Subclass this if you want a state for a specific posture (see StandZero)"""
    def __init__(self, motion_proxy, nao_state=None):
        # if nao state is defined, it's one of the mandatory predefined positions
        print '{'
        if not nao_state:
            nao_state = {}
            for joint_name in JOINT_NAMES:
                nao_state[joint_name] = motion_proxy.getPosition(joint_name, 1, True)[:3]
                print joint_name + ': array(' + str(nao_state[joint_name]) + '),'
        print '}'
        self.state = OrderedDict(sorted(nao_state.items(), key=lambda t: t[0]))

    def get_joint_coordinate(self, joint_name):
        return self.state[joint_name]


# subclassing for the goal states
class StandZero(NaoState):

    def __init__(self, motion_proxy):
        NaoState.__init__(self, motion_proxy, STAND_ZERO)


class NaoProblem:
    """We define a NaoProblem for each subsequence of actions between
    a mandatory pose P_i and the next P_i+1. This means that, in each NaoProblem
    the initial state will be the state in pose P_i and the goal will be the state in pose P_i+1
    Subclass this class to create an instance of a particular Nao subproblem"""
    def __init__(self, initial_state, goal):
        self.initial_state = initial_state
        self.goal = goal

    def actions(self, state):
        """Executable actions in the state"""
        pass

    def result(self, state, action):
        """The state that results from executing this action in this state."""
        pass

    def goal_test(self, state):
        """Checks whether the given state is a goal"""
        pass

    def is_valid(self, state):
        """Checks whether the state is a valid one based on some constraints
            - time constraint
            - each NaoProblem must feature a position in the set of intermediate positions
            - other incompatibilities arisen from testing"""
        pass

    def path_cost(self, state1, action, state2, paid_cost):
        """Returns path cost from state1 to state2
        with action, assuming a certain paid cost """
        pass

    def h(self, nao_state):
        """The heuristic for each state computes the
        euclidean distance between the current joints coordinates
        and the joint coordinates of the goal. This heuristic is admissible
        because Nao can't actually reach the goal without covering at least that distance"""
        # possibly add speed/time in the future
        joints_distances = []
        for joint_coordinates_state, joint_coordinates_goal in zip(nao_state.state.values(), self.goal.state.values()):
            joints_distances.append(np.linalg.norm(joint_coordinates_state - joint_coordinates_goal, ord=2))

        return sum(joints_distances)


# each subproblem defines his own initial state and goal,
# as well as actions and results
# heuristic is common to all problems, as well as path cost
class NaoProblemP0P1(NaoProblem):

    def __init__(self, initial_state, goal):
        NaoProblem.__init__(initial_state, goal)

    def actions(self, state):
        # still to define
        pass

    def result(self, state, action):
        # still to define
        pass

    def goal_test(self, state):
        # still to define
        pass

    def is_valid(self, state):
        # still to define
        pass


class NaoNode:
    """The NaoNode knows the parent, the action with which it was generated,
    its state and the path_cost(g)"""
    def __init__(self, state, parent=None, action=None, path_cost=None):
        """Create a search tree Node, derived from a parent by an action."""
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def expand(self, problem):
        """Defines nodes reachable from this one in one step"""
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        """Returns child node of this node of a certain problem
        generated by action"""
        next_state = problem.result(self.state, action)
        next_node = NaoNode(next_state, self, action, problem.path_cost(self.path_cost, self.state, action, next_state))
        return next_node

    def solution(self):
        """Return the sequence of actions to go from the root to this node."""
        return [node.action for node in self.path()[1:]]

    def path(self):
        """Return a list of nodes forming the path from the root to this node."""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))


