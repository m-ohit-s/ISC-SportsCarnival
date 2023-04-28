class PlayerQuery:
    @staticmethod
    def insert_in_players():
        return f"""
                    insert into dbo.players(player_name) OUTPUT INSERTED.player_id
                    values(?);
                """
