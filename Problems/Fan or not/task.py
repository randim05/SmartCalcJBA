def add_viewer(name, team=None):
    if team is None:
        team = list()
        team.append(name)
    else:
        team.append(name)
    return team
