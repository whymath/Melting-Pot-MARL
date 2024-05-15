# Import necessary libraries
import numpy as np

# Example observations we might need
# Assuming we have a list of dictionaries where each dictionary represents an apple field observation
# and contains information about the number of apples, whether it is depleted, regrowth rate, etc.
apple_fields = [
    {'field_id': 1, 'initial_apples': 100, 'harvested_apples': 80, 'regrown_apples': 20, 'is_depleted': False},
    {'field_id': 2, 'initial_apples': 100, 'harvested_apples': 100, 'regrown_apples': 0, 'is_depleted': True},
    # Add more fields as needed
]

# Assuming we have a list of dictionaries where each dictionary represents an agent's actions
# and contains information about the number of cooperative actions, total actions, etc.
agents = [
    {'agent_id': 1, 'cooperative_actions': 30, 'total_actions': 50, 'reduction_in_overharvesting': 5, 'total_punishments': 2},
    {'agent_id': 2, 'cooperative_actions': 20, 'total_actions': 50, 'reduction_in_overharvesting': 3, 'total_punishments': 1},
    # Add more agents as needed
]

# 1. Number of Apple Fields Depleted
def calculate_depleted_fields(apple_fields):
    return sum(1 for field in apple_fields if field['is_depleted'])

# 2. Average Apple Regrowth Rate
def calculate_average_regrowth_rate(apple_fields):
    total_regrowth = sum(field['regrown_apples'] for field in apple_fields)
    return total_regrowth / len(apple_fields)

# 3. Total Apples Harvested
def calculate_total_apples_harvested(apple_fields):
    return sum(field['harvested_apples'] for field in apple_fields)

# 4. Harvest-to-Regrowth Ratio
def calculate_harvest_to_regrowth_ratio(apple_fields):
    total_harvested = sum(field['harvested_apples'] for field in apple_fields)
    total_regrown = sum(field['regrown_apples'] for field in apple_fields)
    return total_harvested / total_regrown if total_regrown > 0 else float('inf')

# 5. Cooperation Index
def calculate_cooperation_index(agents):
    total_cooperative_actions = sum(agent['cooperative_actions'] for agent in agents)
    total_actions = sum(agent['total_actions'] for agent in agents)
    return total_cooperative_actions / total_actions

# 6. Punishment Effectiveness
def calculate_punishment_effectiveness(agents):
    total_reduction_in_overharvesting = sum(agent['reduction_in_overharvesting'] for agent in agents)
    total_punishments_administered = sum(agent['total_punishments'] for agent in agents)
    return total_reduction_in_overharvesting / total_punishments_administered

# 7. Resource Sustainability Score
def calculate_resource_sustainability_score(apple_fields, alpha=1, beta=1, gamma=1):
    total_regrowth_rate = sum(field['regrown_apples'] for field in apple_fields) / len(apple_fields)
    total_fields = len(apple_fields)
    number_of_depleted_fields = sum(1 for field in apple_fields if field['is_depleted'])
    harvest_to_regrowth_ratio = sum(field['harvested_apples'] for field in apple_fields) / sum(field['regrown_apples'] for field in apple_fields if field['regrown_apples'] > 0)
    
    sustainability_score = (
        alpha * total_regrowth_rate +
        beta * (1 - number_of_depleted_fields / total_fields) +
        gamma * (1 / harvest_to_regrowth_ratio)
    )
    return sustainability_score

# 8. Economic Efficiency
def calculate_economic_efficiency(apple_fields, total_rewards):
    total_apples_harvested = sum(field['harvested_apples'] for field in apple_fields)
    total_fields = len(apple_fields)
    number_of_depleted_fields = sum(1 for field in apple_fields if field['is_depleted'])
    
    economic_efficiency = (total_rewards / total_apples_harvested) * (1 - number_of_depleted_fields / total_fields)
    return economic_efficiency

# Example usage
cooperation_index = calculate_cooperation_index(agents)
punishment_effectiveness = calculate_punishment_effectiveness(agents)
resource_sustainability_score = calculate_resource_sustainability_score(apple_fields, alpha=1, beta=1, gamma=1)
economic_efficiency = calculate_economic_efficiency(apple_fields, total_rewards=500)

# Print the results
print(f"Cooperation Index: {cooperation_index}")
print(f"Punishment Effectiveness: {punishment_effectiveness}")
print(f"Resource Sustainability Score: {resource_sustainability_score}")
print(f"Economic Efficiency: {economic_efficiency}")