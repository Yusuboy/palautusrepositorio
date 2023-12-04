class TennisGame:
    SCORE_MAPPING = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty",
    }

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.get_equal_score()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.get_advantage_or_win()
        else:
            return self.get_regular_score()

    def get_equal_score(self):
        if self.player1_score < 3:
            return f"{self.SCORE_MAPPING[self.player1_score]}-All"
        else:
            return "Deuce"

    def get_advantage_or_win(self):
        minus_result = self.player1_score - self.player2_score

        if minus_result == 1:
            return "Advantage player1"
        elif minus_result == -1:
            return "Advantage player2"
        elif minus_result >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def get_regular_score(self):
        score = ""
        for i in range(2):
            if i == 1:
                score += "-"
            score += self.SCORE_MAPPING[self.player1_score] if i == 0 else self.SCORE_MAPPING[self.player2_score]
        return score
