"""Board game exercise models."""


class GameSession:
    def __init__(self, game_name: str, player_names: list, result_type: str, results: list):
        """Game session constructor."""
        self.game_name = game_name
        self.player_names = player_names
        self.result_type = result_type
        self.results = results

    def get_winner(self) -> str:
        """Get the winner of the current session."""
        if self.result_type == "winner":
            return self.results[0]
        if self.result_type == "places":
            return self.results[0]
        if self.result_type == "points":
            int_results = [int(p) for p in self.results]
            max_idx = int_results.index(max(int_results))
            return self.player_names[max_idx]
        return ""

    def get_loser(self) -> str:
        """Get the loser of the current session (only points and places)."""
        if self.result_type == "places":
            return self.results[-1]
        if self.result_type == "points":
            int_results = [int(p) for p in self.results]
            min_idx = int_results.index(min(int_results))
            return self.player_names[min_idx]
        return ""


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