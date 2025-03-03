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
