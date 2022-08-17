import torch

import hw3.cs285.infrastructure.pytorch_util as ptu


class ArgMaxPolicy(object):

    def __init__(self, critic):
        self.critic = critic

    def get_action(self, obs):
        if len(obs.shape) > 3:
            observation = obs
        else:
            observation = obs[None]

        ## TODO return the action that maxinmizes the Q-value 
        # at the current observation as the output
        observation = ptu.from_numpy(observation)
        q_values = self.critic.q_net(observation)
        action = torch.argmax(q_values, -1).detach().cpu().numpy()
        return action.squeeze()
