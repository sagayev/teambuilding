import itertools

# Define the players and their scores and positions

players = {'Tofiq': {'score': 8.7, 'position': 'goalkeeper'},
           'Omarxan': {'score': 8.9, 'position': 'striker'},
           'Seymur': {'score': 6.2, 'position': 'midfielder'},
           'Samir': {'score': 5.1, 'position': 'goalkeeper'},
           'Ilkin': {'score': 6.5, 'position': 'midfielder'},
           'Akif': {'score': 6.3, 'position': 'midfielder'},
           'Fariz': {'score': 8.9, 'position': 'striker'},
           'Ibrahim': {'score': 8.1, 'position': 'midfielder'},
           'Turxan' :{'score': 7, 'position': 'midfielder'},
           'Baba':{'score': 8.6, 'position': 'midfielder'},
           'Sabit':{'score': 8, 'position': 'midfielder'},
           'Xezan':{'score': 5.5, 'position': 'midfielder'},
           
           }

# The number of players per team
if len(players)%2 == 0:
    players_per_team = len(players) // 2
else: 
    players_per_team = (len(players) - 1) // 2

# Create a list of all possible team combinations
team_combinations_1 = list(itertools.combinations(list(players.keys()), players_per_team  ))
team_combinations_2 = [tuple(set(players.keys()).difference(y)) for y in team_combinations_1]
team_combinations = zip(team_combinations_1, team_combinations_2)

# Filter out combinations that don't have a goalkeeper and striker on each team
valid_combinations = []
for combination in team_combinations:
    team_1 = combination[0]
    team_2 = combination[1]
    positions_1 = [players[player]['position'] for player in team_1]
    positions_2 = [players[player]['position'] for player in team_2]

    if all(['goalkeeper' in positions_1, 'goalkeeper' in positions_2, 'striker' in positions_1, 'striker' in positions_2]):
        valid_combinations.append(combination)


# Calculate the total score for each team in each valid combination
team_scores_differences = []
for combination in valid_combinations:
    team_scores_per_combination = []
    team_1 = combination[0]
    team_2 = combination[1]
    team_score_1 = sum(players[player]['score'] for player in team_1)
    team_score_2 = sum(players[player]['score'] for player in team_2)
    team_scores_diff = abs(team_score_1 - team_score_2)
    team_scores_differences.append(team_scores_diff)


# Combine the score differences with combinations
combined_list = zip(valid_combinations, team_scores_differences)
# Sort the list
sorted_combined_list = sorted(combined_list, key=lambda x: x[1])

# get the lowest 5 scores and their corresponding combinations
lowest_five = sorted_combined_list[:5]

# Print the best combinations
print('Best combinations:')
print()
for i, (combination, score_diff) in enumerate(lowest_five):
    print("OPTION ", i+1, " Score difference: ", score_diff)
    print()
    for team in combination:
        for player in team:
           print('- {}: {}, {}'.format(player, players[player]['score'], players[player]['position'])) 
        print()
    print()