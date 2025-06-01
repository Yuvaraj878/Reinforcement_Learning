# Q Learning Algorithm


## AIM
To develop a Python program to find the optimal policy for the given RL environment using Q-Learning and compare the state values with the Monte Carlo method.
## PROBLEM STATEMENT
Develop a Python program to derive the optimal policy using Q-Learning and compare state values with Monte Carlo method.
## Q LEARNING ALGORITHM
### Step 1:
Initialize Q-table and hyperparameters.

### Step 2:
Choose an action using the epsilon-greedy policy and execute the action, observe the next state, reward, and update Q-values and repeat until episode ends.

### Step 3:
After training, derive the optimal policy from the Q-table.

### Step 4:
Implement the Monte Carlo method to estimate state values.

### Step 5:
Compare Q-Learning policy and state values with Monte Carlo results for the given RL environment.
## Q LEARNING FUNCTION
### Name: Thiyagarajan A
### Register Number:212222240110
```py
def q_learning(env, 
               gamma=1.0,
               init_alpha=0.5,
               min_alpha=0.01,
               alpha_decay_ratio=0.5,
               init_epsilon=1.0,
               min_epsilon=0.1,
               epsilon_decay_ratio=0.9,
               n_episodes=3000):
    nS, nA = env.observation_space.n, env.action_space.n
    pi_track = []
    Q = np.zeros((nS, nA), dtype=np.float64)
    Q_track = np.zeros((n_episodes, nS, nA), dtype=np.float64)
    select_action = lambda state,Q,epsilon: np.argmax(Q[state]) if np.random.random()>epsilon else np.random.randint(len(Q[state]))
    alphas=decay_schedule(init_alpha,min_alpha,alpha_decay_ratio,n_episodes)
    epsilons = decay_schedule(init_epsilon,min_epsilon,epsilon_decay_ratio,n_episodes)
    for e in tqdm(range(n_episodes),leave=False):
      state,done=env.reset(),False
      action=select_action(state,Q,epsilons[e])
      while not done:
        
        action=select_action(state,Q,epsilons[e])
        next_state,reward,done,_=env.step(action)
        td_target=reward+gamma*Q[next_state].max()*(not done)
        td_error=td_target-Q[state][action]
        Q[state][action]=Q[state][action]+alphas[e]*td_error
        state=next_state
      Q_track[e]=Q
      pi_track.append(np.argmax(Q,axis=1))
    V=np.max(Q,axis=1)
    pi=lambda s:{s:a for s,a in enumerate(np.argmax(Q,axis=1))}[s]
    return Q, V, pi, Q_track, pi_track
 
```

## OUTPUT:
### Optimal value functions and policy
![image](https://github.com/user-attachments/assets/3d504a50-959d-42ba-94af-d5630cdc9b6c)

![Screenshot 2025-05-14 201815](https://github.com/user-attachments/assets/b8cd824a-491c-4740-a374-e9038341dfbe)

![Screenshot 2025-05-14 201925](https://github.com/user-attachments/assets/b03b8168-5583-4c36-b53c-c7cee5822cf1)



### Comparison
### First-visit Monte-Carlo
![Untitled](https://github.com/user-attachments/assets/d49d5692-aea1-423c-9ac6-96860edf6d00)


### Q_LEARNING

![Untitled-1](https://github.com/user-attachments/assets/818e13c1-5ecd-4f22-87f2-3a1988b10c58)



## RESULT:

Therefore a python program has been successfully developed to find the optimal policy for the given RL environment using Q-Learning and compared the state values with the Monte Carlo method.
