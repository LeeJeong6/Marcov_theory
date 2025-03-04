import numpy as np
import random
import matplotlib.pyplot as plt

def gamblers_mdp(policy, loss_prob=None):
    """
    Implements a gambler's ruin scenario using MDP.
    Args:
        policy: Function that determines betting amount based on current money.
        loss_prob: Probability of losing the bet (used in new risky policy).
    Returns:
        List of money amounts over time.
    """
    gambling_money = 100  # Initial money
    gambling_goal = 200  # Winning condition
    gambling_situations = []
    
    while 0 < gambling_money < gambling_goal:
        bet_size = policy(gambling_money)  # Choose bet based on policy
        if loss_prob is None:
            win_or_lose = random.choice([-1, 1])  # 50% probability of winning or losing
        else:
            win_or_lose = random.choices([-1, 1], weights=[loss_prob, 1 - loss_prob])[0] # Custom probability for losing and winning
        gambling_money += bet_size * win_or_lose
        gambling_money = max(0, min(gambling_money, gambling_goal))  # Ensure within bounds
        gambling_situations.append(gambling_money)
        
    return gambling_situations


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
    results = [gamblers_mdp(policy, loss_prob)[-1] for _ in range(num_simulations)]
    
    return results

def calculate_win_rate(results):
    return sum(results) / len(results)  /2

def draw_comparison_plot():
    """
    Plots and compares the results of random and greedy policies under normal and risky conditions.
    """
    num_simulations = 1000
    
    # Simulate with random policy and normal 50% win/loss
    random_results = simulate_gamblers_mdp(num_simulations, random_policy)
    random_win_rate = calculate_win_rate(random_results)
    # Simulate with greedy policy and normal 50% win/loss
    greedy_results = simulate_gamblers_mdp(num_simulations, greedy_policy)
    greedy_win_rate = calculate_win_rate(greedy_results)
    # Simulate with greedy policy and risky 52% loss, 48% win probability
    risky_results = simulate_gamblers_mdp(num_simulations, greedy_policy, loss_prob=0.52)
    risky_win_rate = calculate_win_rate(risky_results)

    fig, axes = plt.subplots(1, 3, figsize=(15, 7), sharey=True)  

    
    axes[0].hist(random_results, bins=30, alpha=0.7, color='blue')
    axes[0].set_title(f"Random Policy (50/50)\n Win Rate: {random_win_rate:.2f}%")
    
    axes[0].axvline(x=0, color='r', linestyle='--')
    axes[0].axvline(x=200, color='black', linestyle='--')

    axes[1].hist(greedy_results, bins=30, alpha=0.7, color='green')
    axes[1].set_title(f"Greedy Policy (50/50)\n Win Rate: {greedy_win_rate:.2f}%")
    axes[1].axvline(x=0, color='r', linestyle='--')
    axes[1].axvline(x=200, color='black', linestyle='--')

    axes[2].hist(risky_results, bins=30, alpha=0.7, color='orange')
    axes[2].set_title(f"Greedy Policy (Risky 52% Lose)\n Win Rate: {risky_win_rate:.2f}%")
    axes[2].axvline(x=0, color='r', linestyle='--')
    axes[2].axvline(x=200, color='black', linestyle='--')

    for ax in axes:
        ax.set_xlabel("Final Money")
        ax.set_ylabel("Frequency")

    plt.tight_layout() 
    plt.savefig("Markov_Decision_Result.jpg")
    plt.clf()

if __name__ == "__main__":
    draw_comparison_plot()  # Compare random, greedy, and risky greedy policies
