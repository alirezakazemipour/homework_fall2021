from gym.envs.registration import register

register(
    id='cheetah-cs285-v0',
    entry_point='hw5.cs285.envs.cheetah:HalfCheetahEnv',
    max_episode_steps=1000,
)
from hw5.cs285.envs.cheetah.cheetah import HalfCheetahEnv
