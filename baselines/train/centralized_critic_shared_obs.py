
from ray.rllib.models import ModelCatalog
from ray.rllib.policy import policy
from ray.rllib.models import ModelCatalog
from ray.rllib.examples.models.centralized_critic_models import YetAnotherCentralizedCriticModel, YetAnotherTorchCentralizedCriticModel


def register_centralized_critic_model(args):
    # TODO: Implement custom model and use that
    if args.central_critic == "shared_obs":
        cc_model = YetAnotherCentralizedCriticModel
        if args.framework == "torch":
            cc_model = YetAnotherTorchCentralizedCriticModel
        ModelCatalog.register_custom_model("cc_model", cc_model)
    return


def create_policies_for_centralized_critic(base_env, players_count):
    policies = {}
    player_to_agent = {}

    for i in range(players_count):
        observation_space_i = base_env.observation_space[f"player_{i}"]
        rgb_shape = observation_space_i["RGB"].shape
        sprite_x = rgb_shape[0] * players_count
        sprite_y = rgb_shape[1] * players_count
        observation_space_i["RGB"].shape = (sprite_x, sprite_y, rgb_shape[2]) # TODO: Check if this will work, or if we need to switch 

        policies[f"agent_{i}"] = policy.PolicySpec(
            # observation_space=base_env.observation_space[f"player_{i}"],
            observation_space=observation_space_i,
            action_space=base_env.action_space[f"player_{i}"],
            config={
                "model": {
                    "conv_filters": [[16, [8, 8], 1],
                                    [128, [sprite_x, sprite_y], 1]],
                },
            })
        player_to_agent[f"player_{i}"] = f"agent_{i}"

    return policies, player_to_agent


def centralized_critic_observation_fn(agent_obs):
    new_obs = {}
    for i in range(len(agent_obs)):
        new_obs[i] = {
            "own_obs": agent_obs[i],
            "opponent_obs": agent_obs[0], # TODO: Update other agents' observations
            "opponent_action": 0,
        }
    return new_obs
