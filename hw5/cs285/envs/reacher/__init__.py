from gym.envs.registration import register

register(
    id='reacher-cs285-v0',
    entry_point='hw5.cs285.envs.reacher:Reacher7DOFEnv',
    max_episode_steps=500,
)
from hw5.cs285.envs.reacher.reacher_env import Reacher7DOFEnv
