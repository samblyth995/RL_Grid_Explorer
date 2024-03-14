class GridEnvironment:
    def __init__(self, grid_size=(6, 6), obstacles=[(1, 1)]):
        self.grid_size = grid_size
        self.obstacles = obstacles
        self.agent_position = (0, 0)  # Agent starts at top-left corner
        self.goal_position = (5,5)  # stores the position of the goal # old code : self.goal_position = (grid_size[0] - 1, grid_size[1] - 1)
        self.done=False
        self.reward=0
    def move_agent(self, action):
        """
        Move the agent based on the action.
        Actions:
        0 - Up
        1 - Right
        2 - Down
        3 - Left
        """
        x, y = self.agent_position
        if action == 0 and x > 0:  #up
            x -= 1
        elif action == 1 and y < self.grid_size[1] - 1: #right
            y += 1
        elif action == 2 and x < self.grid_size[0] - 1: #Down
            x += 1
        elif action == 3 and y > 0: #left
            y -= 1
        # Check if the new position is not an obstacle
        #if (x, y) not in self.obstacles:
        self.agent_position = (x, y)
    
    def is_goal_reached(self):
        """
        Check if the agent has reached the goal (bottom-right corner).
        """
        return self.agent_position == self.goal_position
    def get_reward(self):
        """
        Get the reward based on the current state of the environment.
        """
        if self.is_goal_reached():
            done=True
            reward=5
            return reward, done
        elif self.agent_position in self.obstacles:
            done=False
            reward=-1
            return reward, done
        else:
            done =False
            reward=0
            return reward, done

    def get_possible_actions(self):
        """
        Get the possible actions the agent can take.
        """
        possible_actions = []
        x, y = self.agent_position
        if x > 0:
            possible_actions.append(0)  # Up
        if x < self.grid_size[0] - 1:
            possible_actions.append(2)  # Down
        if y < self.grid_size[1] - 1:
            possible_actions.append(1)  # Right
        if y > 0:
            possible_actions.append(3)  # Left
        return possible_actions     

    
    def print_grid(self):
        """
        Print the grid with agent and obstacles.
        """
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                if (i, j) == self.agent_position:
                    print('A', end=' ')
                elif (i, j) in self.obstacles:
                    print('X', end=' ')
                else:
                    print('.', end=' ')
            print()
   

    def reset(self):
        self.agent_position = (0, 0)  # Reset agent position to start
        return self.agent_position  # Return the initial state


# Test the environment
if __name__ == "__main__":
    env = GridEnvironment()
    env.print_grid()
    # initial_position = env.agent_position
    # print(f"Initial Position: {initial_position}")

    # action = 1
    # env.move_agent(action)
    # after_move_position = env.agent_position
    # print(f"After Action {action}, New Position: {after_move_position}")
    # env.print_grid()

    # action = 0
    # env.move_agent(action)
    # after_move_position = env.agent_position
    # print(f"After Action {action}, New Position: {after_move_position}")
    # env.print_grid()

    # action = 3
    # env.move_agent(action)
    # after_move_position = env.agent_position
    # print(f"After Action {action}, New Position: {after_move_position}")
    # env.print_grid()

    # action = 2
    # env.move_agent(action)
    # after_move_position = env.agent_position
    # print(f"After Action {action}, New Position: {after_move_position}")
    # env.print_grid()

    # action = 2
    # env.move_agent(action)
    # after_move_position = env.agent_position
    # print(f"After Action {action}, New Position: {after_move_position}")
    # env.print_grid()

    # action = 1
    # env.move_agent(action)
    # after_move_position = env.agent_position
    # print(f"After Action {action}, New Position: {after_move_position}")
    # env.print_grid()

    # action = 1
    # env.move_agent(action)
    # after_move_position = env.agent_position
    # print(f"After Action {action}, New Position: {after_move_position}")
    # env.print_grid()

    # action = 1
    # env.move_agent(action)
    # after_move_position = env.agent_position
    # print(f"After Action {action}, New Position: {after_move_position}")
    # env.print_grid()

    # if env.is_goal_reached():
    #     print("Goal reached")
    # else:
    #     print("Goal not reached")