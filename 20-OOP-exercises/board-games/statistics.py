from models import GameSession, Player, Game


class Statistics:
    def __init__(self, filename: str):
        self.all_results = []
        self.players = {}
        self.games = {}

        self._read_file(filename)

    def _read_file(self, filename: str):
        """Read from file and create entities."""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                for line in f:
                    if not line.strip():
                        continue

                    parts = line.strip().split(';')
                    if len(parts) != 4:
                        continue

                    game_name = parts[0]
                    player_names = parts[1].split(',')
                    result_type = parts[2]
                    results = parts[3].split(',')

                    session = GameSession(game_name, player_names, result_type, results)
                    self.all_results.append(session)

                    if game_name not in self.games:
                        self.games[game_name] = Game(game_name)
                    self.games[game_name].sessions.append(session)

                    for name in player_names:
                        if name not in self.players:
                            self.players[name] = Player(name)
                        self.players[name].sessions.append(session)

        except FileNotFoundError:
            print(f"Viga: Faili {filename} ei leitud.")

    def get(self, path: str):
        """
        Manage API calls.

        Divide path into parts and call methods.
        """
        # Puhastame tee ja jagame osadeks
        parts = path.strip("/").split("/")

        if parts[0] in ["players", "games", "total"]:
            return self._get_general_stats(parts)

        if parts[0] == "player" and len(parts) >= 3:
            return self._get_player_stats(parts[1], parts[2])

        if parts[0] == "game" and len(parts) >= 3:
            return self._get_game_stats(parts[1], parts[2])

        return None

    def _get_general_stats(self, parts: list):
        """Get general statistics: players, games, total."""
        if parts[0] == "players":
            return list(self.players.keys())
        if parts[0] == "games":
            return list(self.games.keys())
        if parts[0] == "total":
            if len(parts) == 1:
                return len(self.all_results)
            return sum(1 for res in self.all_results if res.result_type == parts[1])
        return None

    def _get_player_stats(self, name: str, action: str):
        """Get statistics about a player."""
        player = self.players.get(name)
        if not player:
            return 0 if action in ["amount", "won"] else None

        if action == "amount":
            return player.get_played_count()
        if action == "won":
            return player.get_won_count()
        if action == "favourite":
            game_counts = {}
            for s in player.sessions:
                game_counts[s.game_name] = game_counts.get(s.game_name, 0) + 1
            return max(game_counts, key=lambda k: game_counts[k]) if game_counts else None
        return None

    def _get_game_stats(self, name: str, action: str):
        """Get statistics about a game."""
        game = self.games.get(name)
        if not game:
            return 0

        if action == "amount":
            return game.get_total_played()
        if action == "player-amount":
            return self._calculate_most_frequent_player_count(game)
        if action == "most-wins":
            return self._calculate_most_wins(game)
        if action == "most-frequent-winner":
            return self._calculate_frequent_winner(game)
        if action == "most-losses":
            return self._calculate_most_losses(game)
        if action == "most-frequent-loser":
            return self._calculate_frequent_loser(game)
        if action == "record-holder":
            return self._calculate_record_holder(game)
        return None

    def _calculate_favourite_game(self, player):
        """Get a player's favourite/most playes game."""
        counts = {}
        for s in player.sessions:
            counts[s.game_name] = counts.get(s.game_name, 0) + 1
        return max(counts, key=lambda k: counts[k]) if counts else None

    def _calculate_most_frequent_player_count(self, game):
        """Get the player who played the most frequently in a game."""
        counts = {}
        for s in game.sessions:
            p_count = len(s.players)
            counts[p_count] = counts.get(p_count, 0) + 1
        return max(counts, key=lambda k: counts[k]) if counts else 0

    def _calculate_most_wins(self, game):
        """Calculate the highest number of wins in a game."""
        win_counts = {}
        for s in game.sessions:
            winner = s.get_winner()
            win_counts[winner] = win_counts.get(winner, 0) + 1
        return max(win_counts, key=lambda k: win_counts[k]) if win_counts else None

    def _calculate_frequent_winner(self, game):
        """Calculate who had the most wins out of their participations."""
        stats = {}  # {nimi: [võidud, osalused]}
        for s in game.sessions:
            winner = s.get_winner()
            for p_name in s.players:
                if p_name not in stats: stats[p_name] = [0, 0]
                stats[p_name][1] += 1
                if p_name == winner:
                    stats[p_name][0] += 1
        return max(stats, key=lambda p: stats[p][0] / stats[p][1])

    def _calculate_most_losses(self, game):
        """Calculate the highest number of losses in a game."""
        loss_counts = {}
        for s in game.sessions:
            if s.result_type in ["points", "places"]:
                loser = s.get_loser()
                loss_counts[loser] = loss_counts.get(loser, 0) + 1
        return max(loss_counts, key=lambda k: loss_counts[k]) if loss_counts else None

    def _calculate_frequent_loser(self, game):
        """Calculate the highest frequency of losses in a game."""
        stats = {}  # {nimi: [kaotused, osalused]}
        for s in game.sessions:
            if s.result_type in ["points", "places"]:
                loser = s.get_loser()
                for p_name in s.players:
                    if p_name not in stats: stats[p_name] = [0, 0]
                    stats[p_name][1] += 1
                    if p_name == loser:
                        stats[p_name][0] += 1
        return max(stats, key=lambda p: stats[p][0] / stats[p][1])

    def _calculate_record_holder(self, game):
        """Find the holder of the overall highest points."""
        record_score = -1
        holder = None
        for s in game.sessions:
            if s.result_type == "points":
                point_list = [int(p) for p in s.results]
                current_max = max(point_list)
                if current_max > record_score:
                    record_score = current_max
                    holder = s.players[point_list.index(current_max)]
        return holder