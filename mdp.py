import numpy as np
class MDP:
    def __init__(self, maze):
        self.maze = maze
        self.states = [(x, y) for x in range(maze.width) for y in range(maze.height)]
        self.actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.gamma = 0.99

    def reward(self, state):
        if state == self.maze.goal:
            return 1.0
        else:
            return 0.0

    def transition_probs(self, state, action):
        next_state = tuple(np.array(state) + np.array(action))
        if next_state not in self.states or self.maze[next_state] == '#':
            return [(1.0, state)]
        else:
            return [(1.0, next_state)]


    def policy_iteration(maze):
        mdp = MDP(maze)

        pi = {s: mdp.actions[0] for s in mdp.states}
        while True:
            # Policy evaluation
            V = {s: 0.0 for s in mdp.states}
            eps = 1e-10
            while True:
                delta = 0
                for s in mdp.states:
                    v = V[s]
                    V[s] = sum(prob * (mdp.reward(next_state) + mdp.gamma * V[next_state]) for prob, next_state in
                               mdp.transition_probs(s, pi[s]))
                    delta = max(delta, abs(v - V[s]))
                if delta < eps:
                    break

            # Policy improvement
            policy_stable = True
            for s in mdp.states:
                old_action = pi[s]
                pi[s] = max(mdp.actions, key=lambda a: sum(
                    prob * (mdp.reward(next_state) + mdp.gamma * V[next_state]) for prob, next_state in
                    mdp.transition_probs(s, a)))
                if pi[s] != old_action:
                    policy_stable = False
            if policy_stable:
                break

        # Find shortest path and search path using pi
        start = maze.start
        goal = maze.goal
        path = [start]
        search_path = [start]
        while path[-1] != goal:
            next_state = tuple(np.array(path[-1]) + np.array(pi[path[-1]]))
            path.append(next_state)
            search_path.append(next_state)
        return search_path,path

    def value_iteration(maze):
        mdp = MDP(maze)

        V = {s: 0.0 for s in mdp.states}
        eps = 1e-10
        while True:
            delta = 0
            for s in mdp.states:
                v = V[s]
                V[s] = max(sum(prob * (mdp.reward(next_state) + mdp.gamma * V[next_state]) for prob, next_state in
                               mdp.transition_probs(s, a)) for a in mdp.actions)
                delta = max(delta, abs(v - V[s]))
            if delta < eps:
                break

        # Find shortest path and search path using V
        start = maze.start
        goal = maze.goal
        path = [start]
        search_path = [start]
        while path[-1] != goal:
            next_state = tuple(np.array(path[-1]) + np.array(max(mdp.actions, key=lambda a: sum(
                prob * (mdp.reward(next_state) + mdp.gamma * V[next_state]) for prob, next_state in
                mdp.transition_probs(path[-1], a)))))
            path.append(next_state)
            search_path.append(next_state)
        return search_path,path