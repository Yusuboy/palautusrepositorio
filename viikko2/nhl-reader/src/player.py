class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']

    def __str__(self):
        total_goals_assists = self.goals + self.assists
        return f"{self.name:20} team {self.team:4} {self.goals:2} + {self.assists:2} =  {total_goals_assists}"
