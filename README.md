# Markov Theory
Markov theory is a mathematical framework used to model systems that transition between different states based on probabilities.

These three files demonstrate applications of Markov theory:

## Markov Chain -> `Markov_chain.py`
> Markov Chain is a sequence of states where transitions occur based on fixed probabilities.  
> No actions or rewards are involved.  
> **Example:** Weather changes (Sunny → Rainy with 30% probability).  
![Image](https://github.com/user-attachments/assets/a172f79d-42ad-48af-9078-3bd9aa9b5efc)

## Markov Decision Process (MDP) V1 -> `Markov_decision_v1 folder `
> An extension of the Markov Chain that includes actions and rewards.  
> The agent chooses an action at each state, influencing future states.  
> Used in reinforcement learning and decision-making problems.  
> **Focus:** Evaluating the effectiveness of different betting strategies.

## Markov Decision Process (MDP) V2 -> `Markov_decision_v2 folder`
> A modified version of MDP V1 that incorporates discounted rewards.  
> Tracks cumulative rewards over time with a discount factor.  
> **Focus:** Understanding long-term profitability by applying reward discounting.

---

## **Code Differences**  

| Feature                  | `Markov_chain.py`          | `Markov_decision_v1`       | `Markov_decision_v2`       |
|--------------------------|--------------------------|------------------------------|------------------------------|
| **State Representation** | Gambler’s current money  | Gambler’s current money     | Gambler’s current money     |
| **Transition**           | Randomly win/lose 50%    | Chooses a bet size, then wins/loses | Chooses a bet size, then wins/loses |
| **Actions**              | No actions (fixed rules) | Policies determine bet size | Policies determine bet size |
| **Rewards**              | No rewards               | Implicit (money gained/lost) | Discounted cumulative rewards |
| **Goal**                 | Reach $0 or $100         | Optimize betting strategy   | Optimize long-term profitability |

---

## **V1: Evaluating the Effectiveness of Different Strategies**  
In the first version (`Markov_decision_v1`), the focus is on analyzing which betting strategy is more effective.  
By running multiple simulations, we compare different policies (**random vs. greedy**) to see which one leads to better outcomes.  
The results highlight how choosing a particular betting approach impacts the **final amount of money** after a certain number of rounds.

---

## **V2: Discounted Rewards and Long-Term Profitability**  
In the second version (`Markov_decision_v2`), a **discount factor** is introduced to analyze long-term profitability over 50 time steps.  
Instead of simply evaluating the **final outcome**, we track how rewards accumulate over time using a discount rate.  
This places more emphasis on **short-term gains** while gradually reducing the weight of future rewards.  
By doing so, we gain insights into how different strategies perform when future rewards are **valued less than immediate gains**.

---

## **Gambling Risk and the Role of Probabilities**  
In the Markov Decision Process (MDP) simulation, choosing the **greedy policy** often leads to **aggressive betting** in hopes of quickly reaching the goal.  
This strategy can result in rapid **success or failure**, depending on the probabilities of winning and losing.

However, when the probability of losing is slightly increased (**e.g., 52% lose, 48% win**), the impact becomes evident.  
Even a small change in the probability distribution can **significantly affect** the gambler’s long-term success rate.

By comparing the results from both `V1` and `V2`, it becomes clear that:  
- **The choice of strategy matters.**  
- **How we evaluate rewards over time also matters.**  
- **Introducing discounted rewards in `V2` provides deeper insight into long-term risks and profitability.**  

These simulations reinforce the importance of considering **long-term risks and rewards** in decision-making, rather than focusing solely on **immediate outcomes**.
