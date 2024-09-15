# RL-snake-game

Overview: 

This project implements a reinforcement learning (RL) solution for the classic Snake game using the Q-learning algorithm. The bot is trained to play the game by learning optimal strategies over time based on rewards and penalties.

Key Features:


•  Q-Learning Algorithm: Uses Q-learning, a model-free RL algorithm, to train the snake to make optimal moves based on the current state and rewards.

•  State-Action Value Storage: Q-values, representing the state-action values, are stored in a qvalues.json file and updated as the game progresses.

•  Training Script: Learner.py is responsible for training the snake using Q-learning by adjusting its actions based on positive or negative feedback.

•  Initialization: InitializeQvalues.py initializes the Q-value table with default values.

•  Snake Game Implementation: The actual Snake game logic and gameplay are handled in snake.py.

•  Visualizing Q-values: printQvalues.py allows you to inspect the Q-values for analysis.

•  Progressive Learning: The bot improves its performance over time by continuously learning from past mistakes and successes.
