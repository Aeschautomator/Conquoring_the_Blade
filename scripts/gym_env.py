import gymnasium as gym
import numpy as np

class StrategyGameEnv(gym.Env):
    """Custom Environment for the Strategy Game Bot."""
    
    metadata = {'render.modes': ['human']}
    
    def __init__(self):
        super(StrategyGameEnv, self).__init__()
        
        # Define action and observation space
        # Actions: [0: Move Up, 1: Move Down, 2: Move Left, 3: Move Right, 4: Command Unit Follow, 5: Command Unit Attack]
        self.action_space = gym.spaces.Discrete(6)
        
        # Observations: Could be a vector representing the state of the game (hero position, unit status, enemy status)
        self.observation_space = gym.spaces.Box(low=0, high=255, shape=(10,), dtype=np.float32)
        
        # Initial game state
        self.state = np.zeros(10)
        self.hero_health = 100
        self.unit_health = 100
        self.enemies_killed = 0
    
    def step(self, action):
        """
        Execute the action in the environment and return:
        - next_state: The next state after the action
        - reward: The reward for the action
        - done: Whether the episode has ended
        - info: Extra information (if any)
        """
        if action == 0:
            # Move hero up
            self.state[0] += 1
        elif action == 1:
            # Move hero down
            self.state[0] -= 1
        elif action == 2:
            # Move hero left
            self.state[1] -= 1
        elif action == 3:
            # Move hero right
            self.state[1] += 1
        elif action == 4:
            # Command unit to follow hero
            self.state[2] = 1  # Set unit to follow mode
        elif action == 5:
            # Command unit to attack enemies
            self.enemies_killed += 1
            self.state[3] = self.enemies_killed
        
        # Reward system: More enemies killed = more rewards
        reward = self.enemies_killed
        
        # Check if game is done (e.g., mission complete, hero or unit death)
        done = self.hero_health <= 0 or self.enemies_killed >= 150
        
        # Return the next state, reward, whether done, and info
        return np.array(self.state, dtype=np.float32), reward, done, {}
    
    def reset(self):
        """Reset the environment to an initial state and return the initial observation."""
        self.state = np.zeros(10)
        self.hero_health = 100
        self.unit_health = 100
        self.enemies_killed = 0
        return np.array(self.state, dtype=np.float32)
    
    def render(self, mode='human'):
        """Render the environment (optional)."""
        print(f"Hero Position: {self.state[:2]}, Enemies Killed: {self.enemies_killed}")
    
    def close(self):
        """Close the environment (optional)."""
        pass
