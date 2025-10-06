import gymnasium as gym

# Create environment
env = gym.make("CartPole-v1", render_mode="human")  # "human" to see animation

# Run 5 episodes
for episode in range(5):
    state, info = env.reset()
    done = False
    total_reward = 0

    while not done:
        env.render()

        # Random action (0 = left, 1 = right)
        action = env.action_space.sample()

        # Step environment
        next_state, reward, terminated, truncated, info = env.step(action)

        total_reward += reward
        state = next_state
        done = terminated or truncated  # Gymnasium separates these flags

    print(f"Episode {episode+1} reward: {total_reward}")

env.close()
