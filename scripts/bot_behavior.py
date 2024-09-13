import gymnasium as gym
from scripts.gym_env import StrategyGameEnv

def run_bot():
    """
    Run the bot by interacting with the custom gym environment.
    The bot will take actions in the environment and receive rewards.
    """
    env = StrategyGameEnv()
    state = env.reset()
    
    done = False
    total_reward = 0
    
    while not done:
        # Here, you can use an AI model or a simple rule-based system to choose actions
        # For now, let's take random actions as a placeholder
        action = env.action_space.sample()
        
        # Take the action in the environment
        next_state, reward, done, info = env.step(action)
        
        total_reward += reward
        state = next_state
        
        # Optionally render the environment
        env.render()
    
    print(f"Total reward after the game: {total_reward}")
    env.close()

