from models import GameSession, Player, Game


class Statistics:
    def __init__(self, filename: str):
        self.all_sessions = []
        self.players = {}
        self.games = {}

        # Siin loe faili:
        # 1. Tükelda rida
        # 2. Loo GameSession objekt
        # 3. Loo/uuenda Player ja Game objekte ja lisa sessioon nende listidesse