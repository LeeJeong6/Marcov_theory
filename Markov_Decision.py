import numpy as np
import random
import matplotlib.pyplot as plt

def gamblers_mdp(policy):
    """
    Implements a gambler's ruin scenario using MDP.
    Args:
        policy: Function that determines betting amount based on current money.
    Returns:
        List of money amounts over time.
    """
    gambling_money = 50  
    gambling_goal = 100  
    gambling_situations = []
    
    while 0 < gambling_money < gambling_goal:
        bet_size = policy(gambling_money)  # Choose bet based on policy
        win_or_lose = random.choice([-1, 1])  # 50% probability of winning or losing
        gambling_money += bet_size * win_or_lose
        gambling_situations.append(gambling_money)
    
    return gambling_situations

def random_policy(state):
    """ Randomly chooses a bet size (1, 2, or 5). """
    return random.choice([1, 2, 5])

def greedy_policy(state):
    """ Bets half of the current money (aggressive strategy). """
    return max(1, state // 2)

def simulate_gamblers_mdp(num_simulations, policy):
    """
    Runs multiple simulations to observe the average outcome.
    """
    results = [gamblers_mdp(policy)[-1] for _ in range(num_simulations)]
    print(f"Average final money after {num_simulations} simulations: {np.mean(results)}")

def draw_gambler_mdp(policy):
    """
    Plots the progression of a single gambler's money.
    """
    plt.plot(gamblers_mdp(policy))
    plt.title("Gambling Simulation (MDP)")
    plt.xlabel("Number of Bets")
    plt.ylabel("Gambler's Money")
    plt.axhline(y=0, color='r', linestyle='-')
    plt.axhline(y=100, color='black', linestyle='-')
    plt.savefig("MDP_greedy.jpg")
    plt.show()

if __name__ == "__main__":
    simulate_gamblers_mdp(100, random_policy)  # Run 100 simulations with random policy
    draw_gambler_mdp(greedy_policy)  # Visualize policy [random_policy or greedy policy]
