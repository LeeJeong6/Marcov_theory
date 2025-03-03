# Markov Theory
Markov theory is a mathematical framework used to model systems that transition between different states based on probabilities.

These two files are examples of Markov theory:

## Markov Chain -> `Markov_chain.py`
> Markov Chain is a sequence of states where transitions occur based on fixed probabilities.  
> No actions or rewards are involved.  
> Example: Weather changes (Sunny → Rainy with 30% probability).  

## Markov Decision Process (MDP) -> `Markov_Decision.py`
> An extension of the Markov Chain that includes actions and rewards.  
> The agent chooses an action at each state, influencing future states.  
> Used in reinforcement learning and decision-making problems.  

---

### **Code Differences**  

| Feature                  | Markov Chain Code          | Markov Decision Process Code |
|--------------------------|--------------------------|----------------------------------|
| **State Representation** | Gambler’s current money  | Gambler’s current money         |
| **Transition**           | Randomly win/lose 50%    | Chooses a bet size, then wins/loses |
| **Actions**              | No actions (fixed rules) | Policies determine bet size     |
| **Rewards**              | No rewards               | Implicit (money gained/lost)    |
| **Goal**                 | Reach $0 or $100         | Optimize betting strategy       |


### Gambling Risk and the Role of Probabilities
In the Markov Decision Process (MDP) simulation, when choosing the greedy policy, the gambler tends to take large bets with the hope of quickly reaching the goal. This aggressive approach can lead to either rapid success or failure, with an equal probability of +1 or -1 outcome. The gambler's fate is, therefore, highly dependent on these random outcomes.

However, if the probability distribution shifts, such that the probability of losing (+1) becomes slightly higher (e.g., 0.48 for +1 and 0.52 for -1), the situation changes significantly. In this case, even though the gambler's policy remains aggressive, the slightly higher probability of losing results in a higher likelihood of failure over time.

Running simulations with a modified probability distribution (such as 0.48 for +1 and 0.52 for -1) reveals how risky the gambler’s behavior can become. Even with the same number of simulations (e.g., 100 simulations), the impact of this small shift in probability illustrates the inherent danger of the gambling process.

Through these simulations, you can observe that gambling is inherently risky—even if a strategy seems favorable, small changes in the underlying probabilities can make success much harder to achieve and failure much more likely.
