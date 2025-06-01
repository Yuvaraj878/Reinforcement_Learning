# POLICY ITERATION ALGORITHM

## AIM
The aim of this experiment is to implement the Policy Iteration Algorithm to determine the optimal policy for a given Markov Decision Process (MDP). The algorithm iteratively evaluates and improves policies until convergence, optimizing the decision-making process in a stochastic environment.

## PROBLEM STATEMENT
The Frozen Lake environment is a grid-based game where an agent must navigate from the start to the goal while avoiding holes. The agent can move left, right, up, or down, but due to the slippery surface, it may not always move as intended. The goal is to find an optimal policy using the Policy Iteration Algorithm to maximize the chances of reaching the goal while minimizing the risk of falling into holes.

## POLICY ITERATION ALGORITHM

Step 1 : Initialize the policy pi. In this implementation, a random action is chosen for each state s in the MDP P. The initial policy is represented by the lambda function pi=lambda s:{s:a for s,a in enumerate(random_actions)}[s], where random_actions is a list of randomly chosen actions for each state.

Step 2 : Enter a loop that continues until the policy pi is no longer changing. This is determined by comparing the previous policy (old_pi) with the current policy computed in the loop.

Step 3 : Store the previous policy as old_pi for comparison later.

Step 4 : Perform policy evaluation using the function policy_evaluation. This step calculates the state-values (V) for each state s given the current policy pi. The state-values represent the expected cumulative rewards starting from state s following policy pi and discounting future rewards by a factor of gamma. The function policy_evaluation is called with the arguments pi, P, gamma, and theta.

Step 5 : Perform policy improvement using the function policy_improvement. This step updates the policy pi based on the current state-values V. The function policy_improvement is called with the arguments V, P, and gamma.

Step 6 : Check if the policy has converged by comparing the previous policy old_pi with the current policy {s:pi(s) for s in range(len(P))}. If they are the same for all states s, the loop is exited.

Step 7 : Return the final state-values V and the optimal policy pi.

## POLICY IMPROVEMENT FUNCTION
#### Name : Thiyagarajan A
#### Register Number : 212222240110
```python
def policy_improvement(V, P, gamma=1.0):
    Q = np.zeros((len(P), len(P[0])), dtype=np.float64)
    # Write your code here to implement policy improvement algorithm
    for s in range(len(P)):
      for a in range(len(P[s])):
        for prob, next_state,reward, done in P[s][a]:
          Q[s][a]+= prob*(reward+gamma*V[next_state]*(not done))
          new_pi = lambda s: {s:a for s, a in enumerate(np.argmax(Q, axis=1))}[s]

    return new_pi
```
## POLICY ITERATION FUNCTION
#### Name : Thiyagarajan A
#### Register Number : 212222240110
```python
def policy_iteration(P, gamma=1.0,theta=1e-10):
  random_actions=np.random.choice(tuple(P[0].keys()),len(P))
  pi = lambda s: {s:a for s, a in enumerate(random_actions)}[s]
  while True:
    old_pi = {s:pi(s) for s in range(len(P))}
    V = policy_evaluation(pi, P,gamma,theta)
    pi = policy_improvement(V,P,gamma)
    if old_pi == {s:pi(s) for s in range(len(P))}:
      break
  return V,pi
```

## OUTPUT:
### 1. Policy, Value function and success rate for the Adversarial Policy

![image](https://github.com/user-attachments/assets/2be9ea72-3110-4a04-a515-682264208a44)
![image](https://github.com/user-attachments/assets/4a8f58b0-115c-4f51-92c6-b2d3fd1c4307)

![image](https://github.com/user-attachments/assets/6f1ab473-c718-4686-9d15-efe58474bad2)



### 2. Policy, Value function and success rate for the Improved Policy

![image](https://github.com/user-attachments/assets/cf318125-8c1e-4b4a-9ba3-dfd019107234)
![image](https://github.com/user-attachments/assets/1e983d0b-2887-4dd9-af13-67b61b90259d)

![image](https://github.com/user-attachments/assets/09176a34-4775-457e-a885-82467e7d4e49)
![image](https://github.com/user-attachments/assets/cde82ae4-d909-45b3-9ea2-5fe4350368a8)



### 3. Policy, Value function and success rate after policy iteration
![image](https://github.com/user-attachments/assets/bf439fa2-f589-45c3-94c0-9e0f5c25317b)
![image](https://github.com/user-attachments/assets/04726ddc-922f-4014-b78e-78c34f11e3ba)

![image](https://github.com/user-attachments/assets/53209499-7331-471c-9061-18d3ffe3b41d)




## RESULT:

Thus, a Python program is developed to find the optimal policy for the given MDP using the policy iteration algorithm.
