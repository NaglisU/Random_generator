import random


def create_teams(num_teams: int, num_names: int, names: list):
    """
    Creating random teams
    :param num_teams: Number of teams required
    :param num_names: Number of names given
    :param names: List of names given
    :return: Generated random teams
    """

    random.shuffle(names)  # Randomize name data

    # Calculate team sizes

    team_sizes = [num_names // num_teams] * num_teams
    remaining = num_names % num_teams
    for i in range(remaining):
        team_sizes[i] += 1

    # Generate teams

    teams = []
    start_index = 0
    for size in team_sizes:
        end_index = start_index + size
        team = names[start_index:end_index]
        teams.append(team)
        start_index = end_index

    return teams
