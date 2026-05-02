"""Board game exercise models."""


class GameSession:
    def __init__(self, game_name: str, players: list, result_type: str, results: list):
        """Game session constructor."""
        self.game_name = game_name
        self.players = players
        self.result_type = result_type
        self.results = results

    def get_winner(self) -> str:
        """Get the winner of the current session."""
        if self.result_type == "winner":
            return self.results[0]

        if self.result_type == "places":
            return self.results[0]

        if self.result_type == "points":
            point_list = [int(p) for p in self.results]
            max_points = max(point_list)
            winner_index = point_list.index(max_points)
            return self.players[winner_index]

        return ""

    def get_loser(self) -> str:
        """Get the loser of the current session (only points and places)."""
        if self.result_type == "places":
            return self.results[-1]

        if self.result_type == "points":
            point_list = [int(p) for p in self.results]
            min_points = min(point_list)
            loser_index = point_list.index(min_points)
            return self.players[loser_index]

        return ""

    def get_points_for_player(self, player_name: str) -> int:
        """Return the number of points of a player in the current session."""
        if self.result_type == "points" and player_name in self.players:
            player_index = self.players.index(player_name)
            return int(self.results[player_index])
        return 0

    def is_player_in_session(self, player_name: str) -> bool:
        """Check if a player is in the current session."""
        return player_name in self.players


class Player:
    def __init__(self, name: str):
        """Player constructor."""
        self.name = name
        self.sessions = []

    def get_played_count(self) -> int:
        """Return number of sessions played."""
        return len(self.sessions)

    def get_won_count(self) -> int:
        """Return number of won sessions."""
        return sum(1 for s in self.sessions if s.get_winner() == self.name)


class Game:
    def __init__(self, name: str):
        """Game constructor."""
        self.name = name
        self.sessions = []

    def get_total_played(self) -> int:
        """Get all played sessions of a game."""
        return len(self.sessions)

    def get_player_most_wins(self) -> str:
        """Get the player with most wins in a game."""
        win_counts = {}
        for s in self.sessions:
            winner = s.get_winner()
            win_counts[winner] = win_counts.get(winner, 0) + 1

        if not win_counts: return ""
        return max(win_counts, key=win_counts.get)