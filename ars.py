# AI 2018

# Importing the libraries
import os
import numpy as np
import gym
from gym import wrappers
import pybullet_envs

# Setting the Hyper Parameters

class Hp():
    
    def __init__(self):
        self.nb_steps = 1000
        self.episode_length = 1000
        self.learning_rate = 0.02
        self.nb_directions = 16
        self.nb_best_directions = 16
        assert      self.nb_best_directions <= self.nb_directions
        self.noise = 0.03
        self.seed = 1
        self.env_name = ''
        
# Normalizing the States