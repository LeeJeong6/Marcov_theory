'''
Markov Chain Decision
https://www.youtube.com/watch?v=WT6jI8UgROI

This code simulates a gambler's situation.
'''

import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt

def gamblers_ruin():
    '''
    The gambler has a 50% chance of winning or losing each bet.
    The game ends when the gambler either reaches $100 or loses all their money.
    
    Returns:
        A list representing the gambler's money progression throughout the game.
    '''
    gambling_money = 100
    gambling_goal = 200
    gambling_situations = []

    while  gambling_money in range(1,gambling_goal) :
        bet_size = 1
        win_or_lose = random.choice([-1, 1])  # Randomly chooses either -1 (lose) or 1 (win)
        gambling_money += bet_size * win_or_lose
        gambling_situations.append(gambling_money)

    return gambling_situations

def draw_gambler_situation():
    '''
    Visualizes the gambler's money progression.
    The graph shows whether the gambler reaches $100 or loses all their money.
    '''
    plt.plot(gamblers_ruin())
    plt.title("Gambling Situations")
    plt.xlabel("Number of Bets")    
    plt.ylabel("Gambler's Money")
    plt.yticks(np.arange(-20, 220, 20))
    plt.axhline(y=0, color='r', linestyle='-')
    plt.axhline(y=200, color='black', linestyle='-')
    plt.savefig("Markov_Chain_Result.jpg")
    print("File Saved")

def prob_of_ruin(gambling_goal, initial_money):
    '''
    Calculates the probability of the gambler losing all their money before reaching the goal.

    Args:
        gambling_goal (int): The target amount of money.
        initial_money (int): The gambler's starting money.

    Returns:
        float: The probability of ruin.
    '''
    return (gambling_goal - initial_money) / gambling_goal

def simulate_gamblers_ruin(num):
    '''
    Runs multiple simulations to estimate the expected value of the gambler's final money.
    Since a single simulation is insufficient to estimate probability, 
    running multiple simulations helps approximate the expected outcome.

    Args:
        num (int): Number of simulations to run.

    Returns:
        None (prints the expected value of the gambler's final money).
    '''
    simulation_results = [gamblers_ruin()[-1] for _ in range(num)]
    print(f"Expectation after {num} simulations: {np.mean(simulation_results)}")

if __name__ == "__main__":
    draw_gambler_situation()
    print(prob_of_ruin(100, 50)) 
    simulate_gamblers_ruin(1000)  # Example with 1000 simulations
    
