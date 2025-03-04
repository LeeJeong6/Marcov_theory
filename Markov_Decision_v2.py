import numpy as np
import matplotlib.pyplot as plt
import random

def gamblers_mdp(policy, loss_prob=None, discount_factor=0.9):
    """
    Implements a gambler's ruin scenario using MDP with discounted rewards.
    
    Args:
        policy: Function that determines betting amount based on current money.
        loss_prob: Probability of losing the bet (used in risky policy).
        discount_factor: Discount factor for future rewards.
    
    Returns:
        List of discounted cumulative rewards over time.
    """
    gambling_money = 100  
    times = 0
    rewards = []
    total_discounted_reward = 0  

    while times < 50:
        bet_size = policy(gambling_money)  
        
        if loss_prob is None:
            win_or_lose = random.choice([-1, 1])  
        else:
            win_or_lose = random.choices([-1, 1], weights=[loss_prob, 1 - loss_prob])[0]

        reward = bet_size * win_or_lose 
        discounted_reward = (discount_factor ** times) * reward  
        total_discounted_reward += discounted_reward  

        gambling_money += reward  
        gambling_money = max(0, gambling_money) 

        rewards.append(total_discounted_reward)  
        times += 1

    return rewards


def random_policy(state):
    """ Randomly chooses a bet size (1, 2, or 5). """
    return random.choice([1, 2, 5])


def greedy_policy(state):
    """ Bets half of the current money (aggressive strategy). """
    return max(1, state // 2)


def simulate_gamblers_mdp(num_simulations, policy, loss_prob=None):
    """
    Runs multiple simulations to observe the average outcome.
    """
    all_results = [gamblers_mdp(policy, loss_prob) for _ in range(num_simulations)]
    
    
    return np.mean(all_results, axis=0)


def draw_comparison_plot():
    """
    Plots and compares the results of random and greedy policies under normal and risky conditions.
    """
    num_simulations = 1
    
    
    random_results = simulate_gamblers_mdp(num_simulations, random_policy)
    greedy_results = simulate_gamblers_mdp(num_simulations, greedy_policy)
    risky_results = simulate_gamblers_mdp(num_simulations, greedy_policy, loss_prob=0.52)

    plt.figure(figsize=(10, 8))

    plt.subplot(3, 1, 1)
    plt.plot(random_results, label="Random Policy", color="blue")
    plt.ylabel("Discounted Reward")
    plt.title("Random Policy (50% Win/Loss)")
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(greedy_results, label="Greedy Policy", color="green")
    plt.ylabel("Discounted Reward")
    plt.title("Greedy Policy (50% Win/Loss)")
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(risky_results, label="Risky Greedy Policy", color="red")
    plt.ylabel("Discounted Reward")
    plt.xlabel("Rounds")
    plt.title("Greedy Policy (Risky: 52% Lose Probability)")
    plt.legend()

    plt.tight_layout()
    plt.savefig("Markov_Decision_add_return.jpg")
    plt.show()


if __name__ == "__main__":
    draw_comparison_plot()  # Compare random, greedy, and risky greedy policies
