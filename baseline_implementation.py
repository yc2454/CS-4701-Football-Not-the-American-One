# -*- coding: utf-8 -*-
"""Baseline-Implemenation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VEK2A4XdSQ8amMzt6fuEoZOG44YmQR-x
"""

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 1.x

import gym
import numpy as np
from stable_baselines import PPO2
from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.evaluation import evaluate_policy
import gym_futbol

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/gym-futbol/gym_futbol/envs

env = gym.make('Futbol-v0')

model = PPO2(MlpPolicy, env, verbose=1)

model.learn(total_timesteps=10000)

def evaluate(model, num_episodes=100):
    env = model.get_env()
    all_episode_rewards = []
    for i in range(num_episodes):
        episode_rewards = []
        done = False
        obs = env.reset()
        while not done:
           
            action, _states = model.predict(obs)
            obs, reward, done, info = env.step(action)
            episode_rewards.append(reward)

        all_episode_rewards.append(sum(episode_rewards))

    mean_episode_reward = np.mean(all_episode_rewards)
    print("Mean reward:", mean_episode_reward, "Num episodes:", num_episodes)

    return mean_episode_reward

env = model.get_env()
env

obs = env.reset()
action, _states = model.predict(obs)

action[0]

obs, reward, done, info = env.step(action)

reward[0]

obs

reward
